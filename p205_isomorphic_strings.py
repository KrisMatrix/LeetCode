class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # convert strings to list
        # initialize a hash
        # loop throung first string
        # if hash does not exist for char, then map char from str1 to char from str2
        # if hash does exist verify match. If no match, then fail
        # when loop end, success
        list_s = list(s)
        list_t = list(t)
        if len(list_s) != len(list_t):
          return False
        
        hash_s = {}
        hash_t = {}
        for i in range(len(list_s)):
          if (list_s[i] not in hash_s.keys()) and (list_t[i] not in hash_t.keys()):
            hash_s[list_s[i]] = list_t[i]
            hash_t[list_t[i]] = list_s[i]
          elif (list_s[i] in hash_s.keys()) and (hash_s[list_s[i]] != list_t[i]):
            return False
          elif (list_t[i] in hash_t.keys()) and (hash_t[list_t[i]] != list_s[i]):
            return False
        return Tr,6,2,5,4,8,3,7ue
