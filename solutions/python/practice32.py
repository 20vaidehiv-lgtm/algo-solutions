# Problem: Best Time to Buy and Sell Stock
# Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Note: Solves the Best Time to Buy and Sell Stock problem
# Description:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing 
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve 
# any profit, return 0.
#
# Input:
# - An array `prices` where 1 <= prices.length <= 10^5
# - Each price is a non-negative integer where 0 <= prices[i] <= 10^4
#
# Output:
# - An integer representing the maximum profit
#
# Status: ✅ SOLVED

class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
                
        return max_profit

# Test cases with assertions
s = Solution()
