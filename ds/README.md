

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
  - Here, there is a directed edge from A to B with a cost of 10, and from B to C with a cost of 15, but not vice versa, proving the matrix is asymmetric.

**Q3. Mr. Arif's Solution to the Challenge**  
- **Description**: Mr. Arif was tasked with creating a Binary Search Tree (BST) using distinct integer numbers. A BST is a tree data structure where each node has at most two children, and for any given node, the left child's value is less than the parent's value, while the right child's value is greater. Mr. Arif started by inserting the numbers one by one. For example, if he first inserted 26, it became the root. When he inserted 52, it went to the right of 26, and when he inserted 20, it went to the left of 26. This structure allows for efficient searching, as he can quickly decide to go left or right based on the value he is looking for.

- **Code Example**:
    ```cpp
    struct TreeNode {
        int value;
        TreeNode* left;
        TreeNode* right;
    };

    TreeNode* insert(TreeNode* root, int value) {
        if (root == nullptr) {
            TreeNode* newNode = new TreeNode();
            newNode->value = value;
            newNode->left = newNode->right = nullptr;
            return newNode;
        }
        if (value < root->value) {
            root->left = insert(root->left, value); // Insert in the left subtree
        } else {
            root->right = insert(root->right, value); // Insert in the right subtree
        }
        return root;
    }
    ```

**Q4. Mr. Arif Helping Mr. Habib**  
- **Explanation**: Mr. Habib had trouble finding his Student ID in his BST. Mr. Arif helped him by explaining the binary search process. He told Mr. Habib to start at the root and compare his Student ID with the value of the current node. If the Student ID was less than the current node's value, they would move to the left child; if it was greater, they would move to the right child. Mr. Arif demonstrated this process step-by-step, showing how to navigate through the tree until they either found the Student ID or reached a leaf node (indicating that the ID was not present). This method is efficient because it reduces the search space by half with each comparison.

- **Code Example**:
    ```cpp
    bool search(TreeNode* root, int value) {
        if (root == nullptr) {
            return false; // Value not found
        }
        if (root->value == value) {
            return true; // Value found
        }
        if (value < root->value) {
            return search(root->left, value); // Search in the left subtree
        } else {
            return search(root->right, value); // Search in the right subtree
        }
    }
    ```

---

#### **Task-2**

**Q5. Minimum Travel Cost from DIU to X**  
- **Calculation**: To find the minimum travel cost from Daffodil International University (DIU) to location X, we first need to calculate X using the formula: \( X = (last \, two \, digits \, of \, your \, student \, ID \% 6) + 1 \). For example, if the last two digits of your Student ID are 42, then \( X = (42 \% 6) + 1 = 0 + 1 = 1 \). Next, we look at the graph to see how much it costs to travel to vertex 1 from DIU. If the costs to the places connected to DIU are 10, 15, and 20, the minimum cost would be 10. This helps in planning the best route to take.

- **Example**: If the graph shows the following costs:
    - DIU to A: 10
    - DIU to B: 15
    - DIU to C: 20
  The minimum travel cost to X (vertex 1) would be 10.

**Q6. Determining the Chromatic Number**  
- **Explanation**: The chromatic number of a graph is the smallest number of colors needed to color the vertices so that no two adjacent vertices share the same color. To find this number, we can start coloring the graph. For example, we can color the first vertex with color 1. Then, we color the adjacent vertices with color 2. We keep doing this until all vertices are colored. If we can do it with just two colors, then the chromatic number is 2. This is important for problems like scheduling, where we want to avoid conflicts.

- **Example**: If we have a graph with three vertices connected in a triangle, we would need three colors to color them so that no two adjacent vertices have the same color. Thus, the chromatic number would be 3.

**Q7. Mr. Tamim's Solutions to QA and QB**  
- **QA**: 
  - **Pseudocode to Delete ‘XX’**: 
    ```
    function deleteNode(head, value):
        if head is None:
            return head
        if head.value == value:
            return head.next
        current = head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return head
            current = current.next
        return head
    ```
  - **Explanation**: This pseudocode shows how to delete a node with a specific value from a linked list. It first checks if the list is empty. If the first node has the value we want to delete, it just returns the next node as the new head. If not, it goes through the list to find the node with the value. When it finds it, it skips that node by changing the pointer, effectively removing it from the list.

- **QB**: 
  - **Explanation**: Yes, we can display the elements of a singly linked list in reverse order. One way to do this is by using a stack. We can go through the linked list and push each element onto the stack. When we pop elements from the stack, they come out in reverse order. Another way is to use recursion. We can call a function for the next node before printing the current node’s value. This way, the last node gets printed first, achieving the reverse order.

- **Code Example for Reversing a Linked List**:
    ```cpp
    void printReverse(Song* head) {
        if (head == nullptr) return; // Base case
        printReverse(head->next); // Recursive call
        std::cout << head->title << std::endl; // Print the current song after returning
    }
    ```


