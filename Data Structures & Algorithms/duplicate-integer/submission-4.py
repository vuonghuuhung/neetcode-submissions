class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idxs = {}
        for i in nums:
            if i in idxs:
                return True
            idxs[i] = True
        return False