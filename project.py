class ListDict:

    def __init__(self):
        self.storage = []

    def insert(word):
        word = word.lower()
        try:
            self.storage.index(word)
        except ValueError:
            self.storage.append(word)

    def lookup(word):
        word = word.lower()
        try:
            self.storage.index(word)
            return True
        except ValueError:
            return False

class HashMapDict:

    def __init__(self):
        self.storage = {}

    def insert(word):
        word = word.lower()
        self.storage[word] = True

    def lookup(word):
        word = word.lower()
        return True if self.storage.get(word, False) else False

class BinarySearchTreeDict:

    class Node:
        def __init__(self, left, word, right):
            self.left = left
            self.word = word
            self.right = right

    def __init__(self):
        self.storage = None

    def insert(word):
        _insert(word.lower())

    def _insert(word, node=self.storage):
        if ( node == None ):
            node = Node(None, word, None)
        elif ( word < node.word ):
            self.insert(word, node=node.left)
        elif ( word > node.word ):
            self.insert(word, node=node.right)

    def lookup(word):
        return _lookup(word.lower())

    def _lookup(word, node=self.storage):
        if ( node == None ):
            return False
        elif ( word < node.word ):
            return self.lookup(word, node=node.left)
        elif ( word > node.word ):
            return self.lookup(word, node=node.right)
        else:
            return True
