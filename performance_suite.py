import slot_matcher, random, unittest, pandas as pd, time, optimality

"""
Measure optimality and performance.
"""

class OptimalityTest(unittest.TestCase):
    """
    General class for a deterministic test. 
    """
    def __init__(self, matcher, matcher_name, filename):
        self.matcher = matcher
        self.matcher_name = matcher_name
        self.filename = filename

    def runTest(self):
        matchings = slot_matcher.final_func('tests/' + self.filename + '.csv', None, self.matcher)
        optimal_val = pd.read_csv('tests/optimals.csv')

unittest.main()

