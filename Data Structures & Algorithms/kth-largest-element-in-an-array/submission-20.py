class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        l, r = 0, len(nums) - 1
        
        while True:

            swap = l
            pivot = r

            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    nums[swap], nums[i] = nums[i], nums[swap]
                    swap += 1
                
            nums[swap], nums[pivot] = nums[pivot], nums[swap]

            print(swap)

            if k == swap:
                return nums[swap]
            elif k > swap: # Check right partition
                l = swap + 1
            else: # Check left partition
                r = swap - 1
            
                
