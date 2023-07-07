class Node(object):
    def __init__(self):
        """
        Initialize node here
        """
        self.val = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        curr_node = self.head
        curr_index = 0
        while curr_node is not None:
            if curr_index == index:
                return curr_node.val
            curr_node = curr_node.next
            curr_index = curr_index + 1

        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node()
        new_node.val = val

        new_node.next = self.head
        self.head = new_node

        return

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node()
        new_node.val = val

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

        return

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node()
        new_node.val = val

        curr_node = self.head
        curr_index = 0

        if index <= 0:
            new_node.next = self.head
            self.head = new_node

        while curr_node is not None:
            if curr_index == index - 1:
                new_node.next = curr_node.next
                curr_node.next = new_node
                return
            curr_node = curr_node.next
            curr_index = curr_index + 1

        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        curr_node = self.head
        curr_index = 0

        if index < 0:
            return

        if index == 0:
            curr_node = curr_node.next
            self.head = curr_node
            return

        while curr_node.next is not None:
            if curr_index == index - 1:
                prev_node = curr_node
                node_to_delete = prev_node.next
                next_node = node_to_delete.next
                prev_node.next = next_node
                return
            curr_node = curr_node.next
            curr_index = curr_index + 1

        return


    def print(self):
        curr_node = self.head
        linked_list = 'head' + ' -> '
        while curr_node is not None:
            linked_list = linked_list + str(curr_node.val) + ' -> '
            curr_node = curr_node.next
        print(linked_list + 'None')
        return

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.print()
print(obj.get(0))
obj.addAtIndex(1, 2)
obj.print()
print(obj.get(0))
print(obj.get(1))
obj.addAtIndex(0, 1)
obj.print()
print(obj.get(0))
print(obj.get(1))