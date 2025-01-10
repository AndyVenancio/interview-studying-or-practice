'''
Missing Number
Difficulty: Easy

Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
    Input: nums = [1,2,3]
    Output: 0

Example 2:

    Input: nums = [0,2]
    Output: 1

'''

from typing import List

def missingNumber(nums: List[int]) -> int:
    res = len(nums)
    for i in range(len(nums)):
        res += i - nums[i]
        
    return res

nums1 = [1,2,3]
nums2 = [0,2]

print(missingNumber(nums1))
print(missingNumber(nums2))

'''
Notes:

    Time complexity: O(n)
    Space complexity: O(1)
    
    Short explanation:
        - Not bitwise manipulation
        - Since the array is ordered, the number missing will be the same as the numbers that are not in the correct position.
        - Therefore, we can find the missing number by adding the difference between the index and the number in the array to the length of the array.
        
'''