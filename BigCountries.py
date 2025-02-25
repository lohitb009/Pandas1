import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    # world is a dataframe
    # <class 'pandas.core.frame.DataFrame'>
    
    # this will return the object (world['area'] >= 3000000) | (world['population'] >= 25000000)
    # <class 'pandas.core.series.Series'>
    
    world_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # return the columns required for the dataframe
    return world_df[['name', 'population', 'area']]