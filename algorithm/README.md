
# **Data Structure Algorithms (A to Z)**

### 1. **ARRAY**

#### **Insert into Array**
1. Start
2. Check if array is full
3. Read position (pos) and value (val)
4. Shift elements from pos to end
5. Place value `array[pos] = val`
6. Increase array size
7. Stop

#### **Delete from Array**
1. Start
2. Read position (pos) to delete
3. Shift elements from pos+1 to end
4. Decrease array size
5. Stop

#### **Linear Search**
1. Start
2. Set `i = 0`
3. While `i < size`:
   - If `array[i] == val`, return "Found"
   - Else, increase `i` by 1
4. If not found, return "Not Found"
5. Stop

#### **Bubble Sort**
1. Start
2. For `i = 0` to `n-1`:
   - For `j = 0` to `n-i-1`:
     - If `array[j] > array[j+1]`, swap `array[j]` and `array[j+1]`
3. Stop

---

### 2. **STACK (LIFO)**

#### **Push (Insert)**
1. Start
2. Check if stack is full
3. Increase `top` by 1
4. Set `stack[top] = val`
5. Stop

#### **Pop (Delete)**
1. Start
2. Check if stack is empty
3. Return value at `stack[top]`
4. Decrease `top` by 1
5. Stop

#### **Peek (Top)**
1. Start
2. Return value at `stack[top]`
3. Stop

---

### 3. **QUEUE (FIFO)**

#### **Enqueue (Insert)**
1. Start
2. Check if queue is full
3. Increase `rear` by 1
4. Set `queue[rear] = val`
5. Stop

#### **Dequeue (Delete)**
1. Start
2. Check if queue is empty
3. Return value from `queue[front]`
4. Increase `front` by 1
5. Stop

---

### 4. **LINKED LIST**

#### **Insert at Beginning**
1. Start
2. Create a new node
3. Set new node’s `next` to `head`
4. Set `head = new node`
5. Stop

#### **Insert at End**
1. Start
2. Create a new node
3. Traverse the list to find last node
4. Set `last node->next = new node`
5. Stop

#### **Delete First Node**
1. Start
2. Set `temp = head`
3. Set `head = head->next`
4. Delete `temp`
5. Stop

#### **Delete Last Node**
1. Start
2. Traverse to second last node
3. Set `second last node->next = NULL`
4. Delete last node
5. Stop

---

### 5. **TREE**

#### **Inorder Traversal (Left, Root, Right)**
1. Start
2. Traverse left subtree
3. Visit root node
4. Traverse right subtree
5. Stop

#### **Preorder Traversal (Root, Left, Right)**
1. Start
2. Visit root node
3. Traverse left subtree
4. Traverse right subtree
5. Stop

#### **Postorder Traversal (Left, Right, Root)**
1. Start
2. Traverse left subtree
3. Traverse right subtree
4. Visit root node
5. Stop

---

### 6. **GRAPH**

#### **Breadth First Search (BFS)**
1. Start
2. Enqueue the starting node
3. While the queue is not empty:
   - Dequeue a node
   - Visit all its neighbors, enqueue them if not visited
4. Stop

#### **Depth First Search (DFS)**
1. Start
2. Visit the node and mark it visited
3. For each unvisited neighbor, repeat DFS
4. Stop

---

### 7. **HEAP**

#### **Insert into Max Heap**
1. Start
2. Add the value at the end of the heap
3. Compare with parent node, if value is larger, swap
4. Repeat the comparison up to the root
5. Stop

#### **Delete Root from Max Heap**
1. Start
2. Replace root with the last element
3. Compare with larger child, if needed, swap
4. Repeat the process until the heap property is restored
5. Stop

---

### 8. **HASHING**

#### **Insert into Hash Table**
1. Start
2. Use the hash function to compute the index
3. If the slot is empty, insert the value
4. If there’s a collision, resolve it (using linear probing, chaining, etc.)
5. Stop

---

Sure, Aadil! Here's an expanded version with more algorithms like **Dijkstra's Shortest Path**, **Quick Sort**, **Merge Sort**, and more. This will give you the complete set of algorithms that a CS student needs in a simple, exam-style format.

---

### 9. **DIJKSTRA’S ALGORITHM (Shortest Path)**

#### **Algorithm: Dijkstra’s Shortest Path**
1. Start
2. Initialize the source node’s distance as 0, all other nodes as infinity.
3. Set all nodes as unvisited.
4. While there are unvisited nodes:
   - Pick the unvisited node with the smallest distance.
   - Update the distance of its neighbors.
   - Mark the node as visited.
5. Stop

---

### 10. **QUICK SORT**

#### **Algorithm: Quick Sort**
1. Start
2. Choose a pivot element from the array.
3. Partition the array such that:
   - All elements less than the pivot are on the left.
   - All elements greater than the pivot are on the right.
4. Recursively apply the same procedure to the left and right partitions.
5. Stop

---

### 11. **MERGE SORT**

#### **Algorithm: Merge Sort**
1. Start
2. Divide the array into two halves.
3. Recursively sort both halves.
4. Merge the two sorted halves back together.
5. Stop

---

### 12. **BINARY SEARCH**

#### **Algorithm: Binary Search (on Sorted Array)**
1. Start
2. Set `low = 0`, `high = size - 1`.
3. While `low <= high`:
   - Find middle index: `mid = (low + high) / 2`
   - If `array[mid] == val`, return "Found".
   - If `array[mid] < val`, set `low = mid + 1`.
   - If `array[mid] > val`, set `high = mid - 1`.
4. Return "Not Found" if the element doesn't exist.
5. Stop

---

### 13. **FLOOD FILL (used in image processing)**

#### **Algorithm: Flood Fill**
1. Start
2. If the current pixel is the same as the target, change the color to the new color.
3. Recursively check the adjacent pixels (up, down, left, right).
4. Stop when all the connected pixels are filled with the new color.

---

### 14. **AVL TREE (Self-Balancing Binary Search Tree)**

#### **Algorithm: Insert in AVL Tree**
1. Start
2. Insert the node as in a regular binary search tree.
3. Check balance factor (left height - right height) of all ancestors.
4. If balance factor > 1, perform rotations:
   - Left-Left (LL): Perform right rotation.
   - Right-Right (RR): Perform left rotation.
   - Left-Right (LR): Perform left rotation, followed by right rotation.
   - Right-Left (RL): Perform right rotation, followed by left rotation.
5. Stop

---

### 15. **TRIE (Prefix Tree)**

#### **Algorithm: Insert in Trie**
1. Start
2. For each character of the word:
   - Check if the character node exists.
   - If not, create a new node for the character.
   - Move to the next character node.
3. Mark the last node as the end of the word.
4. Stop

---

### 16. **KMP ALGORITHM (Pattern Matching)**

#### **Algorithm: KMP Pattern Matching**
1. Start
2. Preprocess the pattern to create the Longest Prefix Suffix (LPS) array.
3. Traverse the text and pattern:
   - If characters match, move to the next character in both text and pattern.
   - If characters don’t match, use the LPS array to skip unnecessary checks.
4. Stop

---

### 17. **BFS (Breadth First Search)**

#### **Algorithm: BFS (Breadth First Search)**
1. Start
2. Mark the starting node as visited.
3. Enqueue the starting node.
4. While the queue is not empty:
   - Dequeue a node, visit it, and enqueue all its unvisited neighbors.
5. Stop

---

### 18. **DFS (Depth First Search)**

#### **Algorithm: DFS (Depth First Search)**
1. Start
2. Mark the starting node as visited.
3. For each unvisited neighbor, recursively visit them.
4. Stop

---

### 19. **Kruskal’s Algorithm (MST - Minimum Spanning Tree)**

#### **Algorithm: Kruskal’s Algorithm**
1. Start
2. Sort all the edges in non-decreasing order of weight.
3. Initialize the forest where each vertex is a separate tree.
4. For each edge, if it doesn’t form a cycle, add it to the MST.
5. Stop when all vertices are connected.

---

### 20. **PRIM’S ALGORITHM (MST - Minimum Spanning Tree)**

#### **Algorithm: Prim’s Algorithm**
1. Start
2. Choose an arbitrary node and mark it as visited.
3. Add the smallest edge to the MST, connecting a visited node to an unvisited node.
4. Repeat until all nodes are visited.
5. Stop

---

### 21. **SHA (Hashing Algorithm)**

#### **Algorithm: SHA (Secure Hashing Algorithm)**
1. Start
2. Break the input message into blocks.
3. Process each block with a hash function (like SHA-256).
4. Combine the results to generate the final hash value.
5. Stop

---

### 22. **SIEVE OF ERATOSTHENES (Finding Prime Numbers)**

#### **Algorithm: Sieve of Eratosthenes**
1. Start
2. Create a boolean array of size `n+1`, initialize all entries as true.
3. For each number `p` from 2 to √n:
   - If `p` is prime, mark all multiples of `p` as false.
4. The remaining true numbers are primes.
5. Stop

---

### 23. **HEAP SORT**

#### **Algorithm: Heap Sort**
1. Start
2. Build a max-heap from the array.
3. Swap the root of the heap with the last element of the array.
4. Reduce the heap size by 1.
5. Heapify the root node to restore the heap property.
6. Repeat until the heap size is 1.
7. Stop

---

### 24. **COUNTING SORT**

#### **Algorithm: Counting Sort**
1. Start
2. Create a count array to store the frequency of each element.
3. For each element in the input array, increment its count.
4. Compute the cumulative sum in the count array.
5. Place elements in the output array based on the cumulative count.
6. Stop

---

