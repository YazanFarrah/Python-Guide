# Exercise 12 - LinkedList

# Write a program to implement a linked list. Define a class 'Node'
# to represent individual elements in the linked list, and a class 'LinkedList'
# to manage the overall linked structure. Include methods to append elements
# to the end of the list('append'), and display the contents of the linked list
# ('display').
# Provide an example demonstrating the usage of your linked list implementation
# by creating an instance of the 'LinkedList' class, appending a few elements,
# and displaying the final linked list.

# Note Ensure that you handle edge cases appropriately. There's no need of
# inputting elements.

# The basic components of a linked list are:
# Node: Each element in a linked list is represented by a node. A node contains
# two fields - data and a reference (or link) to the next node in sequence.
# Head: The starting point of the linked list is called the head. It's a
# reference to the first node in the list.
# None: The last node in the linked list points to null or None,
# indicating the end of the list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None  # Initially None, in case there was another element added, we remove none and add the
        # reference to the added element


class LinkedList:
    def __init__(self):
        self.head = None  # Initially None as we haven't added any element yet

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # Because if head is none, then we make the head as the newly added node
            self.head = new_node
        # else:
        # self.head.next_node = new_node this is wrong, because we are assuming the next node, we need to loop over all nodes
        # and find the latest one "The one that points at None" and then we make it's head point at the newly added node

        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node  # for the loop to break when the condition is met
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next_node  # for the loop to break when the condition is met
        print('None')  # Because the condition checks if none it doesn't enter anymore, and I want to show that the last
        # node points at None


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()
