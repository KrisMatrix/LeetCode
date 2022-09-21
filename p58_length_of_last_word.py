class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_flag = 0
        length = 0
        for i in reversed(range(len(s))):
            if word_flag == 1 and s[i] == ' ':
                break
            elif s[i] != ' ':
                length += 1
                word_flag = 1
        return length
