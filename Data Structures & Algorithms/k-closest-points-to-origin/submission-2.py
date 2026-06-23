class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        for i in range(len(points)):

            dist = -(math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2)))
            heapq.heappush(maxHeap, [dist, points[i][0], points[i][1]])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)     
        

        res = []
        while k > 0:
            temp = heapq.heappop(maxHeap)
            res.append([temp[1], temp[2]])
            k -= 1
        
        return res


'''
Immediate solution is to 
1. iterate through points
2. Calculate dist from the origin
3. Return the ones with the smallest distance

what happens wehn two points have the same dist?

O(n) to calculate all dists from the origin
O(logn) to heapify list of dists

Ultimately O(n + klogn)

'''
        