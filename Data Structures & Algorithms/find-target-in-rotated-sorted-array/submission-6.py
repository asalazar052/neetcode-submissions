class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] <= nums[r]: # right sorted
                if target > nums[r] or target < nums[m]: # must be in between l and m
                    r = m - 1
                else: # in the sorted portion
                    l = m + 1 

            elif nums[m] >= nums[l]: # left sorted
                
                if target < nums[l] or target > nums[m]: # must be in between m and r
                    l = m + 1
                else:
                    r = m - 1
            
            # else:
            #     if target < nums[m]: 
            #         r = m - 1
            #     else:
            #         l = m + 1
                
            
        return -1



'''

[5,1,2,3,4] target = 1   
     ^
[3,4,5,1,2] target = 1
     ^


'''