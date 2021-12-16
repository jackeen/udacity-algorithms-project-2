# Search in a Rotated Sorted Array

def find_rotated_point(arr):
    """
    To find out the point where the smallest element following the biggest one.
    """
    
    n = len(arr)
    start_index = 0
    end_index = n - 1

    # There is no rotated point in the given array
    if arr[start_index] < arr[end_index]:
        return 0

    while True:
        middle_index = (start_index + end_index) // 2
        middle_value = arr[middle_index]
        end_value = arr[end_index]

        if middle_value > end_value:
            if start_index == middle_index:
                break
            else:
                start_index = middle_index
                continue
        
        if middle_value < end_value:
            end_index = middle_index
            continue
    
    return end_index


class RotatedArray:
    
    def __init__(self, array):
        self.is_void_array = False
        
        if array is None or len(array) == 0:
            self.is_void_array = True
            return

        self.array = array
        self.rotated_point = find_rotated_point(array)

    def _is_rotated_array(self):
        return self.rotated_point != 0

    def _binary_array_index(self, value):
        arr = self.array
        start = 0
        end = len(arr) - 1
        
        while end >= start:
            middle = (start + end) // 2
            middle_value = self._get_array_value(middle)
            
            if value > middle_value:
                start = middle + 1
            elif value < middle_value:
                end = middle - 1
            else:
                return self._get_array_index(middle)

        return -1

    def _get_array_value(self, index):
        if self._is_rotated_array():
            index = self._convert_to_real_index(index)

        return self.array[index]

    def _get_array_index(self, index):
        if self._is_rotated_array():
            return self._convert_to_real_index(index)

        return index

    def _convert_to_real_index(self, index):
        """
        Translate the rotated array index to the not rotated form.
        """

        length = len(self.array)
        offset = self.rotated_point
        
        real_index = index + offset
        if real_index >= length:
            real_index -= length
        
        return real_index
    
    def index(self, value):
        if self.is_void_array or value is None:
            return -1
        return self._binary_array_index(value)

def rotated_array_search(array, number):
    """
    Find the index in a rotated sorted array.

    Args:
       array(list): the elements for searching
       number(int): the target
    
    Returns:
       int: the index of the number found the array
       -1: when the number are not found
    """

    ra = RotatedArray(array)
    return ra.index(number)


def linear_search(arr, target):
    if arr is not None:
        for i, v in enumerate(arr):
            if v == target:
                return i
    return -1

def test_function(test_i, case):
    arr = case[0]
    target = case[1]

    expected = linear_search(arr, target)
    output = rotated_array_search(arr, target)

    print('test {}, find {} in {}'.format(test_i, target, arr))
    print('output: {}, expected: {}'.format(output, expected))

    if output == expected:
        print('Pass')
    else:
        print('Fail')

    print('\n')


# tests
test_function(1, [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function(2, [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function(3, [[6, 7, 8, 1, 2, 3, 4], 90])
test_function(4, [[1, 2, 3, 4], 4])
test_function(5, [[], 1])
test_function(6, [[], None])