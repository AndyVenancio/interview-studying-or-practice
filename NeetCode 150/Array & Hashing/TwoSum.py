'''
Two Sum
Difficulty: Easy

Given an array of integers nums and integer target, return the indices i and j such that nums[i] + nums[j] == target. and i != j

You may assume that each input would have exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

    Input:
        nums = [3, 4, 5, 6] 
        target = 7
        
    Output: [0, 1]
    
Example 2:

    Input:
        nums = [4, 5, 6]
        target = 10
        
    Output: [0, 2]
    
Example 3:

    Input:
        nums = [5, 5]
        target = 10
        
    Output: [0, 1]
'''

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    temp = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in temp.keys():
            return [temp[complement], i]
        temp[nums[i]] = i
    return []

nums1, target1 = [3, 4, 5, 6], 7
nums2, target2 = [4, 5, 6], 10
nums3, target3 = [5, 5], 10

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))


'''
Notes:

    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n)
    
    Short Explanation:
        - Create a dictionary temp
        - Loop through the list nums
            - Calculate the complement by subtracting the current number from the target
            - If the complement is already in the dictionary, return the indices of the complement and the current number
            - Otherwise add the current number and its index to the dictionary
        - Return an empty list if no pair is found
'''