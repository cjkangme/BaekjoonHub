import sys, heapq

input = sys.stdin.readline

class Node(object):
    def __init__(self, data, depth=-1):
        self.data = data
        self.depth = depth
        self.children = dict()

    def __str__(self):
        return "--"*self.depth+self.data

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, datas):
        curr_node = self.head
        for data in datas:
            if curr_node.children.get(data) is None:
                curr_node.children[data] = Node(data, curr_node.depth + 1)
            curr_node = curr_node.children[data]

def DFS(node):
    sorted_children = sorted(node.children.items(), key=lambda x : x[0])
    for _, child in sorted_children:
        print(child)
        DFS(child)

if __name__ == "__main__":
    N = int(input())
    trie = Trie()
    
    for _ in range(N):
        foods = list(map(str, input().rstrip().split()))
        trie.insert(foods[1:])
    
    DFS(trie.head)