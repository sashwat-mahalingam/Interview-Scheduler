import pandas as pd

def parse_csv():
    """
    Reads in CSV inputs and returns all dataframes and dimensions
    """
    # Read in data
    slots_df = pd.read_csv('slots.csv', header=None)
    pref_df = pd.read_csv('preferences.csv', header=None)

    K = pref_df.shape[1] - 1
    N = slots_df.shape[0]

    # Label columns and map the indices for use in post-processing
    slots_df.columns = ['start_time', 'end_time']
    pref_df.columns = ['cand_id'] + [str(i) + 'pref' for i in range(1, K + 1)]

    slots_df.sort_values(by = 'start_time')

    time_id_map = {slots_df.loc[i, 'start_time'] : i for i in range(N)}
    # Map timings in pref_df to their indices

    pref_df.iloc[:, 1:] = pref_df.iloc[:, 1:].applymap(lambda time: time_id_map[time])

    return slots_df, pref_df, N, K