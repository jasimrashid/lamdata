
# TODO: hel[per function
# State abbreviation --> full name and vice versa
# FL -> Florida]    

import pandas as pd

def add_state_names_column(my_df):
    """
    Add a column of correspdonging state names to a dataframe

    params (my_df) a dataframe with a column called "abbrev" that has state abbreviation

    Returns a copy of the original dataframe but with an extra column
    """
    
    new_df = my_df.copy()

    names_map = {"CA": "Cali","CO":"Colo","CT":"Conn"}

    breakpoint()

    return my_df

if __name__ =="__main__":
    df=pd.DataFrame({"abbrev":["CA","CO","CT","CT","DC","TX"]})
    print(df.head())

    add_state_names_column(df)
    print(df.head())