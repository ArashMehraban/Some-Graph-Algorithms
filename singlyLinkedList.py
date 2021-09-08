class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # adds a node with a given value to the linked list
    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # returns the size of the linked list
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    # displays the elements in linked list
    def display(self):
        cur = self.head
        print('[',end='')
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')
   
    # returns the value at the given index
    def get(self, index):
        if self.head == None or index < 0:
            return 
        cur = self.head
        idx_count = 0
        while cur.next is not None and idx_count < index:
            cur = cur.next
            idx_count += 1
        if idx_count == index:
            return cur.data
        else:
            return 

    # inserts a value at a given index
    def insert(self, index, data):
        if index < 0:
            return 
        if index == 0:
            self.add(data)
            return
        if self.head == None and index > 0:
            return         
        cur = self.head
        idx_count = 0
        while cur.next is not None:
            prev = cur
            cur = cur.next            
            idx_count += 1
            if idx_count == index:
                node = Node(data)
                prev.next = node
                node.next = cur
                return 
            
    # updates a node's value with a given value at a given index
    def update(self, index, data):
        if index < 0:
            return
        cur = self.head
        idx_count = 0
        while cur.next is not None:
            if idx_count == index:
                cur.data = data
                return
            cur = cur.next
            idx_count += 1
                
    # removes a node at a given index
    def remove(self, index):
        if(index < 0):
            return
        cur = self.head   
        if index == 0:
            self.head = cur.next
            cur = None
            return
        else:
            idx_count = 0
            while cur.next is not None:
                prev = cur
                cur = cur.next
                idx_count += 1
                if idx_count == index:
                    prev.next = cur.next
                    return
    # reverses the link-list
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # reverses the link-list recuresively
    def reverse_recursively(self):
        def rec(prev,cur):
            if not cur:
                return prev            
            self.head = rec(cur,cur.next)
            cur.next = prev            
            return self.head
        return rec(None,self.head)


if __name__ == "__main__":

    sll = LinkedList()
    sll.display()  #[]
    print('Size: {}\n'.format(sll.length())) #0

    print('---------------------------')
    
    sll.add(10)
    sll.add(0)
    sll.add(37)
    sll.add(-4)
    sll.add(-5)
    sll.add(64)
    sll.display() #[64 -5 -4 37 0 10 ]
    print('Size: {}\n'.format(sll.length())) #6
    
    print('---------------------------')

    sll.display() # [64 -5 -4 37 0 10 ]
    print(sll.get(-1)) #None due to invalid index
    print(sll.get(0))  #64
    print(sll.get(1))  #-5 
    print(sll.get(2))  #-4
    print(sll.get(3))  #37
    print(sll.get(4))  #0
    print(sll.get(5))  #10
    print(sll.get(6))  #None due to invalid index
    
    print('---------------------------')

    sll.insert(0, 330) 
    sll.display()   #[330 64 -5 -4 37 0 10 ]
    sll.insert(3, 50) 
    sll.display()   #[330 64 -5 50 -4 37 0 10 ]

    print('---------------------------')

    sll.update(0, 700)
    sll.display() #[700 64 -5 50 -4 37 0 10 ]
    sll.update(4, -400)
    sll.display() #[700 64 -5 50 -400 37 0 10 ]
    sll.update(-1, 500)
    sll.display() #[700 64 -5 50 -4 37 0 10 ] <-- No change due to invalid index
    sll.update(10, 100)
    sll.display() #[700 64 -5 50 -400 37 0 10 ] <-- No change due to invalid index

    print('---------------------------')
    
    sll.display() #[700 64 -5 50 -400 37 0 10 ]
    sll.remove(0)
    sll.display() #[64 -5 50 -400 37 0 10 ]
    sll.remove(1)
    sll.display() #[64 50 -400 37 0 10 ]
    sll.remove(5)
    sll.display() #[64 50 -400 37 0 ]
    sll.remove(5)
    sll.display() #[64 50 -400 37 0 ]  <-- No change due to invalid index

    print('---------------------------')

    sll.display() #[64 50 -400 37 0 ] <--current list
    sll.reverse()
    sll.display() #[0 37 -400 50 64 ] 
    sll.reverse()
    sll.display() #[64 50 -400 37 0 ]

    print('---------------------------')

    sll.display() #[64 50 -400 37 0 ] <--current list
    sll.reverse_recursively()
    sll.display() #[0 37 -400 50 64 ]
    sll.reverse_recursively()
    sll.display() #[64 50 -400 37 0 ]


