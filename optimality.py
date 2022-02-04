import itertools

"""
Utilities for optimality testing and generation for optimal matchings.
"""

def optimality_metric(matching, preferences):
    """
    Finding the optimality of this matching.
    """
    N = len(preferences)
    agent_prefs = [None] * len(preferences)
    K = len(preferences[0])
    avg_pref = 0

    for i in range(N):
        agent_prefs[i] = {preferences[i][j] : j for j in range(K)}
    
    for slot in range(N):
        agent = matching[slot]
        avg_pref += agent_prefs[agent][slot] if slot in agent_prefs[agent] else (K + 1)
    
    return avg_pref / N

def find_global_optima(preferences):
    """
    Find the best matching per the metric. Runs in O(N!) time.
    """
    N = len(preferences)
    base_matching = list(range(N))
    K = len(preferences[0])

    optimal_val = N * (K + 1)

    for matching in itertools.combinations(base_matching, N):
        optimal_val = min(optimal_val, optimality_metric(matching, preferences))
    
    return optimal_val
