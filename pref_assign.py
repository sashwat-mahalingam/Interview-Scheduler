from interview_classes import InterviewSlot, Interviewee
import pandas as pd

def assign(data, N, K):
    """
    Given a dataframe, returns a list of interview slots' preferences
    and list of interviewee's preferences, prepped for stable matching
    """
    InterviewSlot.N = Interviewee.N = N
    Interviewee.K = InterviewSlot.K = K

    slots = [None] * N
    candidates = [None] * N

    for i in range(N):
        slots[i] = InterviewSlot()
        candidates[i] = Interviewee(data.loc[i, :])
        
    for i in range(N):
        candidates[i].consolidate_prefs()
        candidates[i].notify(slots, i)
    
    for i in range(N):
        slots[i].consolidate_prefs()
    
    return slots, candidates