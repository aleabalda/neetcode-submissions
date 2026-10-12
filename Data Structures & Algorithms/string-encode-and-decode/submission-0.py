class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + "$" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length_of_word = int(s[i:j])
            word = s[j + 1:j + 1 + length_of_word]
            decoded.append(word)
            i = j + 1 + length_of_word
        
        return decoded
        
