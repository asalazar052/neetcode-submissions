class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partition = []

        def isPalindrome(test):
            l, r = 0, len(test) - 1

            while l <= r:

                if test[l] != test[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True


        def helper(i):

            if i >= len(s):
                res.append(partition[:])
                return
            
            for j in range(i + 1, len(s) + 1):
                
                p = s[i : j]
                if isPalindrome(p):
                    partition.append(p)
                    helper(j)
                    partition.remove(p)

        helper(0)

        return res

'''

helper(3)
helper(2)
helper(1)
helper(0)

part = [a, a, b]
'''
