class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        checkedSet = set()
        isInSet = set()
        # Load the set
        for n in nums:
            isInSet.add(n)

        maxSeq = 0
        for n in nums:
            if n not in checkedSet:
                cur = n
                length = 1
                while cur + 1 in isInSet:
                    length += 1
                    cur += 1
                    checkedSet.add(cur)

                maxSeq = max(maxSeq, length)


        return maxSeq