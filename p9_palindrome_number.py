class Solution:
  def isPalindrome(self, x: int) -> bool:
    # convert number to string
    # convert string to list
    # take first and last index
    # compare the two. If not same return error
    # if same, then decrement indices and compare.
    # when both first and last index are same. Stop decrementing.

    x = list(str(x))    #convert number to string to list.
    first = 0
    last = len(x) - 1
    while(1):
      if first == last:
        return True
      if x[first] != x[last]:
        return False
      else:
        first += 1
        last -= 1

if __name__ == '__main__':
  print("Method 1")
  j = Solution()
  print(j.isPalindrome(121))
  print(j.isPalindrome(-121))
  print(j.isPalindrome(10))
  print(j.isPalindrome(0))
