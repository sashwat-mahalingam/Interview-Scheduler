import pandas as pd, random
import itertools

"""
Generations of some of the deterministic tests.
"""

def gen(N, K, filename):
    """Generate any test."""
    preferences = [random.sample(range(N), K) for _ in range(N)]
    pd.DataFrame(preferences).to_excel(filename, index=None, header=None)
    

def gen_small():
    """Generate small test"""
    N = random.randint(5, 20)
    K = random.randint(3, N)
    gen(N, K, 'tests/small_determ.csv')

def gen_medium():
    """Generate medium test"""
    N = random.randint(500, 1000)
    K = random.randint(20, N)
    gen(N, K, 'tests/medium_determ.csv')

    
