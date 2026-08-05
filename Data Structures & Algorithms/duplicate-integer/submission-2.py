class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dups = list(set(nums))
        return len(non_dups) != len(nums)