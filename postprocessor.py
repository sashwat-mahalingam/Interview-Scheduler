import pandas as pd

def post_process(slot_agent_list, output_file):
    """
    Convert our slots back into timings and our candidate indices back into their IDs. Output the CSV.
    """
    
    assignments = pd.DataFrame(slot_agent_list)
    assignments.to_csv(output_file, header=None)