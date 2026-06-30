class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def helper(cur, openCount, closedCount):
            print(f"{cur}, {openCount}, {closedCount}")
            if openCount == n and closedCount == n:
                res.append(cur)
                return
            
            if openCount == closedCount:
                cur += "("
                helper(cur, openCount + 1, closedCount)
                cur = cur[:-1]

            elif openCount == n:
                cur += ")"
                helper(cur, openCount, closedCount + 1)
                cur = cur[:-1]

            else:
                cur += "("
                helper(cur, openCount + 1, closedCount)
                cur = cur[:-1]
                cur += ")"  
                helper(cur, openCount, closedCount + 1)
                cur = cur[:-1]
            
            
            
        helper("", 0, 0)
        return res

'''
base case: open count >= n

case where openCount > closedCount:
we can either add an open parenthesis or a closed parenthesis since 

case where closedCount > openCount:

[], open = 0, closed = 0 Must add an open parenthesis
[(] open = 1, closed = 0 Can either add a closed or an open

[()] open = 1, closed = 1 Must add an open
[((] open = 2, closed = 0 Can either add a closed or an open


[(((] open = 3, closed = 0 Must add a closed (since open == n)



'''