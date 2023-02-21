import heapq 

def solution(operations):
    minheap = []
    maxheap = []
    for operation in operations:
        if operation == 'D -1':
            if len(minheap) == 0:
                continue
            heapq.heappop(minheap)
            temp = []
            for value in minheap:
                heapq.heappush(temp, -value)
            maxheap = temp
            
            
        elif operation == 'D 1':
            if len(maxheap) == 0:
                continue
                
            heapq.heappop(maxheap)
            temp = []
            for value in maxheap:
                heapq.heappush(temp, -value)
            minheap = temp
            
        else:
            num = int(operation.split()[1])
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
            
    if len(minheap) == 0:
        return [0,0]
    
    else:
        return[-heapq.heappop(maxheap), heapq.heappop(minheap)]