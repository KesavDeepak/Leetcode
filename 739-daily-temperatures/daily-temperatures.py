class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #[temp, index] nested list
        for i,n in enumerate(temperatures):
            while stack and n > stack [-1][0]:
                stackval, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([n,i])
        return res
        