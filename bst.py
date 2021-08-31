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
			self.root=Node(val)
		else:
			# self.root indicates the current node for inseration
			self._insert(val,self.root)

	def _insert(self,val,cur): # root is replaced with cur to represent cur node for insertion in recursion
		if val < cur.val:
			if cur.left == None:
				cur.left = Node(val)
			else:
				self._insert(val,cur.left)
		elif val > cur.val:
			if cur.right == None:
				cur.right=Node(val)
			else:
				self._insert(val,cur.right)
		else:
			print("Repeated Value!")

	def show(self):
		if self.root != None:
			self._show(self.root)
		print()
	
	def _show(self, cur):
		if cur != None :
			self._show(cur.left)
			print(str(cur.val), end =" ")
			self._show(cur.right)
	
	def height(self):
		if self.root != None:
			return self._height(self.root,0)
		else:
			return 0
	
	def _height(self,cur,cur_height): # store the height in each recursive call
		if cur == None:
			return cur_height
		left_height = self._height(cur.left,cur_height+1)
		right_height = self._height(cur.right,cur_height+1)
		return max(left_height, right_height)
	
	def search(self,val):
		if self.root != None:
			return self._search(val, self.root)
		else:
			return None

	def _search(self,val,cur):
		if val == cur.val:
			return cur
		elif val < cur.val and cur.left != None:
			return self._search(val, cur.left)
		elif val > cur.val and cur.right != None:
			return self._search(val,cur.right)
	
	def exist(self,val):
		if self.search(val): 
			return True
		else:
			return False

	def remove(self,val):
		if self.root != None:
			return self._remove(val,self.root)
		else:
			return None
	
	def _remove(self,val,cur):
		if cur == None:
			return
		if val == cur.val:
			if not cur.left and not cur.right: # leaf node
				return None 
			if not cur.left and cur.right: # node with 1 right child
				return cur.right
			if cur.left and not cur.right: # node with 1 left child
				return cur.left
			if cur.left and cur.right: # node with 2 children
				# Point to the right child of the current node and go
				# all the way down to the left to find the smallest value
				# that is larger than val for replacement
				smallest = cur.right
				while smallest.left:
					smallest = smallest.left
				cur.val = smallest.val
				cur.right = self._remove(cur.val,cur.right)
		elif val < cur.val:
			cur.left = self._remove(val,cur.left)
		elif val > cur.val:
			cur.right = self._remove(val,cur.right)
		return cur
		
###### Helper Function to pupulate a Tree ###########
def fill_tree(tree, num_nodes=100, max_int=1000):
		from random import randint
		for _ in range(num_nodes):
			cur_val = randint(0,max_int)
			tree.insert(cur_val)
		return tree
####################################################

if __name__ == "__main__":
	bst = BST()              # (Binary Search Tree (BST) created)
	#bst = fill_tree(bst)
	bst.insert(10)           # (10 added)
	bst.insert(8)            # (8 added)
	bst.insert(25)           # (25 added)
	bst.insert(17)           # (17 added)
	bst.insert(20)           # (20 added)
	bst.insert(50)           # (50 added)
	bst.insert(16)           # (16 added)
	bst.show()               # 8 10 16 17 20 25 50
	print('BST\'s height: ',bst.height())
	print(bst.exist(16))     # BST's height:  4
	bst.remove(16)           # (16 removed)
	bst.show()               # 8 10 17 20 25 50
	bst.remove(8)            # (8 removed: root)
	bst.show()               # 10 17 20 25 50
	bst.remove(50)           # (50 removed : leaf)
	bst.show()               # 10 17 20 25
