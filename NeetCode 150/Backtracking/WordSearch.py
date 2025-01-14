'''
Word Search
Difficulty: Medium

Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

    Input: 
        board = [
          ["A","B","C","D"],
          ["S","A","A","T"],
          ["A","C","A","E"]
        ],
        word = "CAT"
    Output: true
    
Example 2:

    Input: 
        board = [
          ["A","B","C","D"],
          ["S","A","A","T"],
          ["A","C","A","E"]
        ],
        word = "BAT"
    Output: false

'''

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if (min(r, c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
            return False
        
        path.add((r, c))
        # print(path)
        res = (dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1))
        path.remove((r, c))
        
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False



'''
This is my original solution which works also.
There is nothing wrong with this solution but it is important to remember that it originally did not work because I forgot
to pop the visited cell from the visited list after the recursive call. This caused the visited list to grow indefinitely
blocking further recursive calls. This is why it is important to remember to pop the visited cell after the recursive call
to avoid this issue. 

It is better to use the other solution because it is more efficient.
'''

# def exist(board: List[List[str]], word: str) -> bool:
#     ROWS, COLS = len(board), len(board[0])
#     
#     def dfs(r, c, string, visited):
#         print(string)
#         if word in string:
#             return True
#         
#         if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or len(string) >= len(word)):
#             return False
#         
#         visited.append((r, c))
#         string += board[r][c]
#         res = (dfs(r + 1, c, string, visited) or dfs(r, c + 1, string, visited) or dfs(r - 1, c, string, visited) or dfs(r, c - 1, string, visited))
#         visited.pop()
#         
#         return res
#     
#     for r in range(ROWS):
#         for c in range(COLS):
#             if dfs(r, c, "", []):
#                 return True
#     return False
        
  
  
board1 = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word1 = "CAT" 

board2 = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word2 = "BAT"

board3 =[["A","B","C","E"],
       ["S","F","C","S"],
       ["A","D","E","E"]
       ]
word3 ="ABCCED"
  

print(exist(board1, word1))
print(exist(board2, word2))
print(exist(board3, word3))

'''
Notes:

    Time Complexity: O(m * 4^n) where m is the number of cells in the board and n is the length of the word
    Space Complexity: O(n)
    
    Short Explanation:
        - Similar to other backtracking problems, we will use a recursive function to explore all possible paths
        - We will keep track of the cells we have visited so far to avoid using the same cell more than once
        - We will search from each cell individually since starting only from the first cell only considers possible substrings where the first letter is the first letter of the board
        - For every iteration of dfs():
            - If the index of the word is equal to the length of the word, we have found the word and return True
            - If the current cell is out of bounds, the letter does not match the current letter in the word, or the cell has already been visited, we return False
        - We add the current cell to the path set and recursively call dfs() on the neighboring cells, left, right, up, and down
        - If any of the recursive calls return True, we return True
        - If we have explored all possible paths and have not found the word, we return False
        
'''