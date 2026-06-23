class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)


        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        
        return -maxHeap[0]