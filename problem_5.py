# Autocomplete with Tries


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = dict()
    
    def insert(self, char):
        node = self.children.get(char)
        if node is None:
            node = TrieNode()
            self.children[char] = node
        return node

    def _suffixes_walk(self, suffix, results):
        if self.is_word and suffix != "":
            results.append(suffix)
        
        children = self.children
        for char, node in children.items():
            node._suffixes_walk(suffix + char, results)
    
    def suffixes(self, suffix = ""):
        results = list()
        self._suffixes_walk(suffix, results)
        return results


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.insert(c)
        node.is_word = True
        
    def find(self, prefix):
        """
        Find the Trie node that represents this prefix.

        Argus:
            prefix(string): character(s) for finding the node

        Returns:
            node(TrieNode): after iterating the prefix, the node reached
            None: when iterating the prefix unfinished
        """
        
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if node is None:
                return node
        return node


# preparing test data 
my_trie = Trie()
word_list = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list:
    my_trie.insert(word)


def test_function(n, target, expected):
    node = my_trie.find(target)
    
    print('test {}, target: {}'.format(n, target))
    print('expected: {}'.format(expected))

    if node is None and expected is None:
        print('result: None')
        print("Pass")
        return
    
    output = node.suffixes()
    print('result: {}'.format(output))
    
    if output == expected:
        print("Pass")
    else:
        print("Fail")

    print('\n')

# test 1
test_function(1, target = "f", expected = ["un", "unction", "actory"])

# test 2
test_function(2, target = "fun", expected = ["ction"])

# test 3
test_function(3, target = "function", expected = [])

# test 4
test_function(4, target = "functionality", expected = None)


