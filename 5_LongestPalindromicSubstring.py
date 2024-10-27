class Solution:
    def longestPalindrome(self, s):
        _dict = {}
        for i in range(len(s)):
            pald = self.get_palindrome(s, i, i)
            _dict[len(pald)] = pald
        return _dict[max(_dict.keys())]

    @staticmethod
    def get_palindrome(s, start, end):
        while end + 1 < len(s) and s[start] == s[end+1]:
            end += 1
        
        while start > 0 and end + 1 < len(s) and s[start-1] == s[end+1]:
            start -= 1
            end += 1
        
        return s[start:end+1]


sol = Solution()
print(sol.longestPalindrome("cbbd"))