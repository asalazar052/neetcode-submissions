class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
                
        def houseRobber1(arr):

            rob1, rob2 = 0, 0 # rob1 is 2 away from cur, rob2 is right next to cur
            for cur in arr:

                temp = max(rob1 + cur, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        return max(houseRobber1(nums[0 : len(nums) - 1]), houseRobber1(nums[1:]))