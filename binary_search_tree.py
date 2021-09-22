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

    def show(self,view='inOrder'):
        if self.root != None:
            if view == 'preOrder':
                self._show_preOrder(self.root)  # root left right  
            elif view == 'inOrder':
                self._show_inOrder(self.root)   # left root right  
            elif view == 'postOrder':
                self._show_postOrder(self.root) # left right root
            elif view == 'levelOrder':
                from collections import defaultdict
                self.order = defaultdict(list)
                level = 0 # root level
                self._show_levelOrder(self.root,level)
                for level_data in self.order.values():
                    for val in level_data:
                        print(val, end =' ')
            elif view == 'zigzag':
                output= []
                level = 0 # root level
                self._show_zigzag(self.root,level,output)
                for zigzag_item in output:
                    for val in zigzag_item:
                        print(val, end = ' ')
            elif view == 'left':
                self.left_side = {}
                height = 0 # root height
                self._show_leftview(self.root,height)
                for val in self.left_side.values():
                    print(val, end =' ')
            elif view == 'right':
                self.right_side = {}
                height = 0 # root height
                self._show_rightview(self.root,height)
                for val in self.right_side.values():
                    print(val, end =' ')
        print()

    def _show_preOrder(self,cur):
        if cur != None:
            print(str(cur.val), end =" ")
            self._show_preOrder(cur.left)
            self._show_preOrder(cur.right)

    def _show_inOrder(self,cur):
        if cur != None:
            self._show_inOrder(cur.left)
            print(str(cur.val), end =" ")
            self._show_inOrder(cur.right)

    def _show_postOrder(self,cur):
        if cur != None:
            self._show_postOrder(cur.left)
            self._show_postOrder(cur.right)
            print(str(cur.val), end =" ")

    def _show_levelOrder(self,cur,level):
        if cur != None:
            self.order[level].append(cur.val)
            self._show_levelOrder(cur.left,level+1)
            self._show_levelOrder(cur.right,level+1)

    def _show_zigzag(self,cur,level,output):
        if cur != None:
            if len(output) <= level:
                output += [[]]
            self._show_zigzag(cur.left,level+1,output)
            self._show_zigzag(cur.right,level+1,output)
            if level & 1 == 0: #level % 2 == 0
                output[level].append(cur.val)
            else:
                output[level].insert(0,cur.val) #prepend

    def _show_leftview(self,cur,height):
        if cur != None:
            if height not in self.left_side:
                self.left_side[height] = cur.val
                self._show_leftview(cur.left,height+1) # <-- important to call cur.left first
                self._show_leftview(cur.right,height+1)

    def _show_rightview(self,cur,height):
        if cur != None:
            if height not in self.right_side:
                self.right_side[height] = cur.val
                self._show_rightview(cur.right,height+1) # <-- important to call cur.right first
                self._show_rightview(cur.left,height+1)                     
            
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
        self.root = self._remove(self.root,val)

    def _remove(self,cur,val):
        if cur == None:
            return
        elif val < cur.val:
            cur.left = self._remove(cur.left,val)
        elif val > cur.val:
            cur.right = self._remove(cur.right,val)
        else:
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

    def is_symmetric(self):
        if self._is_symmetric(self.root,self.root):
            return True
        else:
            return False

    def _is_symmetric(self,cur1,cur2):
        if not cur1 and not cur2:
            return True
        elif not cur1 or not cur2:
            return False
        return (cur1.val == cur1.val) and self._is_symmetric(cur1.left,cur2.right) and self._is_symmetric(cur1.right,cur2.left)    

    def fill_randint(self,num_nodes=15,Min=0,Max=100):
        import random
        random_sample = random.sample(range(Min,Max),num_nodes) # to avoid Repeated values
        for val in random_sample:
            self.insert(val)
        del random_sample
        return self.root

    def diameter(self):
        self.res = 0 # static value (used globally).
        return self._diameter(self.root)
        
    def _diameter(self,cur): # using dfs concept
        if not cur:
            return -1
        left = self._diameter(cur.left)
        right = self._diameter(cur.right)
        self.res = max(self.res, 2 + left + right)
        return 1 + max(left,right)

if __name__ == "__main__":
    bst = BST()               
    bst.insert(8)        
    bst.insert(7)
    bst.insert(20)
    bst.insert(10)       
    bst.insert(16)       
    bst.insert(50)              
    bst.show()                   # 7 8 10 16 20 50  (default: view = inOrder)
    bst.show(view='preOrder')    # 8 7 20 10 16 50
    bst.show(view='postOrder')   # 7 16 10 50 20 8
    bst.show(view='levelOrder')  # 8 7 20 10 50 16
    bst.show(view='zigzag')      # 8 20 7 10 50 16
    bst.show(view='left')        # 8 7
    bst.show(view='right')       # 8 20 50
    print(bst.height())   # 4
    print(bst.exists(16)) # True
    bst.remove(8)         
    bst.show()            # 7 10 16 20 50
    bst.remove(7)        
    bst.show()            # 10 16 20 50
    print(bst.is_valid()) # True
    print(bst.is_symmetric()) #False

    bst_rand = BST()
    bst_rand.fill_randint()
    bst_rand.show()       # 0 6 12 16 19 32 37 52 53 58 63 73 83 95 99

    bst_rand = BST()
    bst_rand.fill_randint(12,-11,42) #(num_nodes, min, max)
    bst_rand.show()       # -8 -4 -2 2 3 9 18 22 29 30 33 39
    
    print(bst.diameter()) # 2


    
