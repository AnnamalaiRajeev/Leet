# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, data):
        curr = self.head
        new_node = ListNode(data)
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def lenght_link(self):
        curr = self.head
        count = 0
        while curr.next:
            curr = curr.next
            count += 1

        return count

    def delete_node(self, index):
        if 1 <= index <= self.lenght_link():
            current_node = self.head
            count = 0
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next
                count += 1
                if count == index:
                    previous_node.next = current_node.next
                    current_node.next = None
                    return current_node
        else:
            return 0

    def __str__(self):
        current_node = self.head
        x = 'head'
        while current_node.next:
            current_node = current_node.next
            x += "-->" + str(current_node.val)
        return x

    def reverse_link_list(self):
        current = self.head.next
        previous = None
        while current.next:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        current.next = previous
        self.head.next = current

    def delete_n_from_last(self, i):
        self.reverse_link_list()
        self.delete_node(i)
        self.reverse_link_list()


if __name__ == "__main__":
    L1 = LinkedList()

    for i in range(1,7):
        L1.append(i)





