# Autocomplete with Tries


## Time complexity

The time complexity of insertion is O(n), suppose the characters of word is n.


The time complexity of finding suffix is O(n * m).

Suppose the input number of character is n, and average number of children of 
nodes is m. 

The more letters user input, the less depth of nodes need to explore. Suppose 
user input half of the letters of words every time. The traversing node stage 
costs O(n / 2), the collection suffix stage costs O(n / 2 * m). 
Therefore, the total cost is O(n * m). 

algorithms:
 - iterate to the target node, O(n)
 - find out every children of current node and collect all words, O(n * m)

## Space complexity

Suppose the average length of word is n and the number of the word is m, the 
space complexity is O(n * m). In practice, most of words is containing or 
contained by others, so, it is father less then this evaluated result.

