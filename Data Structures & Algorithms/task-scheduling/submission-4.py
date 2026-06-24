class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Set up
        time = 0
        res = 0
        freqs = {} # Task : Frequency
        for t in tasks:
            freqs[t] = freqs.get(t, 0) + 1
        
        maxHeap = list(freqs.values())
        maxHeap = [-x for x in maxHeap]
        heapq.heapify(maxHeap)
        q = deque() # Initialize with first task since it processes no matter what

        while maxHeap or q:

            # Enqueue the task if it exists still
            if maxHeap:
                curTask = (-heapq.heappop(maxHeap)) - 1
                if curTask > 0:
                    q.append([curTask, time + n])
            
            # Process the task if it's valid
            if q and time >= q[0][1]:
                heapq.heappush(maxHeap, -(q[0][0]))
                q.popleft()

            time += 1
        
        return time


        




'''
[-2,-2]

[]

'''