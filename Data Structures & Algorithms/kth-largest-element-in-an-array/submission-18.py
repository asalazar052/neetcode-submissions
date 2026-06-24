class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # kth largest becomes kth index in sorted ascending order

        l, r = 0, len(nums) - 1

        while True:
            pivot = r
            swap = l

            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    nums[swap], nums[i] = nums[i], nums[swap]
                    swap += 1

            nums[swap], nums[pivot] = nums[pivot], nums[swap]

            if swap == k:
                return nums[swap]
            elif k > swap:
                l = swap + 1
            else:
                r = swap - 1