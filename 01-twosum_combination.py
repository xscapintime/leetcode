
# Memory Limit Exceeded

from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = []
        for pair in list(combinations(nums,2)):
            if pair[0] + pair[1] == target:
                if pair[0] != pair[1]:
                    first = nums.index(pair[0])
                    second = nums.index(pair[1])
                    #val = [ nums.index(pair[0]),nums.index(pair[1])]
                    val = [first, second]
                    
                else:
                    first = nums.index(pair[0])
                    nums.pop(first)
                    second = nums.index(pair[1]) + 1
                    
                    val = [first, second ]
                    #val.append(nums.index(pair[0]))
        return val
