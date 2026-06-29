class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((temperatures[i], i))
        for temp in stack:
            _, ind = stack.pop()
            res[ind] = 0
        
        return res
