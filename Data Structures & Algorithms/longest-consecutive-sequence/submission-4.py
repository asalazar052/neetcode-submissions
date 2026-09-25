class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        isInSet = set()
        # Load the set
        for n in nums:
            isInSet.add(n)

        for n in nums:
            if n - 1 not in isInSet:
                curSeq = 1
                while n + curSeq in isInSet:
                    curSeq += 1
                
                longest = max(longest, curSeq)

        return longest