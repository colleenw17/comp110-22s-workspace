from __future__ import annotations

from typing import Union
# from typing import Optional


class Node:
    data: int
    # Optionally a Node
    next: Union[Node, None]
    # next: Optional[Node]

    def __init__(self, data: int, next: Union[Node, None]) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """"String representation of object it's called on."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

 
def sum(node: Node) -> int:
    """Recursive function. """
    if node.next is None:
        # Solves base case where we know node sum 3 
        # Base case
        return node.data 
    else:
        # data plus the sum of the rest of the list
        # Recursive case
        return node.data + sum(node.next)
         
# def sum(node: Optional[Node]) -> int:
    # if node == None:
    #     return 0 
    # else:
    #     return node.data + sum(node.next)


def count(node: None, current_count: int = 0) -> int:
    if node.next is None:
        return current_count + 1
    else:
        # example of tail recursive function
        return count(node.next, current_count + 1)

# def count(node: Optional[Node], current_count: int = 0) -> int:
    # if node == None:
    #     return current_count
    # else:
    #     # example of tail recursive function
    #     return count(node.next, current_count + 1)

# head: Node = Node(1, None)
# tail: Node = Node(2, None)
# head.next = tail


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)