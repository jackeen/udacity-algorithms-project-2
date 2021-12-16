# Dutch National Flag Problem (sort 0,1,2)

def sort_012(arr):
    """
    Transform the given array containing 0, 1, and 2 to the ordered form 
    in one travering.

    Args:
        arr(list): the list for rearranging
    """
    
    if arr is None:
        return

    n = len(arr)
    if n == 0:
        return

    zero_index = 0
    two_index = n - 1
    index = 0
    
    while index <= two_index:
        v = arr[index]
        
        if v == 0:
            if index > zero_index:
                border_v = arr[zero_index]
                arr[zero_index] = v
                arr[index] = border_v
            else:
                index += 1
            zero_index += 1
        
        elif v == 1:
            index += 1
        
        # if current value is 2, exchange it with the value that located at 
        # previous position of the position taken by 2s, the current new one 
        # will be compared in the next step
        else:
            border_v = arr[two_index]
            arr[two_index] = v
            arr[index] = border_v
            two_index -= 1


def test_function(arr):
    expected = sorted(arr)
    print('target: {}'.format(arr))
    print('expect: {}'.format(expected))
    sort_012(arr)
    print('result: {}'.format(arr))
    if arr == expected:
        print('Pass')
    else:
        print('Fail')

    print('\n')

# test 1
print('--- test 1 ---')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# test 2
print('--- test 2 ---')
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# test 3
print('--- test 3 ---')
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# test 4
print('--- test 4 ---')
test_function([1, 1, 1, 0, 2, 0, 2])

# test 5
print('--- test 5 ---')
test_function([])
