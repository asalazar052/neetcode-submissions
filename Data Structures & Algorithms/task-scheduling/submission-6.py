class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Setup
        time = 0
        freqs = {}
        
        for t in tasks:
            freqs[t] = 1 + freqs.get(t, 0)
        
        maxHeap = list(freqs.values())
        maxHeap = [-x for x in maxHeap]
        heapq.heapify(maxHeap)

        # Used to keep track of when a non-zero task can be run again
        q = deque()
        while maxHeap or q:

            time += 1

            if maxHeap:
                curTask = (-heapq.heappop(maxHeap)) - 1

                # Enqueue the task if it's still nonzero
                if curTask > 0:
                    q.append([curTask, time + n])
            
            if q and q[0][1] <= time:
                task = q.popleft()
                heapq.heappush(maxHeap, -task[0])
        
        return time

'''

h = 1,1

q = 3

1


'''





        