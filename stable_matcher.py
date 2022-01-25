import pandas

class InterviewSlot:
    """
    Class to track an interview slot and its preferences.
    """

    def __init__(self):
        self.preferences = {}
    
    def note_candidate(self, cand_id, ranking):
        """
        Note candidate by how they rank you.
        """

        if ranking not in self.preferences:
            self.preferences[ranking] = []
        self.preferences[ranking].append(cand_id)
    
    def consolidate_prefs(self):
        """
        Consolidate prefs into a final list. Kind of counting sort.
        """
        self.final_prefs = [None] * InterviewAssigner.N

        for key in sorted(self.preferences.keys()):
            self.final_prefs[]

class InterviewAssigner:

    

    def __init__(self, data, N, K):
        InterviewAssigner
        
