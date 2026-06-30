class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        for i in range(n):
            curr = temperatures[i]
            counter = 0
            for j in range(i + 1, n):
                counter += 1
                if curr < temperatures[j]:
                    output[i] = counter
                    break
                                
        
        return output