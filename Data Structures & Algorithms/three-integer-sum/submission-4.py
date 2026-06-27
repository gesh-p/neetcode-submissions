class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums) #n log n
        output = []
        dup = set()
        for i in range(n):
            num = nums[i]
            if num in dup:
                continue
            dup.add(num)
            x = i + 1
            y = n - 1
            filt = set()
            while x < y:
                if x == i:
                    x += 1
                    continue
                if y == i:
                    y -= 1
                    continue
                if num + nums[x] + nums[y] == 0:
                    if nums[i] not in filt or nums[x] not in filt or nums[y] not in filt:
                        output.append([num, nums[x], nums[y]])
                        filt.add(nums[i])
                        filt.add(nums[x])
                        filt.add(nums[y])
                    x += 1
                    y -= 1
                elif num + nums[x] + nums[y] < 0:
                    x += 1
                else:
                    y -= 1
        
        return output
            
        