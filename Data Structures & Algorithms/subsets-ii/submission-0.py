class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        subset = []
        def dfs(i):
            
            # Base case
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Include
            subset.append(nums[i])
            dfs(i + 1)

            # Don't include
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                # ? subset.pop()
            
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res



'''
[1,2,1] -> Should have 8 subsets, but [1,2] = [2,1] and [1] = [1]
            
                
With distinct [1,2,3]
Start with []

                               []                               Start
                [1]                             []              1 Choice
        [1,2]           [1]              [2]         []         2 Choice
    [1,2,2]  [1,2]  [1,3] [1]       [2,3]   [2]    [3] []       3 Choice
    

With repeats [1,1,2]
                                       []
                                [1]                     []                    1 Choice
                         [1,1]           [1]         [2] []                  2nd 1 Choice on the left, skip all the way past 1 on the right for 2 choice
                    [1,1,2]  [1,1]  [1,2]   [1]                         2 choice for left


'''