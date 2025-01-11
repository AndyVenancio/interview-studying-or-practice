'''
Pow(x, n)
Difficulty: Medium

Pow(x, n) is a function that calculates x raised to the power n (i.e., x^n). Given a floating-point value for x and an integer value for n, implement this function.

You may not use the built-in implementation of pow(x, n).

Example 1:

    Input: x = 2.00000, n = 5
    Output: 32.00000
    
Example 2:

    Input: x = 1.10000, n = 10
    Output: 2.59374
    
Example 3:

    Input: x = 2.00000, n = -3
    Output: 0.12500
    
'''

def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    
    power = abs(n)
    res = 1
    
    while power:
        if power & 1:
            res *= x    
        x *= x
        power >>= 1
        
    return res if n > 0 else 1 / res

print(myPow(2.00000, 5))
print(myPow(1.10000, 10))
print(myPow(2.00000, -3))

'''
Notes:

    Time Complexity: O(log(n))
    Space Complexity: O(1)
    
    Short explanation:
        - We are using the binary representation of the power to calculate the result.
        - For example, if we want to calculate 2^5, 5 in binary is 101, so we would calculate 2^1 * 2^4. This results in time complexity O(log(n)).
        - To do this, we iterate through the binary representation of the power, and if the bit is 1, we multiply the result by x. Every iteration, we multiply x by itself to get the next power of x.
        - In the end, we return the result if n is positive, and 1 divided by the result if n is negative.
        
'''
            