class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = list(sorted(set(nums)))
        n = len(nums)
        final_seq = 0
        curr_seq = 1
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                curr_seq += 1
            else:
                final_seq = max(curr_seq, final_seq)
                curr_seq = 1
        final_seq = max(curr_seq, final_seq)
    
        return final_seq
        