import pandas as pd

# Note: everything is 0-indexed!

class InterviewAssigner:
    N = 0
    K = 0

    def assign(data, N, K):
        """
        Given a dataframe, returns a list of interview slots' preferences
        and list of interviewee's preferences, prepped for stable matching
        """
        InterviewAssigner.N = N
        InterviewAssigner.K = K

        slots = [None] * N
        candidates = [None] * N

        for i in range(N):
            slots[i] = InterviewSlot()
            candidates[i] = Interviewee(data.loc[i, :])
            
        for i in range(N):
            candidates[i].assign_rem()
            candidates[i].notify(slots, i)
        
        for i in range(N):
            slots[i].consolidate_prefs()
        
        return slots, candidates

class InterviewSlot:
    """
    Class to track an interview slot and its preferences.
    """

    def __init__(self):
        self.preferences = [None] * (InterviewAssigner.N + 1)
    
    def note_candidate(self, cand_id, ranking):
        """
        Note candidate by how they rank you.
        """
        if not self.preferences[ranking]:
            self.preferences[ranking] = []
        self.preferences[ranking].append(cand_id)
    
    def consolidate_prefs(self):
        """
        Consolidate prefs into a final list. Kind of counting sort.
        """
        self.final_prefs = []

        for cand_lst in self.preferences:
            self.final_prefs.extend(cand_lst) if cand_lst else None

class Interviewee:
    """
    Class to track an interviewee and their preferences.
    """

    def __init__(self, cand_series):
        """
        Read in the series of preferences for that candidate into a list.
        """
        self.unassigned_prefs = set(range(InterviewAssigner.N))
        self.final_prefs = [x[1] for x in cand_series.iteritems()]

        for elem in self.final_prefs:
            self.unassigned_prefs.remove(elem)
    
    def assign_rem(self):
        """
        Assign whatever (N - K) de-preferred slots remain using an approximation of nearby slot 'goodness'
        """
        for elem in self.unassigned_prefs:
            self.final_prefs.append(elem)
    
    def notify(self, slots, id):
        """
        Update the interview slots with this candidate's information.
        """

        for i in range(InterviewAssigner.N):
            slots[self.final_prefs[i]].note_candidate(id, i + 1)