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

if __name__ == "__main__":

    import sys, time

    if ( sys.argv[1] == "binarytree" ):
        data_structure = BinarySearchTreeDict()
    elif ( sys.argv[1] == "hashmap" ):
        data_structure = HashMapDict()
    else:
        data_structure = ListDict()

    data_file = sys.argv[2]
    data_file = open(data_file, 'r')

    words = []
    for word in data_file.readlines():
        words.append(word)

    start = time.clock()
    for word in words:
        data_structure.insert(word)
    insertion_time = time.clock() - start

    queries_file = sys.argv[3]
    queries_file = open(queries_file, 'r')

    words = []
    for word in queries_file.readlines():
        words.append(word)

    results = []
    start = time.clock()
    for word in words:
        results.append(data_structure.lookup(word))
    lookup_time = time.clock() - start

    for i in range(len(words)):
        print '<{}> : {}'.format(words[i],
            "S" if results[i] else "N")
    print "tempo_de_carga :", insertion_time
    print "tempo_da_consulta :", lookup_time
    print "consumo_de_memoria :", 0
