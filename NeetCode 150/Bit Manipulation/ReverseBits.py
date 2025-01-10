'''
Reverse Bits
Difficulty: Easy

Given a 32-bit unsigned integer, reverse the bits of the binary representation of the integer and return the result.

Example 1:

    Input: n = 00000000000000000000000000010101
    Output:    2818572288 (10101000000000000000000000000000)

'''

def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res += (bit << (31 - i))
    return res

n = 0b00000000000000000000000000010101

print(reverseBits(n))

'''
Notes:

    Time complexity: O(1)
    Space complexity: O(1)
    
    res - variable to store the result
    n - input number
    >> - right shift operator
    & - AND operator
    << - left shift operator
    
    Short explanation:
        - Iterate through the 32 bits of the input number
        - Get the rightmost bit of the number (n >> i) & 1 
        - Left shift the bit by (31 - i) and add it to the result (res += (bit << (31 - i)))
        - Repeat the process until all bits are processed
        
'''