from queue import PriorityQueue


class _cmp_class:
    def __init__(self, item, key):
        self.item = item
        self.key = key

    def __lt__(self, other):
        return self.key(self.item) < other.key(other.item)

    def __eq__(self, other):
        return self.key(self.item) == other.key(other.item)


class CustomPriorityQueue(PriorityQueue):
    def __init__(self, key):
        self.key = key
        super().__init__()

    def _put(self, item):
        super()._put(_cmp_class(item, self.key))

    def _get(self):
        wrapper = super()._get()
        return wrapper.item

