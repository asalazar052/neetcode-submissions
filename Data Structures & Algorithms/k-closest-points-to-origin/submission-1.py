class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dists = {} # dist : index in points
        heap = []
        for i in range(len(points)):

            dist = (math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2)))
            dists[tuple([dist, i])] = points[i]
            heapq.heappush(heap, tuple([dist, i]))
        

        res = []
        while k > 0:
            res.append(dists[heapq.heappop(heap)])
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
        