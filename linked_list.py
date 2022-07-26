from node import Node


class LinkedList:

    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_node):
        self._head = new_node

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node

        else:
            first_node = self.head
            second_node = self.head.next

            while (second_node is not None) and (value > second_node.value):
                first_node = second_node
                second_node = second_node.next

            first_node.next = new_node
            new_node.next = second_node

    def print_linked_list_items(self):
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(f"{current_node.value} ", end="")
                current_node = current_node.next
            print()

    def print_reversed_list_items(self):
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            items = []
            while current_node is not None:
                items.append(current_node.value)
                current_node = current_node.next

            for i in range(1, len(items)+1):
                print(items[-i], end=" ")

    def count_nodes(self):
        count = 0
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                count += 1
                current_node = current_node.next
        return count

    def find_node(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False

    def delete_node(self, value):
        if self.head is None:
            return False
        elif value == self.head.value:
            self.head = self.head.next
            return True
        else:
            current_node = self.head
            next_node = current_node.next

            while next_node is not None:
                if next_node.value == value:
                    current_node.next = next_node.next
                    return True
                else:
                    current_node = next_node
                    next_node = current_node.next
            return False

