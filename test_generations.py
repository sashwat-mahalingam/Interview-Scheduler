import pandas as pd, random, optimality

"""
Generations of some of the deterministic tests.
"""

def make_tests():
    gen_small()
    gen_medium()
    gen_large()

def gen(N, K, csv_filename):
    """Generate any test."""
    preferences = [random.sample(range(N), K) for _ in range(N)]
    pd.DataFrame(preferences).to_csv('tests/' + csv_filename + '.csv', index=None, header=None)

    optimal_val = optimality.find_global_optima(preferences)
    optimals = pd.read_csv('tests/optimals.csv')

    optimals.loc[optimals.shape[0]] = ([csv_filename,optimal_val])

    optimals.to_csv('tests/optimals.csv', index=None)

def gen_small():
    """Generate small test"""
    N = random.randint(50, 100)
    K = random.randint(30, N)
    gen(N, K, 'small_determ')

def gen_medium():
    """Generate medium test"""
    N = random.randint(100, 500)
    K = random.randint(100, N)
    gen(N, K, 'medium_determ')

def gen_large():
    """Generate large test"""
    N = random.randint(1000, 5000)
    K = random.randint(750, N)
    gen(N, K, 'large_determ')    

make_tests()