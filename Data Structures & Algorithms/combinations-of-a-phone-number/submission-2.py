class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        curS = ""

        mapper = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        combos = set()
        def helper(i):
            nonlocal curS

            if i >= len(digits):
                res.append(curS)
                return
            
            curDigChars = mapper[digits[i]]
            for j in range(len(curDigChars)):
                curS += curDigChars[j]
                helper(i + 1)
                curS = curS[0:i]

        if digits:
            helper(0)

        return res
                

'''
def
^

ghi
 ^

'''

            


