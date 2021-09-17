class Node:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            # self.root indicates the current node for insertion
            self._insert(val,self.root)

    def _insert(self,val,cur):
        if val < cur.val:
            if cur.left == None:
                cur.left = Node(val)
            else:
                self._insert(val,cur.left)
        elif val > cur.val:
            if cur.right == None:
                cur.right = Node(val)
            else:
                self._insert(val,cur.right)
        else:
            print('Repeated value')

    def show(self):
        if self.root != None:
            self._show(self.root)
        print()

    def _show(self,cur):
        if cur != None:
            self._show(cur.left)
            print(str(cur.val), end =" ")
            self._show(cur.right)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)

    def _height(self,cur, cur_height):
        if cur == None:
            return cur_height
        left_height = self._height(cur.left,cur_height+1)
        right_height = self._height(cur.right,cur_height+1)
        return max(left_height, right_height)

    def search(self,val):
        if self.root != None:
            return self._search(self.root,val)
        else:
            return None

    def _search(self,cur,val):
        if val == cur.val:
            return cur
        elif val < cur.val and cur.left != None:
            return self._search(cur.left,val)
        elif val > cur.val and cur.right != None:
            return self._search(cur.right,val)

    def exists(self,val):
        if self.search(val):
            return True
        else:
            return False

    def remove(self,val):
        if self.root != None:
            return self._remove(self.root,val)
        else:
            return None

    def _remove(self,cur,val):
        if cur == None:
            return
        if val == cur.val:
            if not cur.left and not cur.right: #leaf node
                return None
            if not cur.left and cur.right: #node with 1 right child
                return cur.right
            if cur.left and not cur.right: #node with 1 left child
                return cur.left
            if cur.left and cur.right: #node with 2 children
                # Point to the right child of the current node and go
                # all the way down to the left to find the smallest
                # value that is larger than val for replacement
                smallest = cur.right
                while smallest.left:
                    smallest = smallest.left
                cur.val = smallest.val
                cur.right = self._remove(cur.right,cur.val)
        elif val < cur.val:
            cur.left = self._remove(cur.left,val)
        elif val > cur.val:
            cur.right = self._remove(cur.right,val)
        return cur

    def is_valid(self):
        import sys
        return self._is_valid(self.root,Min=-sys.maxsize,Max=sys.maxsize)

    def _is_valid(self,cur,Min,Max):
        if cur == None:
            return True
        if (cur.val > Min and cur.val < Max and
            self._is_valid(cur.left, Min, cur.val) and
            self._is_valid(cur.right, cur.val, Max)):
            return True
        else:
            return False
        
        

if __name__ == "__main__":
    bst = BST()               
    bst.insert(8)        
    bst.insert(7)
    bst.insert(20)
    bst.insert(10)       
    bst.insert(16)       
    bst.insert(50)              
    bst.show()            # 7 8 10 16 20 50
    print(bst.height())   # 4
    print(bst.exists(16)) # True
    bst.remove(7)         # (remove leaf)
    bst.show()            # 8 10 16 20 50
    bst.remove(10)         #(remove root)
    bst.show()            # 10 17 20 25 50
    print(bst.is_valid()) # True
