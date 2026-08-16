class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def merge_helper(arr1, arr2):
            start = arr1[0]
            finish = max(arr1[1], arr2[1])
            return [start, finish]


        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if res[-1][1] >= intervals[i][0]:
                res[-1] = merge_helper(res[-1], intervals[i])
            else:
                res.append(intervals[i])
            

        return res



'''
Time: O(nlogn) <- Sorting
Space: O(n) for the output, otherwise O(1)

[[1, 3], [1, 5], [6, 7]]

res = [1, 2]
intervals[i] = [2, 3]





[1, 5]

if intervals[i][0] >= res[-1][0]:
    res[-1] = merge_helper(res[-1], intervals[i])
else:
    res.append(intervals[i])
            

'''