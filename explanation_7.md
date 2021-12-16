# Request Routing in a Web Server with a Trie


## Time complexity

The worst time complexity of add handler is O(n).

Suppose n is the number of level of the path.
Both add and lookup the path have the same time complexity. 

algorithms:
 - trim and split the path string by '/' into the array that holds each nodes, O(1)
 - add or lookup is guided by the node list one by one until the last one, O(n)

## Space complexity

The space complexity is O(n).

Suppose n is depth of the path. The router needs to hold every node of the path, 
and growing with the length of level in path.

On the other hand, if there are many relative path stored in the router, 
and suppose the number of path is m, the space complexity much less then O(m). 