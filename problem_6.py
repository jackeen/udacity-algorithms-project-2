# Max and Min in a Unsorted Array

import random


def get_min_max(arr):
    if arr is None or len(arr) == 0:
        return (None, None)

    first_element = arr[0]
    min_int = first_element
    max_int = first_element

    for i in range(1, len(arr)):
        v = arr[i]
        if v > max_int:
            max_int = v
        if v < min_int:
            min_int = v

    return min_int, max_int


def test_function(n, arr, expected):
    result = get_min_max(arr)
    
    print('test {}, input: {}\nexpecting {}, result {}'.format(n, arr, expected, result))
    
    if result == expected:
        print('Pass')
    else:
        print('Fail')

    print('\n')


# The expected results follwing next test cases if Pass

# test 1
arr = [1, 4, 9, 6, 0, -1, 7, 7]
expected = (-1, 9)
test_function(1, arr, expected)

# test 2
arr = [i for i in range(-8, 30)]
random.shuffle(arr)
expected = (-8, 29)
test_function(2, arr, expected)

# test 3
arr = [i for i in range(-1, -9, -1)]
random.shuffle(arr)
expected = (-8, -1)
test_function(3, arr, expected)

# test 4
arr = []
expected = (None, None)
test_function(4, arr, expected)

# test 5
arr = None
expected = (None, None)
test_function(5, arr, expected)
