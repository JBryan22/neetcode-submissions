class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sets = []

        def genParen(currStr: str, left_count: int, right_count: int):
            if left_count + right_count == (n * 2) and left_count == right_count:
                sets.append(currStr)
                return
            if right_count > left_count or left_count + right_count >= (n * 2):
                return

            if left_count <= n:
                currStr += "("
                genParen(currStr, left_count + 1, right_count)
                currStr = currStr[:-1]

            if right_count < left_count:
                currStr += ")"
                genParen(currStr, left_count, right_count + 1)
                currStr = currStr[:-1]
        
        genParen("", 0, 0)
        return sets