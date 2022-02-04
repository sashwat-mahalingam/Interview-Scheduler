from slot_agent_classes import Slot, Agent

def assign(data, N, K):
    """
    Given a dataframe, returns a list of slots' preferences
    and list of agent's preferences, prepped for stable matching
    """
    Slot.N = Agent.N = N
    Agent.K = Slot.K = K

    slots = [None] * N
    agents = [None] * N

    for i in range(N):
        slots[i] = Slot()
        agents[i] = Agent(data.loc[i, :])
        
    for i in range(N):
        agents[i].consolidate_prefs()
        agents[i].notify(slots, i)
    
    for i in range(N):
        slots[i].consolidate_prefs()
    
    return slots, agents

def stable_matcher(slots, agents, N):
    """
    Input: slots with their preferences and agents with their preferences. Matches to be agent-optimal using Gale-Shapley algorithm.
    """
    proposals_queue = list(range(N))
    slots_queue = set()

    while proposals_queue:
        # proposal stage
        for agent_id in proposals_queue:
            slot = agents[agent_id].propose()
            slots[slot].receive_offer(agent_id)
            slots_queue.add(slot)
        
        proposals_queue = []
        
        # rejection/maybe stage
        for s in slots_queue:
            slot = slots[s]

            for agent in slot.proposals:
                if slot.current_match != agent:
                    proposals_queue.append(agent)
            slot.proposals = [slot.current_match]
        
        slots_queue = set()
    
    final_ans = [None] * N

    for i in range(N):
        final_ans[i] = slots[i].current_match
    
    return final_ans, agents

def match(data, N, K):
    slots, agents = assign(data, N, K)
    return stable_matcher(slots, agents, N)