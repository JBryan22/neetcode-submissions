class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res = []

        while pointer < len(s):
            num = 0
            while s[pointer] != '#':
                num = (num * 10) + int(s[pointer])
                pointer += 1
            pointer += 1
            res.append("".join(s[pointer:pointer+num]))
            pointer = pointer + num
        return res
