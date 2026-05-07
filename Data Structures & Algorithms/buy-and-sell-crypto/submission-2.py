from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 
            set buy_price as first value,
            set max_profit = 0
            at each loop check the value, 
                if the value of the next is buy_price:
                    profit = buy_price - price[i]
                    if profit is greater max_profit:
                        set max_profit = profit
                elif less
                    take the value as buy_prices
                    
         '''
        max_profit = 0
        buy_price = prices[0]
        n = len(prices)

        i = 1
        while i < n:
            current_price = prices[i]
            if current_price >= buy_price:
                profit = current_price - buy_price
                
                if profit > max_profit:
                    max_profit = profit
            
            elif current_price < buy_price:
                buy_price = current_price
            
            i += 1

        return max_profit
    

sol = Solution()
profit = sol.maxProfit([10,1,5,6,7,1])
print(f"Profit: {profit}")