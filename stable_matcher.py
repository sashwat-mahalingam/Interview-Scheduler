import interview_classes

def stable_matcher(slots, candidates, N):
    """
    Input: slots with their preferences and candidates with their preferences. Matches to be interviewee-optimal using Gale-Shapley algorithm.
    """
    proposals_queue = list(range(N))
    slots_queue = set()

    while proposals_queue:
        # proposal stage
        for cand_id in proposals_queue:
            slot = candidates[cand_id].propose()
            slots[slot].receive_offer(cand_id)
            slots_queue.add(slot)
        
        proposals_queue = []
        
        # rejection/maybe stage
        for s in slots_queue:
            slot = slots[s]

            for candidate in slot.proposals:
                if slot.current_match != candidate:
                    proposals_queue.append(candidate)
            slot.proposals = [slot.current_match]
        
        slots_queue = set()
    
    final_ans = [None] * N

    for i in range(N):
        final_ans[i] = [i, slots[i].current_match]
    
    return final_ans