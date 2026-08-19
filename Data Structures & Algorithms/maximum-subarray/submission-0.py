class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        curSum = 0
        for n in nums:
            
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(curSum, res)
        
        return res


'''
[2,-3,4,-2,2,1,-1,4]
    ^

'''