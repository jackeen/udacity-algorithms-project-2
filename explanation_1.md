# Square Root of an Integer

# Idea

The sqrt root of the number is between zero and itself. 

According to the given requirement of time complexity, O(log n), 
the binary search is the best way to find the location of two 
numbers' range.

0 can be set as the min border of the range, and the given number 
can set as the max border of the range. The binary search can scale 
down the scope of the sqrt root in O(log n).

Eventually, the middle value of the two border numbers is the sqrt 
root of the given number. 

As for the special numbers, such as 0 and 1, their sqrt root is itself, 
so, it is not meaningful to use this program to find it. These two numbers 
will return directly in practice.

## Time complexity

The worst time complexity is O(log n).

## Space complexity

The space complexity is O(1).