class ListsDict:

    def __init__(self):
        self.storage = []

    def insert(word):
        try:
            self.storage.index(word)
        except ValueError:
            self.storage.append(word)

    def lookup(word):
        try:
            self.storage.index(word)
            return True
        except ValueError:
            return False
