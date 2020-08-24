class MyStack:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.nextNode = None

    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = self.Node(val)
        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
            else:
                currNode.nextNode = newNode

    def pop(self, val=True):
        currNode = self.head
        if currNode is not None:
            while currNode.nextNode.nextNode is not None:
                currNode = currNode.nextNode
            else:
                delVal = currNode.nextNode.val
                currNode.nextNode = None
                if val:
                    return delVal

    def peek(self, val=True):
        currNode = self.head
        if currNode is not None:
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
            else:
                return currNode.val if val else currNode
        else:
            return None

    @property
    def length(self):
        if self.head is None:
            return 0
        else:
            counter = 1
            currNode = self.head
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
                counter += 1
            return counter

    def __str__(self):
        vals = []
        if self.head is None:
            return "|"
        else:
            currNode = self.head
            while currNode is not None:
                vals.append(str(currNode.val))
                currNode = currNode.nextNode
            return f"|{', '.join(vals)}"

    def __repr__(self):
        vals = []
        if self.head is None:
            return "|"
        else:
            currNode = self.head
            while currNode is not None:
                vals.append(str(currNode.val))
                currNode = currNode.nextNode
            return f"|{', '.join(vals)}"


if __name__ == "__main__":
    stack = MyStack()

    print(stack.peek())
    print(stack)
    print()

    stack.push(1)
    print(stack.peek())
    print(stack)
    print()

    stack.push(1)
    print(stack.peek())
    print(stack)
    print()

    stack.push(2)
    print(stack.peek())
    print(stack)
    print()

    stack.push(3)
    print(stack.peek())
    print(stack)
    print()

    stack.push(5)
    print(stack.peek())
    print(stack)
    print()

    stack.pop()
    print(stack.peek())
    print(stack)
    print()
