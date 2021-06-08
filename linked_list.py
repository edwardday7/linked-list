#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Allows us to print the list with arrows
        between the elements, if the list is not
        empty.
        """

        if self.head is None:
            return "The list is empty."
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next
        return " -> ".join(nodes)

    def insert(self, data):
        """
        Inserts a node at the end of the list
        iteratively. 
        """
        if self.head is None:       # List is empty
            self.head = Node(data)

        node = self.head
        while node.next:            # Iterate until end
            node = node.next
        node.next = Node(data)

    def recursive_insert_helper(self, data, node):
        """
        Helper function for recursive insert method
        """
        if node.next is None:
            node.next = Node(data)
            return
        return self.recursive_insert_helper(data, node.next)
            

    def recursive_insert(self, data):
        """
        Insert node at the end of the list recursively
        """
        if self.head is None:
            return
        return self.recursive_insert_helper(data, self.head)

    def reverse(self):
        """
        Reverses the given linked list iteratively.
        """ 
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recursive_reverse_helper(self, node, prev = None):
        """
        Recursive helper method for the recursive reverse method
        """
        if node is None:
            self.head = prev
            return
        current = node
        next = node.next
        node.next = prev
        return self.recursive_reverse_helper(next, current)
        

    def recursive_reverse(self):
        """
        Recursively reverse the linked list
        """
        if self.head is None:
            return
        return self.recursive_reverse_helper(self.head)


def main():

    ll = LinkedList()
    n1 = Node("A")
    ll.head = n1

    # Insert some elements
    ll.insert("B")
    ll.insert("C")
    ll.recursive_insert("D")
    ll.recursive_insert("E")
    print(ll)

    # Reverse the list
    ll.reverse()
    print(ll)

    # Recursively reverse the list
    ll.recursive_reverse()
    print(ll)


    return



if __name__ == "__main__":
    main()