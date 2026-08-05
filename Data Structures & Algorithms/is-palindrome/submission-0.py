class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = ''.join(char.lower() for char in s if char.isalnum())

        return s_filtered == s_filtered[::-1]