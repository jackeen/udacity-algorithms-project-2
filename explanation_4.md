# Dutch National Flag Problem (sort 0,1,2)

# Idea

Building up the new array with length as same as the given array, 
and full filling it by 1s. Doing this for holding 0(s) and 2(s) at two 
ends of the new array by traversing the given array in single time. 

Finally, the 1(s) will remain in the middle of the new array.

The above method is pretty simple, but needs more space.
It can be improved as below one.

Because there are three kinds of numbers in the given array. So the two ends 
of the array can be used without the extra array. The head of given array can 
be used to hold 0(s), and the tail can be used to hold 2(s). The remained cell 
of the array will be 1(s) after single traversing.

In this method, the exchanging of value at different position will be done in 
one place. The code will be little more complex, but less space is required.

## Time complexity

The worst time complexity is O(n)

## Space complexity

The space complexity is O(1)

Because there are no extra space be used in the process.