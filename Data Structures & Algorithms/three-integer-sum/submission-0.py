class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for k in range(n-2):
            if k>0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = n-1
            while i < j:
                threesum = nums[i]+nums[j]+nums[k]
                if threesum == 0:
                    output.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
                elif threesum > 0:
                    j -= 1
                else:
                    i += 1
        return output




        