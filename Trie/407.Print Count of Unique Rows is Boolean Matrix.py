class TrieNode:
    def __init__(self):
        self.child = [0]*2
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        cur = self.root
        n = len(key)
        for i in range(n):
            index = key[i]
            if not cur.child[index]:
                cur.child[index] = TrieNode()
            cur = cur.child[index]
        cur.end = True

    def search(self,key):
        cur = self.root
        n = len(key)
        for i in range(n):
            index = key[i]
            if not cur.child[index]:
                return False
            cur = cur.child[index]
        return cur.end

arr = [[0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0]]    

t = Trie()
c = 0
for i in arr:
    if not t.search(i):
        c += 1
        t.insert(i)
print(c)   








def printArray(matrix):
 
    rowCount = len(matrix)
    if rowCount == 0:
        return
 
    columnCount = len(matrix[0])
    if columnCount == 0:
        return
 
    row_output_format = " ".join(["%s"] * columnCount)
 
    printed = {}
 
    for row in matrix:
        routput = row_output_format % tuple(row)
        if routput not in printed:
            printed[routput] = True
            print(routput)
 
# Driver Code
mat = [[0, 1, 0, 0, 1],
       [1, 0, 1, 1, 0],
       [0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0]]
 
printArray(mat)
