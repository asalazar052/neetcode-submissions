class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Set up
        time = 0
        freqs = Counter(tasks)
        
        maxHeap = list(freqs.values())
        maxHeap = [-x for x in maxHeap]
        heapq.heapify(maxHeap)

        q = deque() # Initialize with first task since it processes no matter what

        while maxHeap or q:

            time += 1

            if maxHeap:
                curTask = 1 + heapq.heappop(maxHeap)
                if curTask:
                    q.append([curTask, time + n])
            
            if q and q[0][1] == time:
                curTask = q.popleft()[0]
                heapq.heappush(maxHeap, curTask)

        
        return time


        




'''
[-2,-2]

[]

'''