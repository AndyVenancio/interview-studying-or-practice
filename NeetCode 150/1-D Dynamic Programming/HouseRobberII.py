'''
House Robber II
Difficulty: Medium

Similar to House Robber, but the houses are arranged in a circle. That is, the first house is the neighbor of the last house.

'''
from typing import List

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    return max(helper(nums[:-1]), helper(nums[1:]))
    
def helper(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
    return dp[-1]

nums = [2,9,8,3,6]
print(rob(nums))

'''
Notes:

    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    Short explanation:
        - Begin by splitting the nums into two arrays, one including the first house and excluding the last house, 
          and the other excluding the first house and including the last house.
            - This allows us to treat the problem as two separate House Robber problems, ignoring the circular nature of the houses. 
        - The rest is similar to the original House Robber problem. We use bottom-up dynamic programming to find the maximum amount of money that can be robbed.    

'''