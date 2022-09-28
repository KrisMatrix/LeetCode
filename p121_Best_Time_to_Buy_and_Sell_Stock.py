class Solution:
  def maxProfit_kk(self, prices: List[int]) -> int:
    # This is slower
    total = 0
    for i in range(0,len(prices)):
      for j in range(i+1,len(prices)):
        if prices[i] > prices[j]:
          continue
        else:
          total = max(total, prices[j]-prices[i])
    return total
    
  def maxProfit(self,prices):
    left = 0              # Buy
    right = 1             # Sell
    max_profit = 0
    while right < len(prices):
      currentProfit = prices[right] - prices[left] #our current Profit
      if prices[left] < prices[right]:
        max_profit = max(currentProfit,max_profit)
      else:
        left = right
      right += 1
    return max_profit
