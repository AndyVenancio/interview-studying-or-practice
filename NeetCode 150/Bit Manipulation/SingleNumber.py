'''
Single Number
Difficulty: Easy

You are given a non-empty array of integers nums. Every element appears twice except for one. Return the integer that appears only once.

You must implement a solution with a linear O(n) runtime complexity and use only constant extra space O(1).

Example 1:

    Input: nums = [3, 2, 3]
    Output: 2
    
Example 2:

    Input: nums = [7, 6, 6, 7, 8]
    Output: 8

'''

from typing import List

def singleNumber(nums: List[int]) -> int:
    s = 0
    for num in nums:
        s = num ^ s
    return s

nums1 = [3, 2, 3]
nums2 = [7, 6, 6, 7, 8]

print(singleNumber(nums1))
print(singleNumber(nums2))

'''
Notes:

    Time complexity: O(n)
    Space complexity: O(1)
    
    s - variable to store the single number
    num - element in the list
    ^ - XOR operator
    
    Short explanation:
        - XOR all the elements in the list
        - The XOR of two same numbers is 0
        - The XOR of a number and 0 is the number itself
        - The single number will be left in the variable s
        
'''