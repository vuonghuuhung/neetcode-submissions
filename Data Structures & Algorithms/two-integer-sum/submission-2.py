class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}

        for idx, val in enumerate(nums):
            nums_set[val] = idx

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in nums_set and nums_set[diff] != idx:
                return [idx, nums_set[diff]]