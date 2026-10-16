class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str += str(len(i))
            encoded_str += '#'
            encoded_str += i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #findign the length could be double digits
            i = j + 1
            j = int(length) + i
            decoded_str.append(s[i:j])
            i = j
        return decoded_str
