class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)

        count = {}
        maxf = 0
        for right in range(n):
            curr_element = s[right]
            count[curr_element] = count.get(curr_element, 0) + 1
            maxf = max(maxf, count[curr_element])

            window_length = right - left  + 1

            if window_length - maxf > k:
                count[s[left]] -= 1
                left += 1

        return n - left