import slot_matcher, random, pandas as pd

rand_mat = pd.DataFrame([random.sample(range(7), 5) for _ in range(7)])
rand_mat.to_csv('tests/pref1.csv',header=None, index=None)

slot_matcher.final_func('tests/pref1.csv', 'tests/schedule1.csv')