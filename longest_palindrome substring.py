class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # slice that forms palindrome

        res = ""
        for i in range(len(s)):
            # Odd-length palindrome (center at i)
            tmp = expand(i, i)
            if len(tmp) > len(res):
                res = tmp

            # Even-length palindrome (center between i and i+1)
            tmp = expand(i, i+1)
            if len(tmp) > len(res):
                res = tmp

        return res
        
