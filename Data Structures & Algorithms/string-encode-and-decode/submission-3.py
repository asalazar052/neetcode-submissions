class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            for c in s:
                encoded += c
        
        print(encoded)
            
        return encoded

    def decode(self, s: str) -> List[str]:

        ptr = 0
        res = []

        while ptr < len(s):
            num = ""
            while s[ptr] != "#":
                num += str(s[ptr])
                ptr += 1
            
            num = int(num)
            
            
            cur = ""
            for i in range(num):
                cur += s[ptr + i + 1]
            
            res.append(cur)
            ptr += num + 1
            
            
        
        return res


'''
2we3say1:3yes10!@#$%^&*()

'''


