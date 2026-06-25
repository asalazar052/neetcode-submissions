class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i): # i is the idx of the num we are choosing to include or not to include
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # don't include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

