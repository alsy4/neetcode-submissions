class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        - Count element in `t`
        - Start a window at `left`
        - Expand `right` window until substring is valid(all element in s is in t)
        - Compare element count in `have` and `need`(len(t)) and find minimum res and res_length
        """

        if t == "":
            return ""

        count_t = {}
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        count_window = {}

        have = 0  # Number of elements we have are correct
        need = len(count_t)

        res, res_len = [-1, -1], float("infinity")

        left = 0
        n = len(s)
        for right in range(n):
            c = s[right]
            count_window[c] = count_window.get(c, 0) + 1

            if c in count_t and count_window[c] == count_t[c]:
                have += 1

            while have == need:
                window_length = right - left + 1

                if window_length < res_len:
                    res = [left, right]
                    res_len = window_length

                left_char = s[left]
                count_window[left_char] -= 1

                if (
                    left_char in count_t
                    and count_window[left_char] < count_t[left_char]
                ):
                    have -= 1

                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""