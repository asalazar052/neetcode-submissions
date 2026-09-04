class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        tracker = set()

        while r < len(s):

            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
    
            tracker.add(s[r])
            maxLen = max((r - l) + 1, maxLen)
            r += 1
        
        return maxLen

'''
Time: O(n)
Space: O(n) due to set

zxyyzxyz

'''

