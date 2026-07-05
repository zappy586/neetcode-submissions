class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = [string+"|" for string in strs]
        encoded_string = ""
        for string in strs:
            encoded_string += string
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = s.split("|")[:-1]
        return decoded_string