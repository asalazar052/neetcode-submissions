class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output



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