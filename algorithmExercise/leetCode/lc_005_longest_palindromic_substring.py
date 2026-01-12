class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_len = 1

        def expand(l, r):
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                    start = l
                l -= 1
                r += 1

        for i in range(len(s)):
            # Odd length palindromes (center at i)
            expand(i, i)
            # Even length palindromes (center between i and i+1)
            expand(i, i + 1)

        return s[start:start + max_len]
