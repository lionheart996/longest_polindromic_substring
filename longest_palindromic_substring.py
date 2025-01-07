class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindromic substring found
            return s[left + 1:right]

        longest_palindrome = ""

        for i in range(len(s)):
            # Check for odd-length palindromes
            palindrome1 = expand_around_center(i, i)
            # Check for even-length palindromes
            palindrome2 = expand_around_center(i, i + 1)

            # Update the longest palindrome if needed
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome

# babad