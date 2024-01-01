import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num):
        self.num = num
        self.children = []
    def append_child(self, num):
        self.children.append(num)

def make_tree(arr, num):
    temp_node = None
    next_node = Node(num)
    while arr:
        if arr[-1].num > next_node.num:
            if temp_node is None:
                arr[-1].append_child(next_node)
            else:
                temp_node.append_child(next_node)
            arr.append(next_node)
            return arr
        else:
            temp_node = arr.pop()
    temp_node.append_child(next_node)
    arr.append(next_node)
    return arr

def postfix(node):
    for child in node.children:
        postfix(child)
    print(node.num)

if __name__=="__main__":
    num = int(input())
    root = Node(num)
    arr = [root]
    while True:
        try:
            num = int(input())
            arr = make_tree(arr, num)
        except:
            break
    # 후위 순회
    postfix(root)
