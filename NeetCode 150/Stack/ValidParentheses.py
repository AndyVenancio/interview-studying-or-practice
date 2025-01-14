'''
Valid Parentheses
Difficulty: Easy

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

    Input: s = "[]"
    Output: true

Example 2:

    Input: s = "([{}])"
    Output: true

Example 3:

    Input: s = "[(])"
    Output: false

'''

def isValid(s: str) -> bool:
    dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for p in s:
        if p in dict:
            if len(stack) == 0 or stack.pop() != dict[p]: # len(stack) == 0 means there are closing brackets that are not opened.
                return False
            else: 
                continue
        stack.append(p)
        
    return True if len(stack) == 0 else False # len(stack) != 0 means there are open brackets that are not closed.
            
            
s1 = "([{}])"
s2 = "[(])"
s3 = "[()[]()]"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))

'''
Notes:

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Short Explanation:
        - We will use a stack to keep track of the open brackets. 
            - If we encounter a closing bracket, we will check if the last element in the stack is the corresponding open bracket.
            - If not, we will return False.
        - Important: If the length of the stack is not 0 at the end, it means there are open brackets that are not closed. Return False in this case. 
                     If when we pop the stack, the stack is empty, it means there are closing brackets that are not opened. Return False in this case.
        
'''