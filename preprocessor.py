import pandas as pd

def parse_csv():
    """
    Reads in CSV inputs and returns all dataframes and dimensions
    """
    # Read in data
    pref_df = pd.read_csv('preferences.csv', header=None)
    K = pref_df.shape[1]
    N = pref_df.shape[0]

    return pref_df, N, K