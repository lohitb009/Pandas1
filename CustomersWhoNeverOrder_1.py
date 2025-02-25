import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # using not clause i.e. (~)
    customer_df = customers[~(customers['id']).isin(orders['customerId'])]

    return customer_df[['name']].rename(columns = {'name':'Customers'})