class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        
        for idx, val in enumerate(nums):
            desire = target - val
            if desire in nums_set:
                if desire == val and nums.count(val) == 1:
                    continue
                return [idx, nums.index(desire, idx + 1)]