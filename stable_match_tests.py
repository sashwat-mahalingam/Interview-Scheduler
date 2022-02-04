import preprocessor, random, unittest, pandas as pd
import typing
import stable_match

"""
To verify the accuracy of the stable matching implementation.
"""


def verify_double_stability(self:unittest.TestCase, match, slots, agents, N):
    """
    Is the matching stable in the double-sided sense?
    """

    for slot_1 in range(N):
        for slot_2 in range(N):
            if slot_1 != slot_2:
                agent_1, agent_2 = slots[slot_1].current_match, slots[slot_2].current_match

                # assert that not both slot-agent pairs would rather swap
                agent1_slot2 = agents[agent_1].pref_mappings[slot_1] > agents[agent_1].pref_mappings[slot_2] 
                agent1_slot2 = agent1_slot2 and slots[slot_2].pref_mappings[agent_1] < slots[slot_2].pref_mappings[agent_2]
                
                agent2_slot1 = agents[agent_2].pref_mappings[slot_2] > agents[agent_1].pref_mappings[slot_1]
                agent2_slot1 = agent2_slot1 and slots[slot_1].pref_mappings[agent_2] < slots[slot_1].pref_mappings[agent_1]

                self.assertFalse(agent1_slot2 and agent2_slot1)

def verify_perfectness(self:unittest.TestCase, match):
    """
    Is there no repeats of agents in matchings? (Perfect matching)
    """
    agents_seen = set()

    for agent in match:
        self.assertFalse(agent in agents_seen)
        agents_seen.add(agent)

def general_framework(input_file, self:unittest.TestCase):
    """
    General framework on a test input.
    """
    
    preferences, N, K = preprocessor.parse_csv(input_file)
    slots, agents = stable_match.assign(preferences, N, K)
    matchings = stable_match.stable_matcher(slots, agents, N)

    verify_perfectness(self, matchings)
    verify_double_stability(self, matchings, slots, agents, N)

class SmallDeterministicTest(unittest.TestCase):
    def runTest(self):
        """
        Test on small inputs.
        """
        general_framework('tests/small_determ.csv', self)

class MediumDeterministicTest(unittest.TestCase):
    def runTest(self):
        """
        Test on medium set of inputs.
        """
        general_framework('tests/medium_determ.csv', self)

class LargeDeterministicTest(unittest.TestCase):
    def runTest(self):
        """
        Test on large set of inputs.
        """
        general_framework('tests/large_determ.csv', self)

if __name__ == "__main__":
    unittest.main()