# Max and Min in a Unsorted Array

## Idea

Considering the negative integer might be existed in the input data, 
so, 0 can not be chosen as the minimum for comparing.

The best way is to pick up any number of the input array as the minimum 
and maximum for following comparison. For convenience of the iteration, 
the first element of the array is chosen as the minimum and maximum. 

## Time complexity

The worst time complexity is O(n).

## Space complexity

The space time complexity is O(1).