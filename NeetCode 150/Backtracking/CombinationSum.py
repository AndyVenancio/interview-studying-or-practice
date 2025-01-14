'''
Combination Sum
Difficulty: Medium

You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

    Input: 
        nums = [2,5,6,9] 
        target = 9
    Output: [[2,2,5],[9]]

Example 2:
    Input: 
        nums = [3,4,5]
        target = 16
    Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:

    Input: 
        nums = [3]
        target = 5
    Output: []

'''

from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    
    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return
        
        cur.append(nums[i]) # Add the current number to the current combination, add it to the result list if the total sum is equal to the target
        dfs(i, cur, total + nums[i])
        cur.pop() 
        dfs(i + 1, cur, total) # Move on to the next number in the array
        
    dfs(0, [], 0)
    return res

'''
Notes:

    Time complexity: O(2^(t/m)) where t is the target and m is the minimum value in the nums array
    Space complexity: O(t/m)
    
    Short explanation:
        - We use dfs to find all possible combinations of the numbers in the nums array that sum to the target
        - For each iteration of dfs(), we either add the current number to the current combination or we don't
            - If we do, we must also increase the total sum by the current number
            - If we don't, we move on to the next number in the array by increasing i by 1
        - Stop Conditions:
            - If the total sum is equal to the target, we add the current combination to the result list
            - If the total sum is greater than the target or if we have gone through all the numbers in the array, we stop the current iteration
            
'''