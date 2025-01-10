'''
Counting Bits
Difficulty: Easy

Given an integer n, count the number of 1's in the binary representation of every number i in the range 0 <= i <= n.
Return an array of the count of 1's for every number i in the range 0 <= i <= n.

Example 1:
    
    Input: n = 4
    Output: [0,1,1,2,1]
    
'''

def countBits(n: int) -> int:
    count = []
    for i in range(n+1):
        curr = i
        ones = 0
        while curr:
            ones += 1 if curr & 1 else 0
            curr >>= 1
        count.append(ones)
        
    return count

n = 4

print(countBits(4))

'''
Notes:

    Time complexity: O(n)
    Space complexity: O(n)
    
    Very similar to "Number of 1 Bits" problem. We can use the same approach here but we need to do it for every number in the range 0 <= i <= n.
    
'''
