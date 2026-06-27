class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res = []
        combos = []
        def dfs(i, curSum):
            
            if curSum == target:
                res.append(combos.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                if curSum + candidates[j] > target:
                    break

                combos.append(candidates[j])
                dfs(j + 1, curSum + candidates[j])
                combos.pop()


        dfs(0, 0)
        return res

    '''
    We can include 2 twice in a combo if it is in candidates twice.

    '''