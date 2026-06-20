class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        
        return False

        