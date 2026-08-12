class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        rotating: put the last element at the first
        """
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l + (r)) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
            