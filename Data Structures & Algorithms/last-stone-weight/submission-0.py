class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-x for x in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 < stone2:
                heapq.heappush(heap, -(stone2 - stone1))
            elif stone2 < stone1:
                heapq.heappush(heap, -(stone1 - stone2))
            
        if heap:
            return -heap[0]
        else:
            return 0





'''
2 heaps? 

heap1 holds the heaviest stone. We remove that from heap2 and then heap
'''