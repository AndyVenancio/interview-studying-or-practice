'''
Number of One Bits
Difficulty: Easy

You are given an unsigned integer n, return the number of '1' bits in its binary representation.

Example 1:

    Input: n = 00000000000000000000000000001011
    Output: 3
    
Example 2:

    Input: n = 01111111111111111111111111111101
    Output: 30

'''

def numberOfOneBits(n: int) -> int:
    res = 0
    while n:
        if n & 1:
            res += 1
        n >>= 1
        
    return res

n1 = 0b00000000000000000000000000001011
n2 = 0b01111111111111111111111111111101

print(numberOfOneBits(n1))
print(numberOfOneBits(n2))

'''
Notes:

    Time complexity: O(1)
    Space complexity: O(1)
    
    res - variable to store the number of '1' bits
    n - input number
    & - AND operator
    >> - right shift operator
    
    Short explanation:
        - Check the rightmost bit of the number (n & 1)
        - If it is 1, increment the result
        - Right shift the number by 1
        - Repeat the process until the number becomes 0 (while n)
        
'''