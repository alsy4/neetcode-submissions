class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        left = 0
        n = len(s)

        for right in range(n):
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1
            maxf = max(maxf, freq[curr])

            window_length = right - left + 1

            if window_length - maxf > k:
                freq[s[left]] -= 1
                left += 1

        return n - left