class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 3:
            return list(set(nums))
        
        c1 = 0
        c2 = 0
        maj1 = 0
        maj2 = 0
        for num in nums:
            if c1 == 0 and num != maj2:
                maj1 = num
            elif c2 == 0 and num != maj1:
                maj2 = num
            
            if num == maj1:
                c1 += 1
            elif num == maj2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == maj1:
                count1 += 1
            elif num == maj2:
                count2 += 1

        result = []
        maxocc = math.floor(n/3)
        if count1 > maxocc:
            result.append(maj1)
        if count2 > maxocc:
            result.append(maj2)
        return result
        
        