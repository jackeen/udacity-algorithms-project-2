# Request Routing in a Web Server with a Trie


## Time complexity

The worst time complexity of add handler is O(n).

Suppose n is the number of level of the path.

The time complexity of 'add_handle' is O(n).
algorithms:
 - trim and split the path string by '/' into the array that holds each nodes, O(1)
 - follow the trie node by path nodes until get the end, O(n)
 - hold the given handler in final trie node, O(1)

The time complexity of 'lookup' is O(n).
algorithms:
 - translate the string of path into the node array of path, O(1)
 - iterate every path nodes and follow the stored trie data, O(n)
 - decide which handler (user's or not found) can be returned, O(1)


## Space complexity

The space complexity is O(n).

Suppose n is depth of the path. The router needs to hold every node of the path, 
and growing with the length of level in path.

On the other hand, if there are many relative path stored in the router, 
and suppose the number of path is m, the space complexity much less then O(m). 