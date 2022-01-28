import pandas as pd

def post_process(slot_candidate_list, cand_series, slots_df):
    """
    Convert our slots back into timings and our candidate indices back into their IDs. Output the CSV.
    """

    assignments = pd.DataFrame(slot_candidate_list)
    assignments.columns = ['cand_ind']

    assignments = pd.concat(slots_df, assignments, axis = 1)
    
    assignments['cand_id'] = assignments['cand_id'].apply(lambda id: cand_series[id])

    assignments.to_csv('schedule.csv')




