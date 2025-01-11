'''
Detect Squares
Difficulty: Medium

You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

    Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as different points.
    Query - Given a single query point, count the number of ways to choose three additional points from the data structure such that the three points and the query point form a square. 
            The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.
            
Implement the CountSquares class:

    CountSquares() Initializes the object with an empty data structure.
    void add(int[] point) Adds a new point point = [x, y] to the data structure.
    int count(int[] point) Counts the number of ways to form a square with point = [x, y] as described above.
    
Example 1:

    Input: 
    ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]

    Output:
    [null, null, null, null, 1, 0, null, 2]

    Explanation:
    CountSquares countSquares = new CountSquares();
    countSquares.add([1, 1]);
    countSquares.add([2, 2]);
    countSquares.add([1, 2]);

    countSquares.count([2, 1]);   // return 1.
    countSquares.count([3, 3]);   // return 0.
    countSquares.add([2, 2]);     // Duplicate points are allowed.
    countSquares.count([2, 1]);   // return 2. 

'''

from collections import defaultdict
from typing import List

class CountSquares:
    
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.points = []
        
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.ptsCount[tuple(point)] += 1 # Increment the count of the point in the dictionary
        
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y: # Not a diagonal point
                continue
            res += (self.ptsCount[(px, y)] * self.ptsCount[(x, py)]) # Add the product of the count of the two points which would be on the "other" corners of the square
            
        return res

if __name__ == "__main__":
    countSquares = CountSquares()
    countSquares.add([1, 1])
    countSquares.add([2, 2])
    countSquares.add([1, 2])
    print(countSquares.count([2, 1]))   # return 1.
    print(countSquares.count([3, 3]))   # return 0.
    countSquares.add([2, 2])     # Duplicate points are allowed.
    print(countSquares.count([2, 1]))   # return 2.
    
'''
Notes:

    Time complexity: O(1) for add and O(n) for count
    Space complexity: O(n)
    
    Short explanation:
        - Every time we add a point, we increment the count of that point in the dictionary and add the point to the list of points.
        - For every count() call, we iterate through the list of points, only considering points that are in a diagonal (equal difference in x and y) position.
            - This is because these are the most important points to consider when forming a square.
        - We then add the product of the count of the two points which would be on the "other" corners of the square to account for all combinations of squares that can be formed.
        - Furthermore, this accounts for multiple diagonal points that can be used to form a square because we are iterating through self.points, which contains all of them.
        
'''