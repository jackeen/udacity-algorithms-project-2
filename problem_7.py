# Request Routing in a Web Server with a Trie


class RouteTrieNode:

    def __init__(self, handler = None):
        self.children = dict()
        self.handler = handler

    def insert(self, path):
        children = self.children
        node = children.get(path)
        
        if node is None:
            node = RouteTrieNode()
            children[path] = node

        return node


class RouteTrie:

    def __init__(self, root_handler = None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_arr, handler):
        node = self.root
        for path in path_arr:
            node = node.insert(path)

        node.handler = handler

    def find(self, path_arr):
        node = self.root
        for path in path_arr:
            node = node.children.get(path)
            if node is None:
                return node
        
        return node


class Router:

    # error handlers' name, compare to user handler,
    # these handlers hold some error cases, such as 404
    # which standardizes these kind of cases in following code
    not_found = "404"

    def __init__(self, root_handler, not_found_handler):
        trie = RouteTrie(root_handler)

        error_handlers = dict()
        error_handlers[self.not_found] = not_found_handler

        self.trie = trie
        self.error_handlers = error_handlers

    def add_handler(self, whole_path, handler):
        path_array = self.split_path(whole_path)
        self.trie.insert(path_array, handler)
    
    def lookup(self, whole_path):
        path_array = self.split_path(whole_path)
        node = self.trie.find(path_array)
        if node and node.handler:
            return node.handler
        
        return self.error_handlers[self.not_found]
    
    def split_path(self, whole_path):
        path_array = None
        if whole_path == "" or whole_path == "/":
            path_array = []
        else:
            # simplify the given path and transform it to the node list
            whole_path = whole_path.strip("/")
            path_array = whole_path.split("/")

        return path_array



# init test
router = Router("root handler", "404 handler")
router.add_handler("/home/about", "about handler")

def test_function(test_n, input, expected):
    result = router.lookup(input)

    print('test {}, input: {}'.format(test_n, input))
    print('expected: {}, result: {}'.format(expected, result))

    if expected == result:
        print('Pass')
    else:
        print('Fail')

    print('\n')


# test 1
test_function(1, input = '/', expected = 'root handler')

# test 2
test_function(2, input = '/home', expected = '404 handler')

# test 3
test_function(3, input = '/home/about', expected = 'about handler')

# test 4
test_function(4, input = '/home/about/', expected = 'about handler')

# test 5
test_function(5, input = '/home/about/me', expected = '404 handler')