class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        remove all spaces
        two pointer
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        i, j = 0, len(s) - 1

        while i < j:
            first_word = s[i]
            second_word = s[j]

            if first_word != second_word:
                return False

            i += 1
            j -= 1

        return True
        