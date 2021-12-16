# Rearrange Array Elements


class MaxHeap:

    def __init__(self, arr):
        self.heap = arr
        self.last_index = len(arr) - 1
        self._heapify()

    def _heapify_walk(self, i):
        arr = self.heap
        last = self.last_index
        
        while i < last:
            
            v = arr[i]
            left_child_i = i * 2 + 1
            right_child_i = i * 2 + 2

            left_child_v = None
            right_child_v = None
            maximum_v = v

            # find out the maximum value in parent and children items
            if left_child_i <= last:
                left_child_v = arr[left_child_i]
                maximum_v = max(maximum_v, left_child_v)
            if right_child_i <= last:
                right_child_v = arr[right_child_i]
                maximum_v = max(maximum_v, right_child_v)

            # move the bigger value of the tree to higher level 
            if maximum_v == left_child_v:
                arr[i], arr[left_child_i] = left_child_v, v
                i = left_child_i
            elif maximum_v == right_child_v:
                arr[i], arr[right_child_i] = right_child_v, v
                i = right_child_i
            else:
                return

    def _heapify(self):
        arr = self.heap
        n = len(arr)
        i = 0
        while i < n:
            last_index = n - 1 - i
            self._heapify_walk(last_index - 1 // 2)
            i += 1

    def pop(self):
        """
        Pop the maximum (first) item of the heap.

        Returns:
            int: the current maximum number is popped
            None: if there is no item in the heap
        """
        
        arr = self.heap

        if self.last_index >= 0:
            v = arr[0]
            arr[0] = arr[self.last_index]
            self.last_index -= 1
            self._heapify_walk(0)
            return v
        
        return None


def generate_number_from_array(arr):
    n = len(arr)
    result = 0
    for i in range(0, n):
        result += 10**i * arr[n - i - 1]
    return result

def rearrange_digits(arr):
    """
    Rearrange the elements of given array to yield a pair of numbers 
    and their sum is maximum.

    Args:
       arr(list): a list filled by numbers
    Returns:
       (int, int): two numbers their sum is maximum
       (None, None): if input data is void
    """

    if arr is None or len(arr) == 0:
        return (None, None)

    mh = MaxHeap(arr)
    
    first_numbers = list()
    second_numbers = list()

    for i, _ in enumerate(arr):
        v = mh.pop()
        if i % 2 == 0:
            first_numbers.append(v)
        else:
            second_numbers.append(v)

    first_n = generate_number_from_array(first_numbers)
    second_n = generate_number_from_array(second_numbers)

    return first_n, second_n


def test_function(test_i, input, solution):
    input_raw = input[0:]
    output = rearrange_digits(input)

    print('test {}, input: {}'.format(test_i, input_raw))
    print('output: {}, one solution: {}'.format(output, solution))
    if output != (None, None):
        print('output sum: {}, solution sum: {}'.format(sum(output), sum(solution)))

    if (output == solution) or (sum(output) == sum(solution)):
        print("Pass")
    else:
        print("Fail")

    print('\n')
    

# test 1
test_function(1, input = [1, 2, 3, 4, 5], solution = (542, 31))

# test 2
test_function(2, input = [4, 6, 2, 5, 9, 8], solution = (964, 852))

# test 3
test_function(3, input = [2], solution = (2, 0))

# test 4
test_function(4, input = [], solution = (None, None))

# test 5
test_function(5, input = [2, 2, 2, 2], solution = (22, 22))