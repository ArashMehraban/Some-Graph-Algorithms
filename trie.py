class Node:
    def __init__(self):
        self.children = {}
        self.end = False  #end of word

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        cur  = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.end = True

    def exists(self,word):
        cur  = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.end:
            return True
        else:
            return False

    def starts_with(self,prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur  = cur.children[char]
        return True

    def remove(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                print('Word does not exists')
                return
            cur = cur.children[char]
        if cur.end == False:
            print('Word does not exists')
            return
        else:
            cur.end = False

    def _suggest(self,cur,key):
        if cur.end == True:
            print(key)
        for added_letter,new_cur in cur.children.items():
            self._suggest(new_cur,key + added_letter )

    def auto_complete(self,key):
        cur  = self.root
        for char in key:
            if char not in cur.children:
                return
            cur = cur.children[char]
        self._suggest(cur,key)
        

if __name__ == "__main__":
    trie= Trie()
    trie.insert('Apple')            # (inserted Apple)
    trie.insert('Appleii')          # (inserted Appleii)
    print(trie.exists('Apple'))     # True
    print(trie.exists('App'))       # False
    print(trie.exists('Appleii'))   # True
    print(trie.starts_with('App'))  # True
    print(trie.starts_with('Abob')) # False
    print(trie.starts_with('bob'))  # False
    trie.remove('Apb')              # Word does not exists
    trie.remove('Apple')            # (removed Apple)
    trie.remove('Apple')            # Word does not exists
    trie.insert('Appzad')           # (inserted Appzad)
    trie.auto_complete('App')       # Appleii
                                    # Appzad
    
        
