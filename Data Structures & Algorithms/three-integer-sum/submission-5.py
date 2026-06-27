#optimal solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #n log n
        output = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            x, y = i + 1, len(nums) - 1
            while x < y:
                total = a + nums[x] + nums[y]
                if total == 0:
                    output.append([a, nums[x], nums[y]])
                    x += 1
                    y -= 1
                    while nums[x] == nums[x - 1] and x < y:
                        x += 1
                elif total < 0:
                    x += 1
                else:
                    y -= 1
        
        return output
            
        