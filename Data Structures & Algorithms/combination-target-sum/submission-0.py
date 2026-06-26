class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        combo = []
        def dfs(i, curSum):

            if i >= len(nums):
                return

            if curSum > target:
                return

            if curSum == target:
                res.append(combo.copy())
                return
            
            # Try with that number again
            combo.append(nums[i])
            curSum += nums[i]
            dfs(i, curSum)

            combo.pop()
            curSum -= nums[i]
            dfs(i + 1, curSum)

        dfs(0, 0)
        
        return res
            




        