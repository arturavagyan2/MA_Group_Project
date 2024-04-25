import os
import sqlite3
import logging
import numpy as np
import pandas as pd

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
            table_name (str): The name of the table in the database to interact with.
        """

        self.cnxn = sqlite3.connect(f'{dbname}.db')
        self.cursor = self.cnxn.cursor()
        self.dbname = dbname
        self.table_name = table_name
#______________________________________________________________________________________________
        
    def close_cnxn(self) -> None:
        """
        Closes the database connection.

        This method should be called when finished with database operations.
        """
        logger.info('Committing the changes')
        self.cursor.close()
        self.cnxn.close()
        logger.info('The connection has been closed')
#______________________________________________________________________________________________
    
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
#______________________________________________________________________________________________
    
    def truncate_table(self) -> None:
        """
        Drops the table if it exists.

        This method deletes all data and structure from the table.
        """
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        self.cursor.execute(query)
        logger.info(f'The {self.table_name} table is truncated')
        self.cnxn.commit()
#______________________________________________________________________________________________
    
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
        logger.info(f'The shape of the table which is going to be imported {data_to_insert.shape}')
        
        if len(columns) > 1:
            cols, params = ', '.join(columns), ', '.join(ncolumns)
        else:
            cols, params = columns[0], ncolumns[0]
        
        logger.info(f'Insert structure: colnames: {cols} params: {params}')
        logger.info(values[0])
        query = f"""INSERT INTO {self.table_name} ({cols}) VALUES ({params});"""
        logger.info(f'QUERY: {query}')

        self.cursor.executemany(query, values)
        self.cnxn.commit()
        logger.warning('The data is loaded')
#______________________________________________________________________________________________
    
    def update_table(self, set_clause: str, condition: str) -> None:
        """
        Update rows in the table based on a condition.
        
        Parameters:
        - set_clause: A string that specifies the column values to be updated, e.g., "name = 'John', age = 30"
        - condition: A string that defines the condition for the rows to be updated, e.g., "subscriber_id = 1"
        """
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
        self.cursor.execute(query)
        self.cnxn.commit()
        logger.info(f"Updated rows in '{self.table_name}' where {condition}.")
#______________________________________________________________________________________________
      
    def get_table_data(self, columns: list = None, condition: str = None) -> pd.DataFrame:
        """
        Retrieve data from the table based on the specified columns and optional condition.

        Parameters:
            columns (list): A list of column names to retrieve. If not specified, all columns will be retrieved.
            condition (str): An optional SQL condition to filter the data (e.g., "column_name = 'value'"). If not specified, all data will be retrieved.

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
   
