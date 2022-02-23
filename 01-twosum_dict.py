class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i,n in enumerate(nums):
            if target - n in seen:
                return([seen[target - n], i])
                #print(seen)
            elif n not in seen:
                seen[n] = i  # key is num, value is index of nums
            
