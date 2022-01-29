import pandas as pd

def post_process(slot_indiv_list, indiv_series, slots_df):
    """
    Convert our slots back into timings and our candidate indices back into their IDs. Output the CSV.
    """

    assignments = pd.DataFrame(slot_indiv_list)
    assignments.columns = ['indiv_ind']

    assignments = pd.concat([slots_df, assignments], axis = 1)
    
    assignments['indiv_ind'] = assignments['indiv_ind'].apply(lambda id: indiv_series[id])

    assignments.to_csv('schedule.csv', header=None, index=None)




