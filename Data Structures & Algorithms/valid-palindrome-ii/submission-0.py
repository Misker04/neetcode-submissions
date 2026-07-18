class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return (isPalindrome(i+1, n-i-1) or isPalindrome(i, n-i-2))
        return True


        