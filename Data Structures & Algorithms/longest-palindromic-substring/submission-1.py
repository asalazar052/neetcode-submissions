class Solution:
    def longestPalindrome(self, s: str) -> str:

        resIdx = l=0
        maxLength = 0 
        for i in range(len(s)):
            # odd length
            l, r  = i, i # Both ptrs start at current index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    resIdx = l
                    maxLength = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    resIdx = l
                    maxLength = r - l + 1
                l -= 1
                r += 1
            
        return s[resIdx : resIdx + maxLength]



    '''
    abacbd
      ^


    '''