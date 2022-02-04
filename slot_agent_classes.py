# Note: everything is 0-indexed!

class Slot:
    """
    Class to track a slot and its preferences.
    """
    N = 0
    K = 0

    def __init__(self):
        self.preferences = [None] * (Slot.N + 1)
        self.proposals = []
        self.current_match = None
    
    def note_candidate(self, cand_id, ranking):
        """
        Note agent by how they rank you.
        """
        if not self.preferences[ranking]:
            self.preferences[ranking] = []
        self.preferences[ranking].append(cand_id)
    
    def consolidate_prefs(self):
        """
        Consolidate prefs into a final list, then map.
        """
        self.final_prefs = []
        self.pref_mappings = [None] * Slot.N

        for cand_lst in self.preferences:
            self.final_prefs.extend(cand_lst) if cand_lst else None
        
        for i in range(Slot.N):
            self.pref_mappings[self.final_prefs[i]] = i

    def receive_offer(self, cand_id):
        """
        Receive an offer from an agent.
        """
        self.proposals.append(cand_id)
        if not self.current_match:
            self.current_match = cand_id
        elif self.pref_mappings[cand_id] < self.pref_mappings[self.current_match]:
            self.current_match = cand_id

class Agent:
    """
    Class to track an agent and their preferences.
    """
    N = 0
    K = 0

    def __init__(self, cand_series):
        """
        Read in the series of preferences for that agent into a list.
        """
        self.unassigned_prefs = set(range(Agent.N))
        self.final_prefs = [x[1] for x in cand_series.iteritems()]

        for elem in self.final_prefs:
            self.unassigned_prefs.remove(elem)
    
    def consolidate_prefs(self):
        """
        Assign whatever (N - K) de-preferred slots remain using an approximation of nearby slot 'goodness', then map
        """
        for elem in self.unassigned_prefs:
            self.final_prefs.append(elem)
        
        self.pref_mappings = [None] * Agent.N
        
        for i in range(Agent.N):
            self.pref_mappings[self.final_prefs[i]] = i

        self.pref_queue = list(self.final_prefs)
        self.pref_queue.reverse()
    
    def notify(self, slots, id):
        """
        Update the slots with this agent's information.
        """
        for i in range(Agent.N):
            slots[self.final_prefs[i]].note_candidate(id, i + 1)
    
    def propose(self):
        """
        Propose to the highest-ranked, available slot.
        """
        return self.pref_queue.pop()

