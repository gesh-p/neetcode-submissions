class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n
        i = 0

        while i < n:
            if len(stack) == 0:
                stack.append([temperatures[i], i])
                i += 1
                continue
            
            if temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
                i += 1
                
            else:
                while stack[-1][0] < temperatures[i]:
                    val, idx = stack.pop()
                    output[idx] = i - idx
                    
                    if len(stack) == 0:
                        break

                
        return output


# [1, 2] : i = 0
#[1], 2 : output = [0, 0] : i = 1
#[], 2 : output = [1, 0] : i = 1
#[2] : i = 1

# [3, 1, 2, 4]

# [] 3 l = 0
# [3] 1 l = 1
# [3, 1] 2 l = 2
# [3, 2] 
# [3, 2] 4 l = 3
# [4]

