import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        print(dic)
        heap = [(values, key) for key, values in dic.items()]
        heapq.heapify_max(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res


