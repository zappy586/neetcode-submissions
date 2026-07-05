class Solution:
    def encode(self, strs):
        out = []
        for s in strs:
            out.append(f"{len(s)}#{s}")   # length-prefix
        return "".join(out)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':           # read length
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])    # read actual string
            i = j + length
        return res
