class Solution:
    def lengthOfLongestSubstring(self, s):
        hash_s = {}
        mx = 0
        for i in range(len(s)):
            if s[i] in hash_s:
                mx = max(mx, len(hash_s))
                hash_s = {j: hash_s[j] for j in hash_s if hash_s[j] >= hash_s[s[i]]}
            hash_s[s[i]] = i
        return max(mx, len(hash_s))

sol = Solution()
print(sol.lengthOfLongestSubstring("anviaj"))       