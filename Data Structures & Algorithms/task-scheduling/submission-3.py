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

            time += 1

            # Enqueue the task if it exists still
            if maxHeap:
                curTask = (-heapq.heappop(maxHeap)) - 1
                if curTask:
                    q.append([curTask, time + n])
            
            # Process the task if it's valid
            if q and q[0][1] <= time:
                curTask = q.popleft()[0]
                heapq.heappush(maxHeap, -curTask)
                

            
        
        return time


        




'''
[-2,-2]

[]

'''