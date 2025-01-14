'''
Kth Largest Element in a Stream
Difficulty: Easy

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

    constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
    int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
    
Example 1:

    Input:
    ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

    Output:
    [null, 3, 3, 3, 5, 6]

    Explanation:
    KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
    kthLargest.add(3);   // return 3
    kthLargest.add(5);   // return 3
    kthLargest.add(6);   // return 3
    kthLargest.add(7);   // return 5
    kthLargest.add(8);   // return 6

'''

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # If the length of the heap is bigger than k, pop the smallest element.
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
if __name__ == "__main__":
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))   # return 3
    print(kthLargest.add(5))   # return 3
    print(kthLargest.add(6))   # return 3
    print(kthLargest.add(7))   # return 5
    print(kthLargest.add(8))   # return 6
    
    
'''
Notes:

    Time Complexity: O(m * log(k)) where m is the number of elements in the stream and k is the value of k.
    Space Complexity: O(k)
    
    Short Explanation:
        - We initialize the minHeap with the first k elements of the stream.
            - Since heappop() pops the smallest element, we have to do this until it removes all the elements that are smaller than the kth largest element. (while len(self.minHeap) > k)
        - When adding a new element:
            - We push the element to the heap.
            - Since we consider the kth largest element the smallest element in the heap, the length of the heap being bigger than k means the new element is smaller than the kth largest element.
            - Therefore, we pop the smallest element in the heap.
            - Otherwise, we return the smallest element in the heap.
            
'''
