'''
Last Stone Weight
Difficulty: Easy

You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

    Input: stones = [2,3,6,2,4]
    Output: 1
    
Example 2:

    Input: stones = [1,2]
    Output: 1

'''

import heapq

from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)
    
    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        
        result = abs(y - x)
        
        if result != 0:
            heapq.heappush(stones, -1 * result)
            
    return -1 * stones[0] if len(stones) == 1 else 0


stones1 = [2,3,6,2,4]
stones2 = [1,2]

print(lastStoneWeight(stones1))
print(lastStoneWeight(stones2))

'''
Notes:

    Time Complexity: O(n * log(n)) where n is the number of elements in the stones array.
    Space Complexity: O(n)
    
    Short Explanation:
        - Since we have to use minHeap, we will multiply all the elements by -1 to use it as maxHeap.
        - The rest of the solution is straightforward. We will pop the two heaviest stones and push the result back to the heap if it is not 0.
        - Return the last element in the heap times -1 (to get the original value) if there is only one element left, otherwise return 0.
        
'''
    