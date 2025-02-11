'''
Valid Anagram
Difficulty: Easy

Given two string s and t, return true if the two strings are anagrams of each other, otherwise return false. 

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

    Input: s = "racecar", t = "carrace"
    Output: True
    
Example 2:

    Input: s = "jar", t = "jam"
    Output: False
'''

from typing import List

def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    s_dic = {}
    t_dic = {}
    for i in range(len(s)):
        s_dic[s[i]] = 1 + s_dic.get(s[i], 0)
        t_dic[t[i]] = 1 + t_dic.get(t[i], 0)
    return s_dic == t_dic

s1, t1 = "racecar", "carrace"
s2, t2 = "jar", "jam"

print(isAnagram(s1, t1))
print(isAnagram(s2, t2))


'''
Notes:

    Time Complexity: O(n + m) where n is the length of s and m is the length of t
    Space Complexity: O(1) 
    
    Short Explanation:
        - Check if the length of s and t are not equal, if not return False
        - Create two dictionaries s_dic and t_dic
        - Loop through the length of s and t
            - Add the character to the dictionary and increment the count
        - Return if the two dictionaries are equal
'''
    