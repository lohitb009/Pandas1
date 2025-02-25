import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # using left join -- customer left joined with orders
    customers_df = customers.merge(orders, left_on = 'id', right_on = 'customerId', how = 'left')
    
    # customer_df is dataframe only, print(type(customers_df)) <class 'pandas.core.frame.DataFrame'>
    
    # get <NA> customer_id
    customers_df = customers_df[
        customers_df['customerId'].isna()
    ]

    # print(customers_df)

    return customers_df[['name']].rename(columns = {'name':'Customers'})