class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        substring = set()
        maxLength = 0
        left = 0

        for right in range(n):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength