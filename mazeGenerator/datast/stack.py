
# Implementation of a Stack.
class Stack:
    class Node:  # Node class (or pointers that hold a value and direction to next node).
        def __init__(self, val=None):
            self.val = val
            self.nextNode = None

    def __init__(self):
        self.head = None

    # Add new node with value to stack.
    def push(self, val):
        newNode = self.Node(val)  # Create new node with given value.
        if self.head is None:  # If stack is empty, put node in stack.
            self.head = newNode
        else:  # Else loop through nodes until a given node points to nothing
            currNode = self.head
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
            else:  # Then set that last node to point to the newly-created node.
                currNode.nextNode = newNode

    # Remove value from the stack.
    def pop(self, val=True):
        currNode = self.head
        if currNode is not None:  # If stack is not empty, loop through nodes.
            while currNode.nextNode.nextNode is not None:
                currNode = currNode.nextNode
            else:
                # Save the value to be deleted and set last node to None through
                # the previous node.
                delVal = currNode.nextNode.val
                currNode.nextNode = None
                if val:
                    return delVal  # Return deleted value if desired.

    # Get value sitting on top of stack.
    def peek(self, val=True):
        currNode = self.head
        if currNode is not None:  # Loop through nodes until the last one is reached.
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
            else:  # Return last node or its value depending on parameter.
                return currNode.val if val else currNode

    # Get length of stack.
    @property
    def length(self):
        if self.head is None:  # If stack is empty, return 0.
            return 0
        else:
            counter = 1
            currNode = self.head  # While there is a next node to go to, add to counter.
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
                counter += 1
            return counter  # Return counter.

    # Return string representation of stack.
    def __str__(self):
        vals = []
        if self.head is None:  # If stack is empty return pipe.
            return "|"
        else:
            currNode = self.head  # Add nodes values to list while iterating through them.
            while currNode is not None:
                vals.append(str(currNode.val))
                currNode = currNode.nextNode
            # Return values from list starting with a pipe, separated by a comma.
            return f"|{', '.join(vals)}"

    # Return canonical string representation of stack.
    def __repr__(self):
        vals = []
        if self.head is None:  # If stack is empty return pipe.
            return "|"
        else:
            currNode = self.head
            while currNode is not None:  # Add nodes values to list while iterating through them.
                vals.append(str(currNode.val))
                currNode = currNode.nextNode
            # Return values from list starting with a pipe, separated by a comma.
            return f"|{', '.join(vals)}"


# Unit Tests.
if __name__ == "__main__":
    stack = Stack()

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
