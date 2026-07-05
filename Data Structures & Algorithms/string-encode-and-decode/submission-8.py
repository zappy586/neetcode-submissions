class Solution:

    def encode(self, strs: List[str]) -> str:
        tempStr = ""
        if not strs:
            return 'empty'
        n = len(strs)
        for i in range(0,n-1):
            tempStr += strs[i] + '\n'
        tempStr += strs[n-1]
        return tempStr
    def decode(self, s: str) -> List[str]:
        if s=="":
            return [""]
        if s=="empty":
            return []
        return s.split('\n')
