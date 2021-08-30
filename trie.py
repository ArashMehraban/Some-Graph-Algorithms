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

	def remove(self, word):
		cur = self.root
		for char in word:
			if char not in cur.children:
				print('Word does not exist!')
				return
			cur = cur.children[char]
		if cur.end_of_word == False:
			print('Word does not exist!')
			return
		else:
			cur.end_of_word = False

                

if __name__ == "__main__":
	trie = Trie()
	trie.insert('Apple')
	trie.insert('Appleii')
	print(trie.search('Apple'))     #True
	print(trie.search('App'))       #False
	print(trie.search('Appleii'))   #True
	print(trie.starts_with('App'))  #True
	print(trie.starts_with('bob'))  #False
	trie.remove('Apb')              #Word does not exist
	trie.remove('Apple')            #<-- Apple gets removed
	trie.remove('Apple')            #Word does not exist

