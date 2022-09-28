class Solution:
    def longestPalindrome_v1(self, s: str) -> int:
        total = 0
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash.keys():
                hash[s[i]] = 1
            else:
                hash[s[i]] += 1
            
        at_least_one_odd = 0
        for key in hash.keys():
            if hash[key] % 2 == 0:
                total += hash[key]
            else:
                at_least_one_odd = 1
                hash[key] -= 1
                total += hash[key]
        if at_least_one_odd:
            total += 1
        #total += 1
        return total
    
    def longestPalindrome(self, s: str) -> int:
        total = 0
        hash = set()
        for char in s:
            #if we have even number of the same
            # char, then the hash remainds empty.
            #if we have odd number of the same
            # char, then the hash exists.
            if char not in hash:
                hash.add(char)
            else:
                hash.remove(char)
                
        if len(hash) > 0:
            return len(s) - len(hash) + 1
        else:
            return len(s)
