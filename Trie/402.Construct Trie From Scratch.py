class TrieNode:
    def __init__(self):
        self.child = [0]*26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        cur = self.root
        n = len(key)
        for i in range(n):
            index = ord(key[i]) - ord("a")
            if not cur.child[index]:
                cur.child[index] = TrieNode()
            cur = cur.child[index]
        cur.end = True

    def search(self,key):
        cur = self.root
        n = len(key)
        for i in range(n):
            index = ord(key[i]) - ord("a")
            if not cur.child[index]:
                return False
            cur = cur.child[index]
        return cur.end

    def isempty(self,root):
        for i in range(26):
            if root.child[i]:
                return False
        return True

    def delete(self , root ,  key , i):
        if root == None:
            return None

        if i == len(key):
            root.end = False
            if self.isempty(root):
                root = None
            return root

        index = ord(key[i]) - ord("a")
        root.child[index] = self.delete(root.child[index] , key , i+1)

        if self.isempty(root) and root.end == False:
            root = None

        return root    


    def delete_naive(self,key):
        cur = self.root
        n = len(key)
        if self.search(key):
            for i in range(n):
                index = ord(key[i]) - ord("a")
                cur = cur.child[index]

            cur.end = False    


t = Trie()
keys = ["the","a","there","anaswe","any", "bye" ,
        "by","their"]

for key in keys:
    t.insert(key)

t.delete(t.root , "the" , 0)
print(t.search("the"))
