import postprocessor, preprocessor

"""Run the main program to process, assign, match, and post-process our inputs.
"""

def final_func(pref_input, output_file, match_func):
    """
    HOF that can run on any given match function.
    """
    preferences, N, K = preprocessor.parse_csv(pref_input)

    # match with whichever supplied matcher
    matchings = match_func(preferences, N, K)
    postprocessor.post_process(matchings, output_file)

    return matchings