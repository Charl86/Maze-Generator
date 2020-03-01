class Node:
    def __init__(self, val=None, next_nod=None, prev_nod=None):
        self.val = val
        self.next_nod = next_nod
        self.prev_nod = prev_nod


class DoublyLinkedList:
    def __init__(self):
        self.leading_node = None

    def traverse(self, values=False):
        nodes = []
        current_node = self.leading_node
        while current_node is not None:
            if values:
                nodes.append(current_node.val)
                current_node = current_node.next_nod
            else:
                nodes.append(current_node)
                current_node = current_node.next_nod
        return nodes

    def add(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError("A Node() object was expected, but instead something else was given.")

        if self.leading_node is None:
            self.leading_node = new_node
        else:
            previous_node = self.leading_node
            current_node = self.leading_node.next_nod
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.next_nod
            previous_node.next_nod = new_node
            new_node.prev_nod = previous_node

    def peek(self):
        current_node = self.leading_node
        while current_node.next_nod is not None:
            current_node = current_node.next_nod
        return current_node

    def pop(self):
        current_node = self.leading_node
        while current_node.next_nod is not None:
            current_node = current_node.next_nod
        popped_node = current_node
        if current_node.prev_nod is None:
            self.leading_node = None
        else:
            current_node.prev_nod.next_nod = None
        return popped_node


def check_type(a, b):
    print(f"{a}'s type is: {type(a)}.\n"
          f"{b}'s type is: {type(b)}.\n"
          f"{a}'s type = {b}'s type: {type(a) == type(b)}.\n")


if __name__ == "__main__":
    doublyLL = DoublyLinkedList()

    doublyLL.add(Node("Mon"))
    doublyLL.add(Node("Tue"))
    doublyLL.add(Node("Wed"))
    print(doublyLL.traverse(values=True))

    # print(f"Mon's previous node: {doublyLL.traverse()[0].prev_nod.val}.")
    print(f"Tue's previous node: {doublyLL.traverse()[1].prev_nod.val}.")
    print(f"Wed's previous node: {doublyLL.traverse()[2].prev_nod.val}.\n")

    print(f"Mon's next node: {doublyLL.traverse()[0].next_nod.val}.")
    print(f"Tue's next node: {doublyLL.traverse()[1].next_nod.val}.")
    # print(f"Wed's next node: {doublyLL.traverse()[2].next_nod.val}.")
