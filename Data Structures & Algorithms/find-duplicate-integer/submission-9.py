class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:

            if nums[abs(n) - 1] < 0:
                return abs(n)

            nums[abs(n) - 1] = -1 * nums[abs(n) - 1]
        


'''
[-1,3,-4,2,2]

 




'''