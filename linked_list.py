class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, 'List is empty'
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


l_list = LinkedList()
l_list.insert(4)
l_list.insert(6)
l_list.insert(8)
# print(l_list)
