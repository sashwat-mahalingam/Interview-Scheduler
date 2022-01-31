import pref_assign, slot_indiv_classes, stable_matcher, postprocessor, preprocessor

"""Run the main program to process, assign, match, and post-process our inputs.
"""

# Preprocess
preferences, N, K = preprocessor.parse_csv()

# Assign and make interview objects
slots, candidates = pref_assign.assign(preferences, N, K)

# Stable match
matchings = stable_matcher.stable_matcher(slots, candidates, N)

# Post process
postprocessor.post_process(matchings)

