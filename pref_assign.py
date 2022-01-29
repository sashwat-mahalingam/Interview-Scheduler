from slot_indiv_classes import Slot, Individual
import pandas as pd

def assign(data, N, K):
    """
    Given a dataframe, returns a list of interview slots' preferences
    and list of interviewee's preferences, prepped for stable matching
    """
    Slot.N = Individual.N = N
    Individual.K = Slot.K = K

    slots = [None] * N
    individuals = [None] * N

    for i in range(N):
        slots[i] = Slot()
        individuals[i] = Individual(data.loc[i, :])
        
    for i in range(N):
        individuals[i].consolidate_prefs()
        individuals[i].notify(slots, i)
    
    for i in range(N):
        slots[i].consolidate_prefs()
    
    return slots, individuals