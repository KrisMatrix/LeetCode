class Solution:
    def getHint(self, secret: str, guess: str) -> str:
      hash = {}
      bulls = 0
      crows = 0
      for i in range(len(secret)):
        if secret[i] == guess[i]:
          bulls += 1
        else:
          if secret[i] not in hash.keys():
            hash[secret[i]] = 1
          else:
            hash[secret[i]] += 1
      
      for j in range(len(guess)):
        if guess[j] in hash.keys() and (secret[j] != guess[j]):
          if hash[guess[j]] > 0:
            crows += 1
            hash[guess[j]] -= 1
      return str(bulls) + "A" + str(crows) + "B"
