# Request Routing in a Web Server with a Trie


## Time complexity

The worst time complexity of add handler is O(n).

Suppose n is the number of level of the path.

The time complexity of 'add_handle' is O(n).
algorithms:
 - translate the string of path into the trie node array of path, O(1)
 - iterate the node array of path, and add the not existed route trie node, (n)
 - assign the given handler to the relative property of the route trie node, O(1)

The time complexity of 'lookup' is O(n).
algorithms:
 - translate the string of path into the trie node array of path, O(1)
 - iterate existed trie node based on the array of path as far as possible, O(n)
 - check the trie node with last element of the array, and return the appropriate handler, O(1)


## Space complexity

The space complexity is O(n).

Suppose n is depth of the path. The router needs to hold every node of the path, 
and growing with the length of level in path.

On the other hand, if there are many relative path stored in the router, 
and suppose the number of path is m, the space complexity much less then O(m). 