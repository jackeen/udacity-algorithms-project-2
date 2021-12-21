# Autocomplete with Tries


## Time complexity

The time complexity of insertion is O(n).

Suppose the characters of word is n.

algorithms:
 - iterate every characters of given word until worn out letters, O(n)
 - check and generate trie nodes for letters if there are not exist, O(n)
 - finishing the adding word by setting the sign of existed word, O(1)


The time complexity of finding suffix is O(n * m).

Suppose the input number of character is n, and average number of children of 
nodes is m. 

The more letters user input, the less depth of nodes need to explore. Suppose 
user input half of the letters of words every time. The traversing node stage 
costs O(n / 2), the collection suffix stage costs O(n / 2 * m). 
Therefore, the total cost is O(n * m). 

algorithms:
 - iterate the given prefix one by one until the trie node with last letter of the prefix, O(n)
 - iterate the children of the last letter's trie node recursively, 
   and record the word if it is existed, O(m * n)

## Space complexity

Suppose the average of length of word is n and the number of the word is m, 
the space complexity is O(n * m). In practice, most of words is containing or 
contained by others, so, it is father less then this evaluated result.

## Modular complexity

> supposed n and m is similar to previous part

'Trie' complexity
 - Method 1 'insert'  
   time complexity: O(n)  
   space complexity: O(1)

 - Method 2 'find'  
   time complexity: O(n)  
   space complexity: O(1)

'TrieNode' complexity
 - Method 1 'insert'  
   time complexity: O(1)  
   space complexity: O(1)

 - Method 2 'suffixes'  
   time complexity: O(m * n)  
   space complexity: O(m * n)

 - Method 3 '_suffixes_walk'  
   time complexity: O(m * n)  
   space complexity: O(m * n)
