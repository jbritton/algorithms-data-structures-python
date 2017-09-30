
## Why use data structures?
* Data structures are used to store data in an efficient way
* Algorithms can be boosted up by proper data structures
* Data structure make sure the running time will be better

## Abstract data types
* Abstract data types define the basic behavior of a data structure
* An interface, does not define the concrete implementation or programming language
* Data structures are the concrete implementation, the actual representation of the data


## Arrays
* Advantages
    * Very fast access when index is known => O(1)
    * Easy to implement and use
    * Arrays should be used when items are added frequently and retrieved by index
* Disadvantages
    * Size of array must be known at compile time
    * When full, each item must be copied to the new bigger array => O(N)
    * It is not able to store items with different types
* Operations
    * append => O(1) when inserting items at the end of a list
    * insert => O(N) when inserting an item at an index, existing items after the insertion index may need to be shifted 
    * remove => O(1) when removing the last item, O(N) when removing at a specific index because items need to be shifted
    
## Linked Lists
* Overview
    * Linked lists are composed of nodes and references (pointers pointing from one node to another), the last reference is point to a null
    * As single node contains the data and a reference to the next node in the linked list
    * A simple and very common data structure, can be used to implement other common data structures (ie. stacks and queues)
    * Do not allow for random access (ie. getItem(int index) )
    * Basic operations such as obtaining the last node of the list or finding a node that contains a specific value require sequential scanning
    of most or all of the list elements
* Advantages
    * Linked lists are dynamic data structures (arrays are not) and can grow organically
    * Can allocate the needed memory in run-time
    * Very efficient if first elements need to be manipulated
    * Easy implementation
    * Can store elements with different sizes
* Disadvantages
    * Wastes memory due to references
    * Nodes must be read in order from the beginning (no random access)
    * It is difficult to traverse a linked list in reverse order
    * Double linked lists allow for easier backwards traversal but waste more memory due to references to previous nodes
* Operations
    * insertAtStart(value) => O(1) when inserting at the start of a list
    * insertAtEnd(value) => O(N) when inserting at the end, the entire list must be traversed to find the last node
    * removeAtStart() => O(1) when removing item at the start of a list
    * remove(value) => O(N) when removing a specific item, must traverse list items until it is found
    
## Arrays vs Linked Lists
* Search Operation
    * arrays are better when index is known O(1), linked lists do not use indexing and require traversal O(N)
    * arrays when index is unknown and linked lists are O(N) because the structure must be searched
* Delete Operation
    * linked lists are better when item is removed from the beginning O(1), arrays require shifting of items O(N)
    * arrays are better when item is removed from the end O(1), linked list O(N)
    * arrays generally need to be restructured when removing an item
    * linked lists are generally better for deletes - removal only requires change in reference pointer location which is fast
* Memory
    * Arrays do not require extra memory, Linked lists require extra memory to store reference pointers to next (and previous) items for each node
    

## Stacks
* Overview
    * Basic operations: pop(), push(), and peek()
    * LIFO structure: last in, first out
    * Used in graph algorithms like depth-first search and recursion, euler-cycles, etc.
    * Most important application of stacks: stack memory 
* Operations
    * push(value) => O(1) when pushing a value onto the stack
    * pop() => O(1) when popping a value off the stack
    * peek() => O(1) when peeking at the value at the top of the stack
* Stacks in memory management
    * Every time a function declares a new variable, it is pushed onto the stack
    * When a function exits, the local variables created by that function are popped off
    * Stack memory is limited
* Heap memory
    * Large region of memory
    * Java: reference types and objects are on the heap
    * Memory chunks must be deallocated manually because it is not managed automatically, if not => memory leak!

    
## Stack vs Heap Memory    
|   Stack Memory            |   Heap Memory         |
-----------------------------------------------------
| Limited in size           |  No size limits       |
-----------------------------------------------------
| Fast access               |  Slow access          |
-----------------------------------------------------
| Local variables           |  Objects              |
-----------------------------------------------------
| Space managed by CPU      |  Memory fragmented    |
-----------------------------------------------------
| Variables not resizable   |  Variables resizable  |
-----------------------------------------------------
    

## Queues
* Overview
    * FIFO structure: first in first out
    * Can be implemented with dynamic arrays as well as with linked lists
    * Important when implementing BFS algorithm for graphs
* Operations
    * enqueue(value) => O(1), adds an item to the end
    * dequeue() => O(N), removes an item from the beginning
    * peek() => O(1)?, gets an item from the beginning without removing it
* Applications
    * Resources shared among multiple consumers (ie. CPU scheduling)
    * Asynchronous data transfer between processes where data is not received as fast as it is sent (ie. IO buffers)
    
    
## Trees
* Overview
    * Consist of node with data and connections (edges) between the nodes
    * Root node - all other nodes are connected directly or indirectly
    * There must be only one path from a root node to any other node (otherwise it is not a tree)
    
    
## Binary Search Trees
* Overview
    * Every node can only have 2 children: left and right child
        * Left child - smaller than the parent
        * Right child - larger than the parent
    * Tree height is the number of layers it contains or number of paths from the root to the deepest node
        * ex. Tree contains 2^h-1 nodes (ie. 4 layers => 2^4-1 => 2x2x2 => 8 nodes)
    * Lookup/insertion/deletions takes time proportional to the logarithm of the number of items stored in the tree
    * If tree is balanced, the operations running time is O(logN)        
    * If a tree is unbalanced, the operations running time is no longer logarithmic, at worst it's linear O(N)        
* Advantages
    * Every decision eliminates half of the comparisons that needs to be performed (much like a binary search) => O(logN)
* Operations
    * Insertion - start at the root node, if smaller => go left, if larger => go right, continue on subsequent nodes until null is encountered
    * Search - start at the root, if smaller => go left, if larger => go right, continue until node is found
        * Find smallest node - go to the far left of the tree
        * Find largest node - go to the far right of the tree
    * Deletion
        * Node is a leaf - find the node => O(logN), set the parent's pointer to the node to null => O(1)
        * Node is a branch with a single child - find the node => O(logN), set parent's pointer to point to the grandchild directly => O(1)
        * Node is a branch with two child nodes 
            * Find the node => O(logN)
            * Either find the largest node in the node's left subtree (predecessor) or the smallest node in the right subtree (successor)
            and swap it with the deleted node => O(logN)
            * Update the references => O(1)
    * Traversal
        * In-order traversal - visit the left subtree, then the root node, then the right subtree recursively
        * Pre-order traversal - visit the root, then the left subtree, then the right subtree recursively
        * Post-order traversal - visit the left subtree, then the right subtree, then the root node recursively
                

## AVL - Balanced Binary Trees
* Overview
    * Guaranteed to be balanced, ensuring O(logN) performance for search, insertion, retrieval, etc.
    * Most of the operations are the same as binary search trees
    * Every node can have at most 2 children: left and right
    * Balancing of tree occurs on every insert
    * Height of the tree should be as small as possible, this ensures that is balanced
    * Height parameter of the left subtree and right subtree should not differ by more than one
* Height Parameter - distance from node to its deepest leaf node
    * Leaf node has a height of zero
    * Node w/ a leaf child has a height of 1
* Rotations
    * Doubly-left heavy situation => right rotation
    * Doubly-right heavy situation => left rotation
    * Left-right heavy situation => left rotation on lower subtree (to form double-left heavy), right rotation on root node
    * Right-left heavy situation => right rotation on lower subtree (to form double-right heavy), left rotation on root node
* Applications
    * Databases when deletions or insertions are not so frequent, but looks are frequent
    * Sort can be accomplished with help of AVL trees
    
    
## Red Black Trees    
* Overview
    * A balanced binary search tree with O(logN) performance
    * Not rigidly balanced => look ups are not as fast as AVL, but insertions/deletions are faster than AVL
    * Red-black properties
        * Each node is either red or black
        * Root node is always black
        * All leaves (NIL or NULL) are black
        * Every red node must have two black child nodes and no other children => it must have a black parent
        * Every path from a given node to any of its descendant NIL/NULL nodes contains the same number of black nodes            
    * AVL trees are faster than red-black trees because they are more rigidly balanced but require more work
    * Operating systems (Linux Kernel) rely heavily on these data structures
* Basics    
    * Every new node is red by default
    * Nodes are inserted in the same manner as other binary search trees
    * On every insertion, the tree must check that it doesn't violate red-black properties
    * Violations are rectified by either making rotations or re-coloring the nodes
* Rectifying violations
   * Recoloring may cause violations in other parts of the tree, requiring the check to be applied on the whole tree recursively
* Rotation Cases
    * Case 1: Recolor the nodes
    * Case 2: Left and right rotation on node's parent
    * Case 3: Make rotation on the node's grand parent, recolor nodes
    * Case 4:
* Implementations
    * Java: java.util.TreeMap, java.util.TreeSet
    * C++: map, multimap, multiset

    
## Priority Queues
* Overview
    * Abstract data type like stack or queue, except every item has a priority value
    * An element with a high priority is served before an element with a lower priority
    * They are typically implemented with heaps, but can be implemented with self balancing trees too
    * Very similar to queues with some modification => the highest priority element is retrieved first
    * No FIFO!
* Operations
    * insertWithPriority(data, priority) - inserts element w/ priority, sometimes priority is not specified
    * getHighestPriorityElement() - returns the element with the highest priority, reconstructs the data structure
    * peek() - returns the element with the highest priority, without altering the data structure
* Sorting
    * Insert elements to be sorted into a priority queue
    * Sequentially remove elements from their sorted order, highest priority elements are returned first


## Heaps
* Overview
    * It is basically a binary tree except the left child is not necessarily less than the right child
    * Two main binary heap types - min and max heaps:
        * Max heap - keys of parent nodes are always greater than or equal to those of the children => highest key is in the root node
        * Min heap - keys of parent nodes are always less than or equal to those of the children => lowest key is in the root node
    * It is complete: it cannot be unbalanced.  Every item is inserted into the next available space
    * Heap is one maximally efficient implementation of a priority queue abstract data type
    * It has nothing to do with the pool of memory from which dynamically allocated memory is allocated (ie. Not related to Java Heap)
* Applications
    * Dijkstra's algorithm
    * Prim's algorithm
* Properties
    * Complete - heap is constructed from left to right across each row, there is no missing node from left to right in a layer, last row might not be complete
    * Every node can have 2 children: left child and right child
    * Min heap: the parent is always smaller than the values of its children
    * Max heap: the parent is always greater than the values of its children
    * => O(1) access for max or min item in a max or min heap
* Array Indexing
    * i is the parent node of a subtree 
    * 2i + 1 is the index of its left child
    * 2i + 2 is the index of its right child
* Heapify - swap nodes in order to satisfy heap constraints
* Operations
    * Construct a heap => O(N)
    * Reconstruct a heap => O(logN)
    * Insertion - insert item at last position O(1), reconstruct heap O(logN) => O(logN)
    * Remove root node - remove root node O(1) + reconstruct heap O(logN) => O(logN)
    * Remove arbitrary node - find and remove arbitrary node O(N) + reconstruct heap O(logN) => O(N)
    * Find minimum (min heap) or maximum (max heap) => O(1) 
* Memory complexity - O(N), array containing N elements
* A node has at most log<sub>2</sub>N parents so it requires at most log<sub>2</sub>N swaps
    

## Heapsort
* Overview
    * Comparison-based sorting algorithm
    * Use head data structure rather than a linear-time search to find the maximum
    * An in-place algorithm, but it is not a stable sort
    * Does not require additional memory
    * Problem: first we need to construct a heap before sorting it => O(N)
    * A bit slower in practice than a well implemented quicksort, it has the advantage of a more favorable worse-case O(N logN)
* Speed of heap sort => O(N logN)


## Binomial Heap
* Similar to a binary heap but also supports quick merging of two heaps
* Mergeable Heap => Basically, this is a priority queue that supports the merge operation
* Insertion time O(logN) can be reduced to O(1) with the help of binomial heaps


## Fibonacci Heap
* Faster than the classic binary heap
* Dijkstra's shortest path and Prim's spanning tree algorithms run faster if they rely on it instead of a Binary Heap
* Very hard to implement efficiently
* Can have several children, number of children are usually kept low
* O(1) insert operation instead of O(logN)


## Associative Arrays
* Overview
    * Collection of key-value pairs where each key appears only once in the collection
    * Typically implemented with hashtables but binary search trees can be used as well
    * Goal is to reach O(1) time complexity for most of the operations
* Operations
    * Adding key-value pairs to the collection
    * Removing key-value pairs from the collection
    * Update existing key-value pairs
    * Lookup of value associated with a given key

    
## Hashtables and Dictionaries
* Arrays as basis for Hashtable
    * Insert/retrieve operations can be done in O(1) time if index is known
    * Problem: Keys must be transformed into array indexes => hash functions (ie. index = hashFn(key); )
* Overview
    * Hashing - mapping a key of any type to a random array index
    * Use modulo operation to transform the number into an index within range
* Operations
    * Search => Avg: O(1), Worst case: O(N)
    * Insert => Avg: O(1), Worst case: O(N)
    * Delete => Avg: O(1), Worst case: O(N)        
* Hash function
    * Distribute the keys uniformly into buckets
    * h(x) = n % m
        * n - number of keys
        * m - number of buckets (size of the array)
    * Use prime numbers for size of the array and in hash function to ensure uniform distribution of generated indexes
    * String keys - calculate the ASCII value for each character, add it up, make modulo
* Collisions - occur when two keys are mapped to the same array index   
* Resolving Collisions
    * Chaining - bucket with colliding index contains a linked list, storing multiple values
        * O(1) complexity gets worse, additional memory cost due to the references
    * Open addressing - find an empty slot instead
        * Linear probing - Find the next empty slot
        * Quadratic probing - Find the next empty slot at 1,2,4,8,... slots away from the collision index
        * Rehashing - Hash the result again in order to find an empty slot
* Dynamic Resizing
    * Load factor - number of entries divided by the number of slots/buckets (n/m)
        * Load factor of 0 - Hash table is empty
        * Load factor of 1 - Hash table is full
    * As load factor approaches 1, performance decreases and operations will be slow (more collisions)
    * As load factor approaches 0, memory is wasted
    * => Trade off between memory usage vs time complexity
    * Java: hashmap will resize automatically when the load factor is greater than 0.75
    * Python: dict will resize automatically when the load factor is greater than 0.66
    * Hash values depend on underlying array's size - hashes of existing entries need to be recomputed
    * Resizing takes O(N) time to complete
    * Dynamic-sized hash tables may be inappropriate for real-time applications
* Applications
    * Database: sometimes search trees, sometimes hashing is better
    * Counting word occurence in a particular document
    * Storing data and lookup tables (ie. password checks)
    * Lookup tables in huge networks (ie. lookup for IP addresses)
    * Hashing technique can be used for substring search (Rabin-Karp algorithm)
    

## Tries
* Overview
    * Also called radix trees or prefix trees
    * Implement associative arrays
    * Keys are usually strings
    * No node in the tree stores the key associated within that given node
    * All descendants of a noe have a common prefix of the string associated with that node, the root is associated with the empty string
    * Values are not necessarily associated with every node, usually leaf nodes only
    * Nodes can have as many edges as needed (unlike a binary search tree)
    * Typically, there are as many edges as the number of characters in the alphabet
    * Memory inefficient because there are typically many unneeded edges/child nodes
    * Search and sort strings very efficiently
    
## Ternary Search Trees
* Overview
    * Store less references and null objects
    * TST stores characters or strings in nodes
    * Each node has 3 children: less (lower child), equal (middle child), or greater (higher child)
    * Can be balanced with rotations but not worth the effort
    * Can be used instead of Hashmap: efficient as hashing
    * Hashing need to examine the entire string key, TST does not
    * Supports sorting operation
    * TST is better than hashing, especially for search misses
    * TST is faster than hashmap and more flexible than binary search trees
* Applications
    * Very efficient for auto-complete feature
    * Can be used for spell-checkers
    * Near-neighbor searching
    * For databases especially when indexing by several non-key fields is desirable
    * Very important in package routing on WWW, routers direct packages in the direction of the longest prefix
    * Prefix matching - Google Search           

    
    
## TST vs Hashing
* Hashing
    * Need to examine the entire key w/ hash function
    * Search hits and misses cost the same
    * Running time and performance relies heavily on the hash function
    * Does not support as many operations as TST
* TST
    * Works ONLY for strings
    * Only examines just enough key characters
    * Search miss may only involve a few characters
    * Supports sorting
    * Faster than hashing (for misses especially), more flexible than BST
   


## Graph Theory
* Two main types of graphs: directed and undirected
    * Directed graph edges have arrows indicating direction
* Hamiltonian Path
    * A path in an undirected or directed graph that visits each vertex exactly once
    * Hamiltonian cycle is a Hamiltonian path that is a cycle
    * Determining whether such paths and cycles exist in graphs is NP-Complete
    * Travelling salesman problem relies on Hamiltonian cycles
    * Problem: given a list of cities and the distances between each pair of cities, what is the 
    shortest possible route that visits each city only once and returns to the origin city
* Eulerian Path
    * It is a trial in a graph which visits every edge exactly once
    * Eulerian cycle is an Eulerian trail which starts and ends on the same vertex
    * An undirected graph has an Eulerian cycle if and only if every vertex has an even degree (# number of edges from the given node is even)
    * Useful for solving the Chinese postman problem
    * Problem: a postman needs to go through every street at least once, closed circuit, wants to find the shortest path
* Algorithms
    * Fleury Algorithm - Not so efficient
        * Rules: 
            1. Pick any vertex to start 
            2. From that vertex, pick an edge to traverse (it can't be traversed again)
            3. Travel that edge
            4. Repeat until all edges are traversed
            5. Important: never cross a bridge of the reduced graph unless there is no other choice
    * Hierholzer Algorithm - Linear time complexity
        * Rules:
            1. Maintain two stacks: one stack contains visited nodes, other stack contains nodes without unvisited edges (results)
            2. Initially all edges are unvisited
            3. Choose any vertex V and push it onto a stack
            4. While the stack is non-empty, look at the top vertex, U, on the stack.  If U has an unmarked incident edge (ie. to a vertex W), then
            push the vertex W onto the stack and mark the edge (U,W).  If U has no unmarked incident edge, the pop U off the stack and print it.
            5. The algorithm terminates when the stack has become empty


## Graph Traversal Algorithms
* Breadth-First Search
    * We want to visit every node exactly once
    * Visit the neighbors then the neighbors of these vertices and so on
    * Running time complexity: Linear O(V+E), V = Vertices, E = Edges
    * Memory complexity is not good: we have to store a lot of references
    * Constructs a shortest path: Dijkstra algorithm does a BFS if all the edge weights are equal to 1
    * Implementation uses a FIFO Queue, starts with an empty queue, we keep checking if we've visited the given node or not, iterate until queue is empty
    * Applications
        * AI/Machine learning - robots can discover the surrounding more easily with BFS than DFS
        * Maximum flow problems - Edmonds-Karp algorithm
        * Cheyen's algorithm in garbage collection - it helps to maintain active references on the heap memory
        * Serialization/Deserialization of a tree like structure - allows the tree to be reconstructed in an efficient manner
* Depth-First Search
    * Investigated as a strategy for solving mazes by Tremaux in the 19th century
    * It explores as far as possible along each branch before backtracking
    * Time complexity is same as BFS: Linear O(V+E), V = Vertices, E = Edges
    * Memory complexity is a bit better than BFS
    * Implemented using recursion or iteration
    * Implementation uses a LIFO Queue, ie. a stack
    * Symmetrical - starting at left or right both work equally well
    * Applications
        * Topological ordering
        * Kosaraju algorithm for finding strongly connected components in a graph which can be proved to be very important in recommendation systems (ie. YouTube)
        * Detecting cycles (checking whether a graph is a Directed Acyclic Graph or not)
        * Generating mazes or finding a way out of a maze
            
        
## Graph Shortest Path Algorithms
* Shortest path problem - finding a path between two vertices in a graph such that the sum of the weights of its edges is minimized
* Dijkstra algorithm
    * Constructed by computer scientist Edsger Dijkstra in 1956
    * Algorithm can handle positive edge weights
    * Several variants: it can find shortest path from A to B, but its able to construct a shortest path tree as well => defines shortest path from a source to all the other nodes
    * Asymptotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded negative weights
    * Algorithm time complexity: Linearithmic O(V*logV + E)
    * Algorithm is a greedy one: it tries to find the global optimum with the help of a local minimum => it turns out to be good
    * It is greedy: on every iteration we want to find the minimum distance to the next vertex possible => appropriate data structures are heaps or priority queues    
* Bellman-Ford algorithm
    * Invented in 1958 by Bellman and Ford independently
    * Slower than Dijkstra's but more robust: it can handle negative edge weights too
    * Dijkstra algorithm chooses the edge greedily, with the lowest cost: Bellman-Ford relaxes all edges at the same time for V-1 iteration
    * Running time is O(V*E)
    * Does V-1 iterations and an additional iteration to determine detect cycles
    * Applications
        * Cycle detection can prove to be very important
        * Negative cycles - Bellman-Ford can handle negative edge weights and detect negative cycles
        * On the FOREX market, it can detect arbitrage situations (mispricing)
        
        
## Applications of Shortest Path Algorithms
* DAG Shortest Path
    * Directed Acyclic Graph - has no directed cycles, it is easier to find the shortest path
    * Sort the vertices into topological order: we iterate through the topological order, relaxing all egdes from the actual vertex
    * Topological sort algorithm computes the shortest path tree in any edge weighted (can be negative) 
    * O(E+V)
    * Much faster than Bellman-Ford or Dijkstra
    * Applications
        * knapsack problem
    

## Disjoint sets
* Also known as union-find data structures
* Data structure to keep track of a set of elements partitioned into a number of disjoint subsets
* Main operations: union, find, and makeSet
* Can be represented by linked lists but usually implemented with tree-like structure
* Kruskal algorithm, with disjoint sets, we can decide in O(1) time whether two vertexes are in the same set or not

## Spanning Tree
* Determine which edges with the lowest cost (weight) should be included to connect all vertices in the graph
* A spanning tree of an undirected graph is a subgraph that includes all the vertices
* A tree may have several spanning trees
* A weight is assigned to each edge
* A minimum spanning tree is then a spanning tree with weight less than or equal to the weight of every other spanning tree
* Applications: big data analysis, clustering algorithms, minimum cost for telecom company laying cable to a new neighborhood
* Standard algorithms: Prim's-Jarnik, Kruskal -> greedy algorithms

## Kruskal Algorithm
* Edge-based algorithm
* Sorts the edges according to their edge weights
* Union find data structure: disjoint set


## Prims Algorithm
* Build spanning tree from a given vertex, adding the smallest edge to the minimum spanning tree
* Vertex-based algorithm
* Underlying data structure is a heap
* Running time: O(E*logE), worst case: O(E*logV)

## Prims vs Kruskal Algorithm
* Prims is faster when graph is dense (ie. many more edges than vertices)
* Kruskal performs better when graph is sparse (ie. less edges).  
* Kruskal can have better performance if the edges can be sorted in linear time or the edges are pre-sorted


## Applications of Spanning Trees
* Optimization problems related to roads, cables, pipes, etc.
* K-means clustering - classify similar items
* Routing in LAN - spanning tree topology ensures a loop-free topology for any bridged Ethernet local area network
    

## Sorting Algorithm
* Sorting algorithms put elements of an array in a certain order (ie. numerical, alphabetical, chronological, etc)
* Comparison based algorithms: bubble sort, insertion sort, selection sort, merge sort, quicksort
* Non-comparison based sorting: radix sort, bucket sort
* Features:
    * Time complexity: O(N^2), O(NlogN), O(N)
    * In place - needs only O(1) memory beyond the items being sorted (ie. does not require extra memory)
    * Recursive - implemented in a recursive manner, especially the divide and conquer algorithms
    * Stable - maintain the relative order of records with equal values

## Adaptive Sorting Algorithms  
* Changes its behavior based on information available at runtime
* Adaptive sort takes advantage of existing order in its input
* Benefits from local orders, sometimes an unsorted array contains sequences that are sorted by default result in a faster sort
* Most of the time, existing sorting algorithms can be modified to be adaptive


## Bubble Sort
* Too slow and impractical for most problems
* Stable and in-place algorithm
* Time complexity: O(N^2)


## Selection Sort
* Noted for its simplicity and it has performance advantages over more complicated algorithms
* Particularly useful when auxiliary memory is limited
* Algorithm divides input list into two parts: sub-array of sorted items, sub-array of unsorted items
* Algorithm is in-place and not stable
* Performs better than bubble sort - less swaps
* Time complexity: O(N^2)


## Insertion Sort
* Simple sorting algorithm, builds final sorted array one item at a time
* Performs better than bubble sort and selection sort
* Adaptive algorithm - speeds up when array is already substantially sorted
* Algorithm is in-place and stable
* Very good for smaller arrays: 10-20 items
* Insertion sort requires mores writes because the inner loop can require shifting large sections of the sorted sub-array
* Insertion sort writes O(N^2) times while selection sort will write only O(N) times
* Time complexity: O(N^2)


## Quicksort
* An efficient sorting algorithm
* Well implemented quicksort outperforms heapsort and mergesort
* Comparison-based algorithm
* Algorithm is in-place and not stable
* Time complexity: O(N logN), worst case => O(N^2)
* Divide and conquer algorithm


## Mergesort
* Divide and conquer algorithm
* Comparison-based algorithm
* Algorithm is not in-place and is stable
* Heapsort has the same time bounds as merge sort - heapsort requires only O(1) auxiliary space, mergesort requires O(N)
* Efficient quicksort implementations outperform mergesort
* Mergesort is often the best choice for sorting a linked list: in this situation its relatively easy to implement a merge sort that requires O(1) extra space


## Hybrid Algorithms
* Combines more algorithms to solve a given problem
* Choses one algorithm depending on the data or switching between them over the course of the algorithm
* Generally done to combine desired features of different algorithms for better performance
* Hybrid algorithms combine multiple algorithms that solve the same problem but differ in characteristics (such as performance)
* The technique can be used when sorting
    * Introsort = Quicksort + Heapsort
    * Timsort = Insertion sort + Mergesort


## Counting sort
* Non-comparison based algorithm
* Operates by counting the number of objects that have each distinct key value
* Integer sorting algorithm: value MUST be integers
* Uses arithmetic on counts to determine the positions of each key value in the output sequence
* Suitable when the variation in keys is not significantly greater than the number of items
* Can be used as a subroutine in radix sort
* O(N + k)


## Radix sort
* Non-comparison based algorithm
* String-based algorithm
* Sort the elements according to individual characters
* Stable sorting algorithm
* Two types: Least-significant-digit, Most-significant-digit




    

                                             
        
        
    
     