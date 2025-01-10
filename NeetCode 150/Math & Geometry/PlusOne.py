'''
Plus One
Difficulty: Easy

You are given an integer array digits, where each digits[i] is the ith digit of a large integer. 
It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

    Input: digits = [1,2,3,4]
    Output: [1,2,3,5]
    
Example 2:

    Input: digits = [9,9,9]
    Output: [1,0,0,0]

'''

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits[-1] += 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > 9:
            digits[i] = 0
            if i - 1 >= 0:
                digits[i - 1] += 1
                continue
            digits = [1] + digits
            
    return digits

digits1 = [1,2,3,4]
digits2 = [9,9,9]

print(plusOne(digits1))
print(plusOne(digits2))

'''
Notes:

    Time Complexity: O(n)
    Space Complexity: O(1)

    Short explanation:
        - Implementing the same thing we would do manually when adding 1 to a number.
        
'''