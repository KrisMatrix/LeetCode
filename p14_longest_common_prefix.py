class Solution:
    def longestCommonPrefix_v1(self, strs: List[str]) -> str:
        lista = []
        hash = {}
        print(type(lista))
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                print(i,j)
                if i >= len(strs[j]):
                    break
                elif strs[0][i] == strs[j][i]:
                    lista.append(strs[0][i])
                else:
                    lista.pop()
                    
        print(lista)
        
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        start = min(strs)   #return the lowest string
        end = max(strs)     #returns the highest string
        for index, char in enumerate(start):
            if char != end[index]:
                return start[:index]    #start to the everything before the index where there is no match
        return start                    # if we got here, then everything matches.
