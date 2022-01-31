import stable_match, postprocessor, preprocessor

"""Run the main program to process, assign, match, and post-process our inputs.
"""

def final_func(pref_input, output_file):
    # Preprocess
    preferences, N, K = preprocessor.parse_csv(pref_input)

    # Assign and make slot objects
    slots, agents = stable_match.assign(preferences, N, K)

    # Stable match
    matchings = stable_match.stable_matcher(slots, agents, N)

    # Post process
    postprocessor.post_process(matchings, output_file)
