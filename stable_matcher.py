import pandas

class InterviewAssigner:
    N = 0

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
        if self.preferences[ranking]:
            self.preferences[ranking] = [None] * N
        self.preferences[ranking].append(cand_id)
    
    def consolidate_prefs(self):
        """
        Consolidate prefs into a final list. Kind of counting sort.
        """
        self.final_prefs = [None] * InterviewAssigner.N

        for key in sorted(self.preferences.keys()):
            self.final_prefs.extend(self.preferences[key])
    
