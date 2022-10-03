class Solution():
    def decodeString(self, s:str) -> str:
        while('[' in s):
            s = self.create_string(s)
        return s

    def create_string(self, s:str):
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        for i in range(len(s)):
            if s[i] == '[':
                j = i-1
                num = None
                while (j >=0 and s[j].isnumeric()):
                    if num == None:
                        num = s[j]
                    else:
                        num = s[j] + num
                    j -= 1
                num = int(num)
                ptr3 = j
                ptr1 = i
            elif s[i] == ']':
                ptr2 = i
                break
        s = s[0:ptr3+1] + num * s[ptr1+1:ptr2] + s[ptr2+1:len(s)]
        return s

                
obj = Solution()
print(obj.decodeString("3[a2[c]]d"))
print(obj.decodeString("3[a]2[bc]"))
print(obj.decodeString("3[a2[c]]"))
print(obj.decodeString("2[abc]3[cd]ef"))
print(obj.decodeString("100[leetcode]"))
