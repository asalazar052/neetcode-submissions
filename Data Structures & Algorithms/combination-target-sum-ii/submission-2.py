class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        combos = []
        candidates.sort()

        def dfs(i, curSum):

            if curSum == target:
                res.append(combos[:])
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            # Include current val
            combos.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            combos.pop()
            # Don't include current value and skip over all of the same type to avoid duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curSum)
        

        dfs(0, 0)
        return res

