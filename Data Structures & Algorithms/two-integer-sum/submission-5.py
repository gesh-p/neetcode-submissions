class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}
        for i in range(n):
            diff = target - nums[i]
            h[diff] = i
        
        for i in range(n):
            if nums[i] in h and i != h[nums[i]]:
                return [i, h[nums[i]]]
            
            