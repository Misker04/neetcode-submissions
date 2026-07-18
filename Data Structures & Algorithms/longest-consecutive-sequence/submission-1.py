class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1

        # nums = list(sorted(set(nums)))
        # n = len(nums)
        # final_seq = 0
        # curr_seq = 1
        # for i in range(1, n):
        #     if nums[i] == nums[i-1] + 1:
        #         curr_seq += 1
        #     else:
        #         final_seq = max(curr_seq, final_seq)
        #         curr_seq = 1
        # final_seq = max(curr_seq, final_seq)
    
        # return final_seq
        