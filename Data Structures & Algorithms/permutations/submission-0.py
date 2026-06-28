class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
         
        def helper(arr):
            if len(arr) == 0:
                return [[]]
            
            perms = helper(arr[1:])
            res = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, arr[0])
                    res.append(p_copy)

            return res
        
        return helper(nums)

'''
[1,2,3]

How do permutations work?

For n unique integers, the number of unique permutations is n!

3 * 2 * 1

(3 choices) (2 choices) (1 choice)
   1           2           3
   2           1           3 
   3           1           3


'''