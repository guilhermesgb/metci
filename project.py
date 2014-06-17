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
