'''
Longest Increasing Subsequence
Difficulty: Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

Example 1:

    Input: nums = [9, 1, 4, 2, 3, 3, 7]
    Output: 4

Example 2:

    Input: nums = [0, 3, 1, 3, 2, 3]
    Output: 4

'''

from bisect import bisect_left
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    l = []
    l.append(nums[0])
    LIS = 1
    
    for i in range(len(nums)):
        if l[-1] < nums[i]:
            l.append(nums[i])
            LIS += 1
            # print(f'appended: {nums[i]}')
            # print(f'l: {l}')
            continue
        
        idx = bisect_left(l, nums[i])
        l[idx] = nums[i]
        # print(f'idx: {idx}')
        # print(f'l: {l}')
        
    return LIS

nums1 = [9, 1, 4, 2, 3, 3, 7]
nums2 = [0, 3, 1, 3, 2, 3]

print(lengthOfLIS(nums1))
print(lengthOfLIS(nums2))

'''
Notes:

    Time complexity: O(nlogn)
    Space complexity: O(n)

    bisect_left() - returns the index where the element should be inserted in a sorted list
    l - list to store the increasing subsequence
    LIS - length of the longest increasing subsequence
    idx - index where the element should be inserted in the list
    
    Short explanation: 
        - If the current element is greater than the last element of the list, append it to the list and increment LIS
        - If not, find the index where the element should be inserted and replace the element at that index with the current element
        - The length of the list is the length of the longest increasing subsequence
'''
