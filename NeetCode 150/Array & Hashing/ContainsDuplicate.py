'''
Contains Duplicate
Difficulty: Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

    Input: nums = [1, 2, 3, 3]
    Output: true
    
Example 2:

    Input: nums = [1, 2, 3, 4]
    Output: false
'''

from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    temp = {}
    for num in nums:
        if num in temp.keys():
            return True
        temp[num] = 1
    return False

nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 3]

print(hasDuplicate(nums1))
print(hasDuplicate(nums2))

'''
Notes:

    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n)
    
    Short Explanation:
        - Create a dictionary temp
        - Loop through the list nums
            - If the number is already in the dictionary, return True
            - Otherwise add the number to the dictionary
        - Return False
'''