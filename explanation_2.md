# Search in a Rotated Sorted Array

## Idea

By observing, the rotated array's elements are divided into two parts, 
they are keeping ordered in smaller scales. There is a point that connects 
these two parts. It is necessary to find it for next process, because the 
rotated array can be recovered by using it. Once the whole order of the array 
is recovered, binary search can be used for indexing any element in log n.

I prefer to call this point as 'rotated point in the following part. From 
this point, the smaller ordered part that follows the biggest element. 

To find the rotated point, the binary search can be used for meeting the required 
time complexity. In the rotated array, this point is the smallest element that 
connects to the biggest one. If the reversed order of two elements is digged out, 
then the point will be there. 

Next, I am going to recover the order of the given array.

One way is to move the elements following the rotated point to the head of the 
array. However, this operation costs O(n) in worst case. 

Another way is to map the position of the elements. When the binary searching 
program to deal with the array, it operates the array as the normal ordered array. 
But the fetching operation converts the normal array index into the index of rotated
array. 

Even though every searching step needs to convert the index, but it just costs O(1), 
so the second approach can be used. 

## Converting the index

This process like the 'map', but it is not the real 'map'. It just a formula to 
calculate the index of ordered array and pick up the appropriate value from the 
rotated array. 

## Time complexity

The worst time complexity of indexing is O(log n)

algorithms:
 - find out the point that the lowest element follows the biggest one, O(log n)
 - convert the index, O(1)
 - binary search the target by using the converted index, O(log n)

## Space complexity

In this program, there is no more growing space for processing. It costs O(1).
