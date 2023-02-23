from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    waiting = deque(truck_weights)
    bridgeWeight = 0
    time = 0
    
    while len(waiting) or bridgeWeight > 0:
        removed = bridge.popleft()
        bridgeWeight -= removed
        
        if len(waiting) and bridgeWeight + waiting[0] <= weight :
            new_truck = waiting.popleft()
            bridge.append(new_truck)
            bridgeWeight += new_truck
        else:
            bridge.append(0)
        time += 1
        
    return time
    