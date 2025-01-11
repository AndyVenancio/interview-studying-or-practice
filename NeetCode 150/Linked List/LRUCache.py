'''
LRU Cache
Difficulty: Medium

Implement the Least Recently Used (LRU) Cache class LRUCache. The class should support the following operations:

    - LRUCache(int capacity) Initialize the LRU cache of size capacity.
    - int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
      If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
      
A key is considered used if a get or a put operation is called on it.
Ensure that get and put each run in O(1) average time complexity.

Example 1:
    Input:
    ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

    Output:
    [null, null, 10, null, null, 20, -1]

    Explanation:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 10);  // cache: {1=10}
    lRUCache.get(1);      // return 10
    lRUCache.put(2, 20);  // cache: {1=10, 2=20}
    lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
    lRUCache.get(2);      // returns 20 
    lRUCache.get(1);      // return -1 (not found)

'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap  = capacity
        self.cache = {}
        
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
         
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        # print(self.cache)
            
            
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 10)
    print(lRUCache.get(1))
    lRUCache.put(2, 20)
    lRUCache.put(3, 30)
    print(lRUCache.get(2))
    print(lRUCache.get(1))


'''
Notes:

    Time complexity: O(1) for both get and put operations
    Space complexity: O(capacity) for the cache
    
    Short explanation:
        - We use a doubly linked list to keep track of the order of the keys
        - We use a dictionary to store the key-value pairs
        - Initially, we have two dummy nodes, left and right to keep track of the head and tail of the linked list
        - The left node is the least recently used node and the right node is the most recently used node
        - Other than that, the rest is just LRU cache implementation
        
'''