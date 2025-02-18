'''
Group Anagrams
Difficulty: Medium

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

    Input: strs = ["act","pots","tops","cat","stop","hat"]
    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

    Input: strs = ["x"]
    Output: [["x"]]

Example 3:

    Input: strs = [""]
    Output: [[""]]
'''

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    m = {}
    
    for word in strs:
        temp = [0] * 26
        for l in word:
            index = ord(l) - ord('a')
            temp[index] += 1
        m[tuple(temp)] = m.get(tuple(temp), []) + [word]
        
    return list(m.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))

'''
Notes:

    Time Complexity: O(m * n) where m is the number of strings and n is the length of the longest string
    Space Complexity: O(m)
    
    Short Explanation:
        - Create a dictionary m
        - Loop through the list of strings
            - Create a list temp of length 26 with all elements as 0
            - Loop through the characters in the string
                - Get the index of the character and increment the count in temp
            - Add the string to the dictionary with the tuple of temp as the key
        - Return the values of the dictionary as a list
'''