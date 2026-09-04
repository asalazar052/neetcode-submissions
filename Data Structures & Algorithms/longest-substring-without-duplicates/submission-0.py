class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        tracker = set()

        while r < len(s):

            if s[r] not in tracker:
                tracker.add(s[r])
            else:
                while s[l] != s[r]:
                    tracker.remove(s[l])
                    l += 1
                l += 1

            maxLen = max((r - l) + 1, maxLen)

            r += 1
        
        return maxLen

'''
zxyyzxyz

'''

