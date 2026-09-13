class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        # for n in nums:
        #     vals.add(n)

        # for i in range(len(nums)):
        i = 0
        while i < len(nums):
            
            target = -nums[i]

            #for j in range(i, len(nums)):
            j = i + 1
            vals = set()
            while j < len(nums):
                
                desire = target - nums[j]
                if desire in vals:
                    res.append([nums[i], nums[j], desire])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                else:
                    vals.add(nums[j])
                j += 1

                
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1


        return res
                    



'''
[-1,0,1,2,-1,-4]
[-4, -1, -1, 0, 1, 2]
  ^

[-2,0,1,1,2]
        ^

[0,0,0,0]
 ^ ^

'''