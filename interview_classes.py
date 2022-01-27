import pandas as pd
# Note: everything is 0-indexed!

class InterviewSlot:
    """
    Class to track an interview slot and its preferences.
    """
    N = 0
    K = 0

    def __init__(self):
        self.preferences = [None] * (InterviewSlot.N + 1)
        self.proposals = []
        self.current_match = None
    
    def note_candidate(self, cand_id, ranking):
        """
        Note candidate by how they rank you.
        """
        if not self.preferences[ranking]:
            self.preferences[ranking] = []
        self.preferences[ranking].append(cand_id)
    
    def consolidate_prefs(self):
        """
        Consolidate prefs into a final list, then map.
        """
        self.final_prefs = []
        self.pref_mappings = [None] * InterviewSlot.N

        for cand_lst in self.preferences:
            self.final_prefs.extend(cand_lst) if cand_lst else None
        
        for i in range(InterviewSlot.N):
            self.pref_mappings[self.final_prefs[i]] = i

    def receive_offer(self, cand_id):
        """
        Receive an offer from a candidate.
        """
        self.proposals.append(cand_id)
        if not self.current_match:
            self.current_match = cand_id
        elif self.pref_mappings[cand_id] < self.pref_mappings[self.current_match]:
            self.current_match = cand_id

class Interviewee:
    """
    Class to track an interviewee and their preferences.
    """
    N = 0
    K = 0

    def __init__(self, cand_series):
        """
        Read in the series of preferences for that candidate into a list.
        """
        self.unassigned_prefs = set(range(Interviewee.N))
        self.final_prefs = [x[1] for x in cand_series.iteritems()]

        for elem in self.final_prefs:
            self.unassigned_prefs.remove(elem)
    
    def consolidate_prefs(self):
        """
        Assign whatever (N - K) de-preferred slots remain using an approximation of nearby slot 'goodness', then map
        """
        for elem in self.unassigned_prefs:
            self.final_prefs.append(elem)

        self.pref_queue = list(self.final_prefs)
        self.pref_queue.reverse()
    
    def notify(self, slots, id):
        """
        Update the interview slots with this candidate's information.
        """
        for i in range(Interviewee.N):
            slots[self.final_prefs[i]].note_candidate(id, i + 1)
    
    def propose(self):
        """
        Propose to the highest-ranked, available candidate.
        """
        return self.pref_queue.pop()