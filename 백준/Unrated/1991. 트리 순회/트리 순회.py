import sys
input = sys.stdin.readline

def char_to_num(char):
    if char == '.':
        return -1
    return ord(char) - ord('A')

def preorder(node, tree):
    print(chr(node+ord('A')), end='')
    for child in tree[node]:
        if child != -1:
            preorder(child, tree)
        
def inorder(node, tree):
    left, right = tree[node]
    if left != -1:
        inorder(left, tree)
    print(chr(node+ord('A')), end='')
    if right != -1:
        inorder(right, tree)

def postorder(node, tree):
    for child in tree[node]:
        if child != -1:
            postorder(child, tree)
    print(chr(node+ord('A')), end='')

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N):
    parent, left, right = map(str, input().rstrip().split())
    parent, left, right = char_to_num(parent), char_to_num(left), char_to_num(right)
    tree[parent] = (left, right)

preorder(0, tree)
print()
inorder(0, tree)
print()
postorder(0, tree)