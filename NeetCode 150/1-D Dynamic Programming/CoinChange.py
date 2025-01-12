'''
Coin Change
Difficulty: Medium

You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

    Input: coins = [1,5,10], amount = 12
    Output: 3

Example 2:

    Input: coins = [2], amount = 3
    Output: -1

Example 3:

    Input: coins = [1], amount = 0
    Output: 0

'''

from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    memo = {}
    
    def dfs(amount):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        res = 1e9 # placeholder for the minimum number of coins needed to make up the amount
        
        for coin in coins:
            if amount - coin >= 0: # skip if the amount is negative
                res = min(res, 1 + dfs(amount - coin)) 
                
        memo[amount] = res
        # print(memo)
        return res
    
    minCoins = dfs(amount)
    return -1 if minCoins >= 1e9 else minCoins

coins = [1, 2, 5]
amount = 11

print(coinChange(coins, amount))


'''
Notes

    Time Complexity: O(n * m) where n is the amount and m is the number of coins
    Space Complexity: O(n)
    
    Short explanation:
        - Memoization is used to store the minimum number of coins needed to make up the amount, resolves overlapping subproblems
        - There are two base cases:
            - If the amount is 0, return 0
            - If the amount is already in the memo, return the value
        - Again, we use Depth First Search to find the minimum number of coins needed to make up the amount (greedy approach)
'''
        
    