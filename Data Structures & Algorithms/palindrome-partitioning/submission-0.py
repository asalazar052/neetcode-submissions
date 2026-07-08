class Solution:

    def partition(self, s: str) -> List[List[str]]:

    
        res = []
        path = []

        def isPali(curStr, l, r):
            
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            
            return True

        def helper(i):
            
            if i >= len(s):
                res.append(path.copy())
                return 


            # Check if the path so far is okay
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    path.append(s[i : j + 1])
                    helper(j + 1)
                    path.pop()
        
        helper(0)
        return res

            
    

    



'''
Will for sure split every char into one array


ababacd
^     ^
ababacd     ababacd
^    ^       ^    ^ 


"aba" "b" "a" "c" "d"
"ababa" "cd"
"a" "bab" "a" "c" "d"
"a" "b" "aba" "c" "d"
'''