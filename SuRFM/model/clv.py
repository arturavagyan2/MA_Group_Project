import pandas as pd
from .data_processing import MM, p

class CLV:
    def __init__(self, customer_data, customer_id, t):
        """
        Initialize the CLV calculator with the specified customer data, customer ID, and time 't'.
        
        Parameters:
        -----------
        customer_data : DataFrame
            A DataFrame containing customer transaction data.
        customer_id : int
            Identifier for the customer, for which the CLV is calculated.
        t : int
            Time for which CLV is calculated.
        """
        self.customer_data = customer_data
        self.customer_id = customer_id
        self.t = t

    def calculate_rfm(self):
        """
        Calculate the Recency, Frequency, and Monetary values for the customer.
        
        Returns:
        --------
        tuple:
            A tuple containing Recency, Frequency, and Monetary values.
        """
        data = self.customer_data[self.customer_data['customer_id'] == self.customer_id]
        
        recency = (pd.to_datetime('today') - data['date'].max()).days
        
        frequency = data.shape[0]

        monetary = data['amount'].sum()
        
        return recency, frequency, monetary

    def calculate_clv(self):
        """
        Calculate the Customer Lifetime Value (CLV) using RFM and survival probabilities.
        
        Returns:
        --------
        float:
            The calculated Customer Lifetime Value (CLV) rounded to three decimal places.
        """
        recency, frequency, monetary = self.calculate_rfm()

        base_discount_rate = 0.1
        
        discount_adjustment = min(0.05, recency / 30 * 0.01)
        discount_rate = max(0, base_discount_rate - discount_adjustment)

        monthly_margin = MM() * monetary
        customer_probabilities = p()

        probabilities_list = customer_probabilities.loc[1:self.t, self.customer_id].values.tolist()

        probabilities_list = [p * min(1, frequency / 10) for p in probabilities_list]

        clv = 0
        for i in range(len(probabilities_list)):
            clv += (probabilities_list[i] / ((1 + discount_rate / 12) ** i))

        clv *= monthly_margin
        clv = round(clv, 3)

        return clv
