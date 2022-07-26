class Node:

    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def __str__(self):
        return f"node_{self.value}"
