import pref_assign, slot_indiv_classes, stable_matcher, postprocessor, preprocessor

"""Run the main program to process, assign, match, and post-process our inputs.
"""

# Preprocess
slots_df, pref_df, N, K = preprocessor.parse_csv()
indiv_series, preferences = pref_df.iloc[:, 0], pref_df.iloc[:, 1:]

# Assign and make interview objects
slots, candidates = pref_assign.assign(preferences, N, K)

# Stable match
matchings = stable_matcher.stable_matcher(slots, candidates, N)

# Post process
postprocessor.post_process(matchings, indiv_series, slots_df)

