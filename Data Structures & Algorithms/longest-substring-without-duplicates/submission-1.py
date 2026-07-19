class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            hashmap[s[right]] = right
            result = max(result, right - left + 1)
        return result



        # left = 0 
        # result = 0
        # charSet = set()
        # for right in range(len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left += 1
        #     charSet.add(s[right])
        #     result = max(result, right - left + 1)
        # return result