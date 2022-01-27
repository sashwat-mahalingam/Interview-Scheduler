import pref_assign, interview_classes, stable_matcher, pandas as pd

df = pd.read_excel('test_file.xlsx', header=None)
slots, candidates = pref_assign.assign(df, df.shape[0], df.shape[1])

slot_prefs = pd.DataFrame([slot.final_prefs for slot in slots])
candidate_prefs = pd.DataFrame([candidate.final_prefs for candidate in candidates])

w = pd.ExcelWriter('slot_prefs.xlsx')
slot_prefs.to_excel(w)
w.close()

w = pd.ExcelWriter('candidate_prefs.xlsx')
candidate_prefs.to_excel(w)
w.close()

results = stable_matcher.stable_matcher(slots, candidates, df.shape[0])
w = pd.ExcelWriter('schedule.xlsx')

pd.DataFrame(results).to_excel(w)
w.close()