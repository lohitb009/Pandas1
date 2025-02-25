import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
    products_df = products[
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    ]
    
    return products_df[['product_id']]