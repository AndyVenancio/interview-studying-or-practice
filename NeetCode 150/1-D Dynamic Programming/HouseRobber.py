'''
House Robber
Difficulty: Medium

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically contact the police if two adjacent houses were broken into on the same night.

Return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

    Input: nums = [1,1,3,3]
    Output: 4

Example 2:

    Input: nums = [2,9,8,3,6]
    Output: 16

'''

from typing import List

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
    return dp[-1]

nums = [100, 1, 1, 100]
print(rob(nums))


# Second approach using memoization and top-down dynamic programming
# def rob(nums: List[int]) -> int:
#     memo = [-1] * len(nums) # Stores the maximum amount of money that can be robbed up to the ith house
#     
#     def dfs(it):
#         if it >= len(nums):
#             return 0
#         if memo[it] != -1:
#             return memo[it]
#         
#         memo[it] = max(dfs(it + 1), nums[it] + dfs(it + 2)) # Either rob the ith house or do not rob the ith house
#         return memo[it] 
#     
#     return dfs(0)

'''
Notes:

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Uses bottom-up dynamic programming to solve the problem. The dp array stores the maximum amount of money that can be robbed up to the ith house.
    
    Short explanation:
    
        - Create dp array of size n where n is the number of houses, and initialize the first two elements of the dp array to be the maximum of the first two houses.
            - dp[1] is the maximum that can be robbed from the first two houses because we cannot rob two adjacent houses.
        - dp[i] depends on whether we rob the ith house or not. If we rob the ith house, then we cannot rob the (i-1)th house. If we do not rob the ith house, then we can rob the (i-1)th house. 
          This explains why dp[i] = max(dp[i-1], nums[i] + dp[i-2]).
        - The final answer is the last element of the dp array.
        
    The second approach uses memoization and top-down dynamic programming to solve the problem. The memo array stores the maximum amount of money that can be robbed up to the ith house.
    
'''