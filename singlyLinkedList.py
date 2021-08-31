class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# This is a Singly Linked List


class LinkedList:
    def __init__(self):
        self.head = Node()

    # adds a node with a given value to the end of the linked list
    def add(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    # returns the size of the linked list
    def length(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    # displays the elements in linked list
    def display(self):
        cur = self.head
        elems = []
        while cur.next is not None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
    # returns the value at the given index

    def get(self, index):
        if(index >= self.length()):
            print('LinkedList has less elements than {}'.format(index))
            return
        cur = self.head
        idx_count = 0
        while idx_count <= index:
            cur = cur.next
            idx_count += 1
        return cur.data

    # inserts a value at a given index
    def insert(self, index, data):
        if(index < 0):
            print('ERROR: Not a valid index!')
            return
        ll_length = self.length()
        if(index > ll_length+1):
            print('LinkedList size was {}. You inserted in index {}.\nUnset\
            indecies were set to \'None\'\n'.format(
                ll_length, index))
            diff = index - ll_length
            for i in range(diff-1):
                self.add(None)
            self.add(data)
        else:
            cur = self.head
            idx_count = 0
            while True:
                last_node = cur
                cur = cur.next
                if(idx_count == index):
                    new_node = Node(data)
                    last_node.next = new_node
                    new_node.next = cur
                    return
                idx_count += 1

    # removes a node at a given index
    def remove(self, index):
        if(index < 0):
            print('ERROR! Invalid index ({}) to be removed!\n'.format(index))
            return
        if(index >= self.length()):
            print('LinkedList has less elements than {}'.format(index))
            return
        cur = self.head
        idx_count = 0
        while True:
            last_node = cur
            cur = cur.next
            if(idx_count == index):
                last_node.next = cur.next
                return
            idx_count += 1

    # updates a node's value with a given value at a given index
    def update(self, index, data):
        if(index >= self.length()):
            print('LinkedList is samller is samller than {} elements'.format(index))
            return
        cur = self.head
        idx_count = 0
        while True:
            cur = cur.next
            if(idx_count == index):
                cur.data = data
                return
            idx_count += 1


if __name__ == "__main__":

    print('\n')
    print('Tesing our LinkedList in Python...')
    print('\n')
    sll = LinkedList()
    print('An empty Singly LinkedList created')
    print('\n')
    print('Current LinkedList:')
    sll.display()
    print('Current size of LinkedList: {}'.format(sll.length()))
    print('\n')
    print('Some numbers were added to the LinkedList...')
    sll.add(10)
    sll.add(0)
    sll.add(37)
    sll.add(-4)
    sll.add(-5)
    sll.add(64)
    print('Current LinkedList:')
    sll.display()
    print('Current size of the LinkedList: {}'.format(sll.length()))
    print('\n')
    print('Value 3 was added to index 3:')
    print('Current LinkedList:')
    sll.insert(3, 3)
    sll.display()
    print('Current size of the LinkedList: {}'.format(sll.length()))
    print('\n')
    print('Value 8 was added to index 10. READ THE MESSAGE BELOW from function!!')
    sll.insert(10, 8)
    print('Current LinkedList:')
    sll.display()
    print('\n')
    print('Index 8 was updated with value 7:')
    sll.update(8, 7)
    print('Current LinkedList:')
    sll.display()
    print('\n')
    print('Index 8 was updated with value -100 again:')
    sll.update(8, -100)
    print('Current LinkedList:')
    sll.display()
    print('\n')
    print('A value was tried to be added to index -7:')
    sll.insert(-7, 21)
    print('Current LinkedList:')
    sll.display()
    print('\n')
    print('The first element was removed from LinkedList')
    sll.remove(0)
    print('Current LinkedList:')
    sll.display()
    print('\n')
