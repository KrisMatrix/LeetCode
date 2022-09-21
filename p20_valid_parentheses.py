class Solution:
    def isValid(self, s: str) -> bool:
        list1 = list(s)
        hash = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        open_parens = []
        retVal = False
        if len(list1) % 2 != 0:
            return False
        for ptr in range(len(list1)):
            if list1[ptr] in hash.values():
                open_parens.append(list1[ptr])
            elif list1[ptr] in hash.keys():
                if len(open_parens) > 0:
                    last = open_parens.pop()
                else:
                    retVal = False
                    return retVal
                if hash[list1[ptr]] != last:
                    retVal = False
                    return retVal
                    break
        if len(open_parens) > 0:
            retVal = False
        else:
            retVal = True
        return retVal
