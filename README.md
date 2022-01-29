# Slot Matcher

## Overview
Given a set of `N` slots and a set of `N` agents, each agent has `K <= N` ordered preferences of the slots. `K` is fixed for all agents. The goal is to assign agents to slots such that the average preference level of each agent's assignment is maximized (i.e. on average, an agent is assigned as high a preference as possible). The various approaches to this problem and their results have been summarized below.

## Development
The program was implemented in Python, and the core libraries used in this implementation are Pandas for the data processing and output.

## Metric and Test Cases:

## Approach 1: Semi-Arbitrary Stable Matching Algorithm

One possible approximation to obtain the best "average level" of matching is stability. That is, given a matching, no agent can hope to swap with another agent such that at least one is better off and neither is worse off. To implement this, I used Gale-Shapley's algorithm. The algorithm is semi-arbitrary because each agent has to give an ordering of all `N` slots for Gale-Shapley to work, so the remaining `N - K` preferences per agent were assigned randomly. 

### Results:
Runtime Complexity: `O(N²)`
Space Complexity: `Θ(N²)`

## Approach 2a: Local Search - Hill-Climbing

## Approach 2b: Local Search - Simulated Annealing

