import os
import sqlite3
import logging
import numpy as np
import pandas as pd
from datetime import datetime
from typing import Optional

from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


class SqlHandler:

    def __init__(self, dbname: str, table_name: str) -> None:
        """
        Initializes a new instance of the SqlHandler class.

        Parameters:
            dbname (str): The name of the SQLite database file.
            table_name (str): The name of the table in the
            database to interact with.
        """

        self.cnxn = sqlite3.connect(f'{dbname}.db')
        self.cursor = self.cnxn.cursor()
        self.dbname = dbname
        self.table_name = table_name

# ____________________________________________________________________________

    def close_cnxn(self) -> None:
        """
        Closes the database connection.

        This method should be called when finished with database operations.
        """
        logger.info('Committing the changes')
        self.cursor.close()
        self.cnxn.close()
        logger.info('The connection has been closed')

# ____________________________________________________________________________

    def get_table_columns(self) -> list:
        """
        Retrieves the column names of the specified table.

        Returns:
            list: A list of column names.
        """
        self.cursor.execute(f"PRAGMA table_info({self.table_name});")
        columns = self.cursor.fetchall()
        column_names = [col[1] for col in columns]
        logger.info(f'The list of columns: {column_names}')
        return column_names

# ____________________________________________________________________________

    def truncate_table(self) -> None:
        """
        Drops the table if it exists.

        This method deletes all data and structure from the table.
        """
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        self.cursor.execute(query)
        logger.info(f'The {self.table_name} table is truncated')
        self.cnxn.commit()

# ____________________________________________________________________________

    def insert_many(self, df: pd.DataFrame) -> None:
        """
        Inserts data from a DataFrame into the database table.

        Parameters:
            df (pd.DataFrame): The DataFrame containing the data to insert.
        """
        df = df.replace(np.nan, None)
        df.rename(columns=lambda x: x.lower(), inplace=True)
        columns = list(df.columns)
        logger.info(f'BEFORE the column intersection: {columns}')
        sql_column_names = [i.lower() for i in self.get_table_columns()]
        columns = list(set(columns) & set(sql_column_names))

        logger.info(f'AFTER the column intersection: {columns}')
        ncolumns = list(len(columns) * '?')
        data_to_insert = df.loc[:, columns]
        values = [tuple(i) for i in data_to_insert.values]
        logger.info(f'The shape of the table which is going to be imported {data_to_insert.shape}')  # noqa: E501

        if len(columns) > 1:
            cols, params = ', '.join(columns), ', '.join(ncolumns)
        else:
            cols, params = columns[0], ncolumns[0]

        logger.info(f'Insert structure: colnames: {cols} params: {params}')
        logger.info(values[0])
        query = f"""INSERT INTO {self.table_name} ({cols}) VALUES ({params});"""  # noqa: E501
        logger.info(f'QUERY: {query}')

        self.cursor.executemany(query, values)
        self.cnxn.commit()
        logger.warning('The data is loaded')

# ____________________________________________________________________________

    def update_table(self, set_clause: str, condition: str) -> None:
        """
        Update rows in the table based on a condition.

        Parameters:
        - set_clause: A string that specifies the column values
        to be updated, e.g., "name = 'John', age = 30"
        - condition: A string that defines the condition for
        the rows to be updated, e.g., "subscriber_id = 1"
        """
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
        self.cursor.execute(query)
        self.cnxn.commit()
        logger.info(f"Updated rows in '{self.table_name}' where {condition}.")

# ____________________________________________________________________________

    def get_table_data(self, columns: list = None, condition: str = None) -> pd.DataFrame:  # noqa: E501
        """
        Retrieve data from the table based on the
        specified columns and optional condition.

        Parameters:
            columns (list): A list of column names to retrieve. If not filled,
            all columns will be retrieved.
            condition (str): An optional SQL condition to filter the data
            (e.g., "column_name = 'value'"). If not specified,
            all data will be retrieved.

        Returns:
            pd.DataFrame: A DataFrame containing the retrieved data.
        """
        if columns is None:
            columns = self.get_table_columns()

        if not columns:
            return pd.DataFrame()

        column_names = ', '.join(columns)

        query = f"SELECT {column_names} FROM {self.table_name}"
        if condition:
            query += f" WHERE {condition}"

        data = pd.read_sql_query(query, self.cnxn)
        return data

# ____________________________________________________________________________

    def get_rfm_data(self) -> pd.DataFrame:
        """
        Retrieve RFM (Recency, Frequency, Monetary)
        segmentation data from the database.

        Returns:
            pd.DataFrame: DataFrame containing RFM segmentation
            data with columns:
            - subscriber_id: Identifier for subscribers
            - recency_score: calculated during RFM analysis
            - frequency_score: calculated during RFM analysis
            - monetary_score: calculated during RFM analysis

        Raises:
            Any exceptions related to SQL query execution
            or DataFrame creation.
        """

        query = ' SELECT DISTINCT subscriber_id, recency_score, frequency_score, monetary_score FROM RFM_segmentation; '  # noqa: E501
        rfm_data = pd.read_sql_query(query, self.cnxn)
        return rfm_data

# ____________________________________________________________________________

    def segment_subscribers(self, rfm_data: pd.DataFrame) -> pd.DataFrame:
        """
        Segment subscribers into three groups based on
        their RFM (Recency, Frequency, Monetary) scores.

        Args:
            rfm_data (pd.DataFrame): RFM segmentation data with columns:
            - subscriber_id: Identifier for subscribers
            - recency_score: Recency score calculated during RFM analysis
            - frequency_score: Frequency score calculated during RFM analysis
            - monetary_score: Monetary score calculated during RFM analysis

        Returns:
            pd.DataFrame: DataFrame containing segmented subscribers
            with an additional 'Segment' column,
            where each subscriber is categorized as 'Low',
            'Medium', or 'High' based on their RFM scores.

        Raises:
            Any exceptions related to DataFrame manipulation
            or segmentation process.
        """
        # Segment subscribers into three groups based on their RFM scores
        rfm_data['Segment'] = pd.cut(rfm_data['recency_score'] + rfm_data['frequency_score'] + rfm_data['monetary_score'], bins=3, labels=['Low', 'Medium', 'High'])  # noqa: E501
        return rfm_data

# ____________________________________________________________________________

    def get_declining_customers(self, rfm_data: pd.DataFrame) -> pd.DataFrame:
        """
        Identify declining customers based on their
        RFM (Recency, Frequency, Monetary) segments.

        Args:
            rfm_data (pd.DataFrame): RFM segmentation data with columns:
            - subscriber_id: Identifier for subscribers
            - recency_score: Recency score calculated during RFM analysis
            - frequency_score: Frequency score calculated during RFM analysis
            - monetary_score: Monetary score calculated during RFM analysis

        Returns:
            pd.DataFrame: DataFrame containing only declining customers,
            i.e., customers categorized as 'Low' segment.

        Raises:
            Any exceptions related to DataFrame manipulation
            or filtering process.
        """
        # Identify declining customers based on their RFM segments
        declining_customers = rfm_data[rfm_data['Segment'] == 'Low']
        return declining_customers

# ____________________________________________________________________________

    def get_email_by_subscriber_id(self, subscriber_id):
        """
        Retrieve the email of a subscriber based on their
        subscriber_id from the rfm_segmentation_table.

        Args:
            cnxn (Connection): Database connection object.
            subscriber_id (int): Subscriber ID for which
            to retrieve the email.

        Returns:
            str or None: Email of the subscriber
            if found, None otherwise.
        """
        query = """
            SELECT s.email
            FROM rfm_segmentation r
            INNER JOIN subscriber s ON r.subscriber_id = s.subscriber_id
            WHERE r.subscriber_id = ?
            LIMIT 1
        """

        try:
            # Execute the SQL query
            email_data = pd.read_sql_query(query, self.cnxn, params=(subscriber_id,))  # noqa: E501
            # Check if any email is retrieved
            if not email_data.empty:
                return email_data['email'][0]
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# ____________________________________________________________________________

    def update_subscriber_data(
            self,
            subscriber_id: int,
            name: Optional[str] = None,
            email: Optional[str] = None,
            age: Optional[int] = None,
            location: Optional[str] = None,
            gender: Optional[str] = None,
            subscription_ended: Optional[bool] = None,
            event_observed: Optional[int] = None,
            email_sent: Optional[bool] = False
            ):

        """
        Update subscriber information in the database.

        Args:
            subscriber_id (int): ID of the subscriber to update.
            name (str, optional): New name of the subscriber.
            email (str, optional): New email of the subscriber.
            age (int, optional): New age of the subscriber.
            location (str, optional): New location of the subscriber.
            gender (str, optional): New gender of the subscriber.
            subscription_ended (bool, optional): Flag indicating
            if subscription has ended.
            event_observed (int, optional): Event observed status.
            email_sent (bool, optional): Flag indicating if email
            has been sent.

        Raises:
            Any exceptions related to SQL query execution
            or database connection.
        """
        query = """
            SELECT s.subscription_start_date
            FROM rfm_segmentation r
            INNER JOIN subscriber s ON r.subscriber_id = s.subscriber_id
            WHERE r.subscriber_id = ?
            LIMIT 1
        """

        try:
            start_date = pd.read_sql_query(query, self.cnxn, params=(subscriber_id,))  # noqa: E501

            set_clauses = []

            if name is not None:
                set_clauses.append(f"name = '{name}'")
            if email is not None:
                set_clauses.append(f"email = '{email}'")
            if age is not None:
                set_clauses.append(f"age = {age}")
            if location is not None:
                set_clauses.append(f"location = '{location}'")
            if gender is not None:
                set_clauses.append(f"gender = '{gender}'")
            if subscription_ended:
                current_time = datetime.now()
                set_clauses.append(f"subscription_end_date = '{current_time}'")
                duration = current_time - start_date
                set_clauses.append(f"survival_time = {duration.days}")
            if event_observed is not None:
                set_clauses.append(f"event_observed = {event_observed}")
            if email_sent:
                current_time = datetime.now()
                set_clauses.append(f"email_sent = '{current_time}'")

            set_clause = ", ".join(set_clauses)

            condition = f"subscriber_id = {subscriber_id}"

            self.update_table(set_clause, condition)

        except Exception as e:
            print(f"Error: {e}")
            return None
