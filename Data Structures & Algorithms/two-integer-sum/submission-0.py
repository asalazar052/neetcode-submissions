class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indicies = {} # Value : Index

        for i in range(len(nums)):
            desire = target - nums[i]
            if desire in indicies:
                return [indicies[desire], i]
            else:
                indicies[nums[i]] = i