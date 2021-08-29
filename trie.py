class Node:
	def __init__(self):
		self.children = {}
		self.end_of_word = False

class Trie:
	def __init__(self):
		self.root = Node()
	
	def insert(self, word):
		cur  = self.root
		for char in word:
			if char not in cur.children:
				cur.children[char] = Node()
			cur = cur.children[char]
		cur.end_of_word = True
				
	def search(self, word):
		cur = self.root
		for char in word:
			if char not in cur.children:
				return False
			cur = cur.children[char]
		if cur.end_of_word:
			return True
		else:
			return False

	def starts_with(self, prefix):
		cur = self.root
		for char in prefix:
			if char not in cur.children:
				return False
			cur = cur.children[char]
		return True

if __name__ == "__main__":
	trie = Trie()
	trie.insert('Apple')
	trie.insert('Appleii')
	print(trie.search('Apple'))
	print(trie.search('App'))
	print(trie.search('Appleii'))
	print(trie.starts_with('App'))
