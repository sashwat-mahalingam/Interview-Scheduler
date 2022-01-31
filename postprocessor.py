import pandas as pd

def post_process(slot_indiv_list):
    """
    Convert our slots back into timings and our candidate indices back into their IDs. Output the CSV.
    """
    
    assignments = pd.DataFrame(slot_indiv_list)
    assignments.to_csv('schedule.csv', header=None)