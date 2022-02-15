import sys
input = sys.stdin.readline 
N = int(input())
btree = {}

class Node:
  def __init__(self, root, left, right) :
    self.root = root
    self.left = left
    self.right = right

for _ in range(N):
  root, left, right = map(str, input().split())
  btree[root] = Node(root=root, left=left, right=right)

def preorder(node):    # 전위 root, left, right
  print(node.root, end='')
  if node.left != '.':
    preorder(btree[node.left])
  if node.right != '.':
    preorder(btree[node.right])


def inorder(node):    # 중위 left, root, right
  if node.left != '.':
    inorder(btree[node.left])
  print(node.root, end='')
  if node.right != '.':
    inorder(btree[node.right])

def postorder(node):  # 후위 left, right, root
  if node.left != '.':
    postorder(btree[node.left])
  if node.right != '.':
    postorder(btree[node.right])
  print(node.root, end='')


preorder(btree['A'])
print()
inorder(btree['A'])
print()
postorder(btree['A'])