class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = 1
        suffix_prod = 1
        output = [0]*n

        for i in range(n):
            output[i] = prefix_prod
            prefix_prod *= nums[i]
        
        for i in range(n-1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]

        return output


















        
        
        
        # n = len(nums)
        # prefix_prod = 1
        # postfix_prod = 1
        # output = [0]*n

        # for i in range(n):
        #     output[i] = prefix_prod
        #     prefix_prod *= nums[i]

        # for i in range(n-1, -1, -1):
        #     output[i] *= postfix_prod
        #     postfix_prod *= nums[i]
        
        # return output