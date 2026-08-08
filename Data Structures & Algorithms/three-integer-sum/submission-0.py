class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            offset = nums[i]
            if offset > 0:
                break
            elif i > 0 and offset == nums[i - 1]:
                continue

            lo, hi = i+1, n-1

            while lo < hi:
                low = nums[lo]
                high = nums[hi]

                total = offset + low + high
                if total == 0:
                    res.append([offset, high, low])

                    lo += 1
                    hi -= 1

                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo +=1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

                elif total < 0:
                    lo +=1
                else:
                    hi -= 1

        return res
        