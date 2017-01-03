
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
    


    
    
    
    


