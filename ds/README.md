

### **Theory Part (Marks - 35)**

#### **Task-1**

**Q1. Data Structures Used by Mr. Sisir and Mr. Tusher**  
- **Mr. Sisir**: 
  - **Data Structure**: **Array**
  - **Explanation**: Mr. Sisir is developing an online ticket booking system. He uses an array to store information about the tickets. An array is a collection of elements stored at contiguous memory locations. This structure allows for efficient access to elements using an index. For example, if he has 100 seats, he can represent them in an array where each index corresponds to a seat number. If he wants to check if seat number 5 is booked, he can simply access `array[4]` (since arrays are zero-indexed) to get the status of that seat. This makes operations like checking availability very fast (O(1) time complexity). However, arrays have limitations, such as a fixed size. If Mr. Sisir needs to add more seats, he would have to create a new larger array and copy the existing data, which can be inefficient.



- **Mr. Tusher**: 
  - **Data Structure**: **Linked List**
  - **Explanation**: Mr. Tusher is creating a music playlist application. He uses a linked list for this purpose. A linked list consists of nodes where each node contains data and a pointer to the next node. This structure allows for dynamic memory allocation, meaning that the size of the playlist can change as songs are added or removed. For instance, if a user wants to add a new song, Mr. Tusher can create a new node and link it to the existing list without needing to resize an array. This makes it easy to insert or delete songs from any position in the playlist.


**Q2. Proving the Adjacency Matrix is Asymmetric**  
- **Explanation**: An adjacency matrix is a square matrix used to represent a graph. Each cell in the matrix indicates whether pairs of vertices are adjacent or not. For a directed graph, the matrix is asymmetric if the connection from vertex A to vertex B does not imply a connection from vertex B to vertex A. For example, if the cost of traveling from vertex A to vertex B is 10, but the cost from B to A is 15, the matrix will show different values at positions (A, B) and (B, A). This property is important in applications like route planning, where the cost of travel may differ based on direction.

- **Example**:
  - Consider a graph with vertices A, B, and C. The adjacency matrix might look like this:
    ```
          A   B   C
        A  0   10  0
        B  0   0   15
        C  5   0   0
    ```


---

### Q3. How does Mr. Arif solve the challenge provided by the course instructor? A detailed description is needed.

To solve the challenge, Mr. Arif follows these steps:

1. **Understanding the Constraints**: The first step for Mr. Arif is to understand the constraints provided by the instructor. He needs to select 10 distinct integers between 20 and 200, where:
   - The first number is always 26.
   - The fourth number is calculated as XX, based on his Student ID (last two digits of Student ID % 10 + the lowest number selected).
   - The seventh number is 86.
   - The ninth number is 52.
   - There are two numbers less than 35.
   - No more than four numbers exceed 110.

2. **Selecting the Numbers**: Mr. Arif selects the 10 distinct numbers based on the given constraints. He ensures that two numbers are less than 35, and no more than four numbers exceed 110. He also calculates XX based on his Student ID, which gives him the fourth number.

3. **Building the Binary Search Tree (BST)**: After selecting the numbers, Mr. Arif builds the BST. He starts by inserting 26 as the root, then inserts each subsequent number by comparing it to the current node and placing it either to the left (if smaller) or to the right (if larger). This process continues until all the numbers are inserted into the BST.

4. **Using Binary Search to Find the Student ID**: Once the BST is built, Mr. Arif can use binary search to find his Student ID. He starts at the root and compares the current node with XX (his Student ID). If XX is smaller, he moves to the left child; if it’s larger, he moves to the right child. This process is repeated until he finds the correct node.

By following these steps, Mr. Arif solves the challenge efficiently and finds his Student ID in the BST using binary search.

---

### Q4. How did Mr. Arif solve the difficulties faced by Mr. Habib? Describe with proper explanation.

Mr. Habib successfully built the BST, but he faced difficulties finding his Student ID using binary search. The possible reasons for this are:

1. **Incorrect Calculation of XX**: Mr. Habib may have miscalculated XX, which is based on the last two digits of his Student ID. If this calculation was wrong, the BST structure would be incorrect, making it hard to find his Student ID.

2. **Incorrect Tree Structure**: Mr. Habib might have built the tree incorrectly. If the numbers were not inserted properly (for example, not following the BST property), the tree structure could be invalid, and binary search would not work.

3. **Incorrect Binary Search**: Mr. Habib might not have applied binary search properly. For example, he might not have compared the current node with the target (Student ID) and navigated left or right accordingly.

Mr. Arif, having successfully solved the problem, helped Mr. Habib by:

1. **Correcting the Calculation of XX**: Mr. Arif explained the correct way to calculate XX using the last two digits of Mr. Habib's Student ID, ensuring that the number was calculated accurately.

2. **Fixing the Tree Structure**: If Mr. Habib's tree was incorrectly built, Mr. Arif would have guided him in rebuilding the tree, ensuring that the BST property was followed (left child smaller, right child larger).

3. **Guiding on Binary Search**: Mr. Arif would have explained the steps of binary search clearly, making sure Mr. Habib understood how to compare the current node with the Student ID and navigate left or right accordingly.

By helping Mr. Habib with these steps, Mr. Arif ensured that the BST was correct and binary search was applied successfully to find the Student ID.

--- 

#### **Task-2**


---

### ✅ **Q5. Find out the minimum travel cost from DIU to X of Figure 01 that is made by Mr. Mehedi.**  
**[X = (Last two digits of your Student ID % 6) + 1]**  
**Student ID Assumed: 25**

---

### **Step 1: Determine Destination Node (X)**  
According to the given formula:  
\[
X = (25 \mod 6) + 1 = 1 + 1 = 2
\]  
Hence, the destination node is **Node 2**, which represents **Sajek Valley**.

---

### **Step 2: Applying Dijkstra’s Algorithm to Find Minimum Cost**

We use **Dijkstra's Algorithm** to calculate the shortest path from the source node (DIU = Node 7) to all other nodes. The graph is weighted and directed, representing travel costs between historical sites.

---

### **Output (Minimum Distance from Node 7 to All Other Nodes):**  
```
From Node 7:
To Node 1 = 50      Path: 7 → 5 → 1  
To Node 2 = 40      Path: 7 → 6 → 2  
To Node 3 = 53      Path: 7 → 6 → 2 → 3  
To Node 4 = 58      Path: 7 → 6 → 5 → 4  
To Node 5 = 26      Path: 7 → 6 → 5  
To Node 6 = 15      Path: 7 → 6  
```

---

### **Final Answer:**
✅ **The minimum travel cost from DIU (Node 7) to Sajek Valley (Node 2) is 40 units.**  
➡ **Shortest Path:** 7 → 6 → 2

---


**Q6. Determining the Chromatic Number**  
To determine the **chromatic number** of the given directed graph, we need to find the **minimum number of colors** required to color the vertices such that no two adjacent vertices share the same color. Let's go step by step to understand how to calculate it.  

---

### **Step 1: Understanding the Graph**  
Looking at **Figure 01**, we can see that the graph represents **historical places as vertices** and **travel costs as weighted edges** between them. The presence of an edge between two vertices means that these locations are directly connected.  

Since every vertex in the graph has direct edges to multiple other vertices, it is important to analyze the structure to determine the chromatic number correctly.  

---

### **Step 2: Identifying the Graph Type**  
From observation, we notice that:  
- Every vertex is connected to multiple other vertices.  
- The graph appears to be **fully connected**, meaning each vertex has edges connecting it to every other vertex.  
- A fully connected graph with \( n \) vertices is called a **complete graph** and is denoted as \( K_n \).  

To confirm, let's count the number of vertices and check their connections:  
- The graph has **7 vertices** (representing historical places).  
- Each vertex is directly connected to the other 6 vertices, meaning **every vertex shares an edge with all others**.  

Since each vertex is connected to all others, this is a **complete graph** \( K_7 \).  

---

### **Step 3: Chromatic Number of a Complete Graph**  
For a **complete graph \( K_n \)**, the chromatic number is always equal to the number of vertices. This is because:  
- Every vertex is adjacent to every other vertex.  
- Since adjacent vertices **must** have different colors, each vertex must be assigned a unique color.  

Thus, for \( K_7 \), the chromatic number is:  
\[
\chi(K_7) = 7
\]  
This means we need **7 different colors** to properly color this graph while ensuring that no two adjacent vertices have the same color.  

---

### **Step 4: Conclusion**  
Since the given graph is a complete graph with 7 vertices, the **minimum number of colors required (chromatic number) is 7**.  

**Final Answer:**  
**The chromatic number of Figure 01 is 7, meaning we need 7 different colors to color the vertices correctly.**

### **Q7: How Did Mr. Tamim Solve QA and QB?**  

#### **QA Solution by Mr. Tamim (Deleting ‘XX’ from the Linked List)**  
Mr. Tamim approached the problem systematically by following the standard deletion procedure for a singly linked list:  

1. **Check if the list is empty**: If the head of the linked list is `NULL`, no deletion is required.  
2. **Check if the first node (head) contains the target value**:  
   - If `head.data == 'XX'`, update the head to `head.next` to remove the first node.  
3. **Traverse the list to locate the node containing ‘XX’**:  
   - Maintain a `current` pointer starting from the head.  
   - If `current.next.data == 'XX'`, update `current.next` to `current.next.next`, effectively bypassing the target node.  
4. **Stop the traversal** after the deletion to avoid unnecessary iterations.  
5. **Edge Cases Considered**:  
   - The node may not exist → No action is needed.  
   - The node may be at the end → Adjust the last node’s pointer to `NULL`.  

- **Final Pseudocode Used by Mr. Tamim**:  
    ```
    function deleteNode(head, value):
        if head is NULL:
            return head
        if head.data == value:
            return head.next
        current ← head
        while current.next ≠ NULL:
            if current.next.data == value:
                current.next ← current.next.next
                return head
            current ← current.next
        return head
    ```

#### **QB Solution by Mr. Tamim (Reversing the Display Order of a Singly Linked List)**  
Mr. Tamim correctly identified that **a singly linked list does not support backward traversal**, meaning the list’s structure cannot be modified for reverse printing. However, he provided **two valid solutions**:

1. **Using a Stack (Iterative Approach)**:  
   - Traverse the list and store each node’s data in a **stack**.  
   - Since stacks follow the **Last In, First Out (LIFO)** principle, popping the elements results in a **reverse order**.  

   **Pseudocode for Stack-Based Reversal**:  
    ```
    function printReverseUsingStack(head):
        stack ← empty
        current ← head
        while current ≠ NULL:
            push(stack, current.data)
            current ← current.next
        while stack is not empty:
            print pop(stack)
    ```

2. **Using Recursion (Recursive Approach)**:  
   - **Recursively traverse** the list until the last node.  
   - As the function **returns**, print each node’s data, ensuring a **reverse display**.  

   **Pseudocode for Recursive Reverse Printing**:  
    ```
    function printReverse(node):
        if node is NULL:
            return
        printReverse(node.next)
        print node.data
    ```

#### **Why Mr. Tamim’s Approach is Correct?**  
- He successfully deleted the node `'XX'` while **preserving the linked list structure**.  
- He correctly **identified** that singly linked lists do not have backward pointers.  
- He implemented **two efficient** solutions to print elements in reverse order.  
- His solutions were **optimal**:  
  - **Stack-based approach**: \(O(n)\) time and \(O(n)\) space.  
  - **Recursive approach**: \(O(n)\) time and \(O(n)\) space (due to recursive stack).  

Thus, Mr. Tamim demonstrated a **clear understanding of linked list operations**, solving both QA and QB efficiently. 🎯
