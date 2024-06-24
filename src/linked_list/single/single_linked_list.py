class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        self.size += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node does not exist')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            self.size -= 1
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        self.size -= 1
        current_node = None

    def append_v2(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def append_at_location(self, data, index):
        current_node = self.head
        prev_node = self.head
        new_node = Node(data)
        count = 1
        while current_node is not None:
            if index == 1:
                new_node.next = current_node
                self.head = new_node
                self.size += 1
                return
            elif count == index:
                new_node.next = current_node
                prev_node.next = new_node
                self.size += 1
                return
            count += 1
            prev_node = current_node
            current_node = current_node.next

        if count < index:
            print("The list has less number of elements")

    def iter(self):
        current_node = self.head

        while current_node:
            val = current_node.data
            current_node = current_node.next
            yield val

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
            return False

    def size_of_list(self):
        count = 0
        for node in self.iter():
            count += 1
        return count

    def delete_node_at_pos(self, pos):
        if self.head:
            current_node = self.head
            if pos == 0:
                self.head = current_node.next
                self.size -= 1
                current_node = None
                return

            prev_node = None
            count = 0
            while current_node and count != pos:
                prev_node = current_node
                current_node = current_node.next
                count += 1

            if current_node is None:
                return

            prev_node.next = current_node.next
            self.size -= 1
            current_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def clear(self):
        # clear the entire list.
        self.tail = None
        self.head = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.insert_after_node(llist.head.next, "E")

llist.delete_node("B")
llist.delete_node("E")

llist.append_at_location("B", 2)
llist.append_at_location("B", 3)
llist.append_at_location("A", 3)

llist.delete_node_at_pos(0)
print("---------------------------")
llist.print_list()
print("---------------------------")
for letter in llist.iter():
    print(letter)
print("--------Search-------------")
print(llist.search('A'))
print(llist.search('F'))
print("--------Size---------------")
print(str(llist.size_of_list()))
print(str(llist.size))
print(llist.len_iterative())
print(llist.len_recursive(llist.head))
print("--------Clear---------------")
llist.clear()
