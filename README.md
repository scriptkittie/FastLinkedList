# FastLinkedList
 A linked-list implementation that mimics a least-recently-used (LRU) cache system

# Overview

Recently, I began working on a project that required the use of a data structure that performed similar to a least-recently-used (LRU) cache system. Essentially, what I wanted to do was to build a "cache" of the last 20,000 used objects/elements. When a new object had to be created within the structure, I wanted to remove the oldest element in the "cache". Previously, the structure I was using was suitable the OrderedDict implementation, and only 160 elements. With such a small amount of elements, looping through the dictionary to find the least recently used element was efficient for the program load. However, with 20,000 objects, that situation changed. The built in python OrderedDict implementation was inefficient for what I wanted to accomplish. Some research led me to see that a simple linked list data structure was a good fit for this problem, as a doubly linked list can easily be maintained in a least recently used order. With this implementation, when an element in the structure is used, it is moved to the beginning of the list (an O(1) operation on linked list), meaning that the structure stores objects sorted from most recently used to least recently used. To remove the most least recently used element, the tail of the list is removed. (which is also an O(1) operation).


As mentioned above, the main difference between an typical linked list implementation and this linked list implementation, is that this implementation does not allocate element objects to store the next and previous references. Instead, the structure stores those references in the nodes themselves. I also added some special helper functions which help in moving elements in the linked list to the start of the list. This helps with performance. Tthe following functions are all O(1):

 - add_to_first(o)
 - add_to_last(o)
 - move_to_first(o)
 - remove_element(o)
 - remove_from_first()
 - remove_from_last()
