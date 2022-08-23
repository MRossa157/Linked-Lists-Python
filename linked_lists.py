class Linkedlist:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None) -> None:
            self.element = element
            self.next_node = next_node

    def append(self, element) -> None:
        # Append element to list
        if not self.head:
            self.head = self.Node(element)
            return element

        node = self.head
        while node.next_node:
            node = node.next_node
        
        node.next_node = self.Node(element)

    def append_by_index(self, element, index) -> int:
        # Index = The index after which the element will be append
        i = 0
        node = self.head
        prev_node = self.head

        while i <= index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)
        return prev_node.next_node


    def get_element_by_index(self, index) -> int:
        i = 0
        node = self.head
        prev_node = self.head

        while i <= index:
            prev_node = node
            node = node.next_node
            i += 1

        return prev_node.element      

    def get_len(self) -> int:
        if not self.head:
            return 0

        i = 1
        node = self.head

        while node.next_node:
            node = node.next_node
            i += 1
        
        return i

    def delete(self, index) -> int:
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        
        prev_node.next_node = node.next_node
        element = node.element
        del node

        return element

    def out(self) -> None:
        # Print all list
        if not self.head:
            return print('List is empty')

        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def out_withIndex(self) -> None:
        if not self.head:
            return print('List is empty')
        i = 0
        node = self.head
        while node.next_node:
            print(node.element, '| index:', i)
            node = node.next_node
            i += 1
        print(node.element, '| index:', i)

        
linked_list = Linkedlist()
linked_list.append(324)
linked_list.append(12345)
linked_list.append(1323)
linked_list.append_by_index(7726, 1)
linked_list.out_withIndex()
print('----------')
linked_list.delete(2)
linked_list.out_withIndex()
print('----------')
#print(linked_list.get_element_by_index(3))
print(linked_list.get_len())