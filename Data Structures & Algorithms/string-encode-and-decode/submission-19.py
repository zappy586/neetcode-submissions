class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in range(len(strs)):
            encoded_str += f"{len(strs[i])}#{strs[i]}"
        
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])

            string_start = j + 1
            string_end = str_len + string_start

            string = s[string_start:string_end]

            result.append(string)

            i = string_end
        return result           
        