
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def left(dig):
            if dig == '0':
                return '9'
            if dig == '1':
                return '0'
            if dig == '2':
                return '1'
            if dig == '3':
                return '2'
            if dig == '4':
                return '3'
            if dig == '5':
                return '4'
            if dig == '6':
                return '5'
            if dig == '7':
                return '6'
            if dig == '8':
                return '7'
            if dig == '9':
                return '8'
        def right(dig):
            if dig == '0':
                return '1'
            if dig == '1':
                return '2'
            if dig == '2':
                return '3'
            if dig == '3':
                return '4'
            if dig == '4':
                return '5'
            if dig == '5':
                return '6'
            if dig == '6':
                return '7'
            if dig == '7':
                return '8'
            if dig == '8':
                return '9'
            if dig == '9':
                return '0'

        terminate = set(deadends)
        visited = set()
        q = deque()
        counter = 0
        canUnlock = False

        if '0000' in deadends:
            return -1

        def checkValidity(code):
            nonlocal canUnlock

            if code == target:
                canUnlock = True
                return

            if code in terminate or code in visited:
                return

            else:
                q.append(code)
                visited.add(code)
        
        def bfs(curCode):
            nonlocal counter

            q.append(curCode)
            visited.add(curCode)
            
            while q and not canUnlock:
                for i in range(len(q)):
                    cur = q.popleft()

                    checkValidity(cur[0:3] + left(cur[3]))
                    checkValidity(cur[0:3] + right(cur[3]))

                    checkValidity(cur[0:2] + left(cur[2]) + cur[3])
                    checkValidity(cur[0:2] + right(cur[2]) + cur[3])

                    checkValidity(cur[0] + left(cur[1]) + cur[2:])
                    checkValidity(cur[0] + right(cur[1]) + cur[2:])

                    checkValidity(left(cur[0]) + cur[1:])
                    checkValidity(right(cur[0]) + cur[1:])
                
                counter += 1
            
            return 
        
        bfs('0000')
        if canUnlock:
            return counter
        else:
            return -1
        

