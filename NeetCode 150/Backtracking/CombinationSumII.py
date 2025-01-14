'''
Combination Sum II
Difficulty: Medium

You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

    Input: candidates = [9,2,2,4,6,1,5], target = 8
    Output: [
      [1,2,5],
      [2,2,4],
      [2,6]
    ]
    
Example 2:

    Input: candidates = [1,2,3,4,5], target = 7
    Output: [
      [1,2,4],
      [2,5],
      [3,4]
    ]


'''

from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()
    
    def dfs(i, cur, total):
        if total == target:
            # print(cur)
            res.append(cur.copy())
            return 
        if i >= len(candidates) or total > target:
            return 
        
        cur.append(candidates[i])
        dfs(i + 1, cur, total + candidates[i])
        cur.pop()
        for j in range(i, len(candidates)):
            if candidates[i] != candidates[j]:
                dfs(j, cur, total)
                break
        return
    
    dfs(0, [], 0)
    return res

candidates=[9,2,2,4,6,1,5]
target=8

print(combinationSum2(candidates, target))

'''
Notes:

    Time Complexity: O(n*2^n)
    Space Complexity: O(n)
    
    Short Explanation:
        - Exact same as Combination Sum but with a slight modification to the dfs function to avoid duplicates
        - We sort the candidates array to avoid duplicates
        - Two paths can be taken inside the dfs function:
            - Add the current number to the current combination and move on to the next number in the array (don't have to worry about duplicates here because we are still using only one instance 
              of the current number)
            - Next, rather than moving on to the next number in the array, which could be a duplicate of the current number, 
              we iterate through the array starting from the current index and break the loop if we find a number that is not equal to the current number then we move to that number.
        - The rest is the same as Combination Sum
        
'''