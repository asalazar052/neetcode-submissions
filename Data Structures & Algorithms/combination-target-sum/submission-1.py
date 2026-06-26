class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        combo = []
        nums.sort()

        def dfs(i, curSum):
            print(curSum)

            if curSum == target:
                res.append(combo.copy())
                return
            
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum > target:
                    return
                combo.append(nums[j])
                dfs(j, curSum)
                curSum -= nums[j]
                combo.pop()

        dfs(0, 0)
        
        return res
            




        