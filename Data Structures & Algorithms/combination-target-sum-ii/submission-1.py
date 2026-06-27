class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res = []
        combos = []
        def dfs(i, curSum):

            if curSum == target:
                res.append(combos.copy())
                return

            if i >= len(candidates) or curSum > target:
                return
            
            # Choose to include it
            combos.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            # Choose not to include it
            combos.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSum)
        
        dfs(0, 0)
        return res

    '''
    We can include 2 twice in a combo if it is in candidates twice.

    '''