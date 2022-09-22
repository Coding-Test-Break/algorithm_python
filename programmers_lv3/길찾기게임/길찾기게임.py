import sys

sys.setrecursionlimit(10**6)

answer = [[], []]
class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def append(self, node):
        self.recur_append(self.root, node)
        
    def recur_append(self, target, node):
        if node.compare(target) < 0:
            if target.left:
                self.recur_append(target.left, node)
            else:
                target.left = node
        elif node.compare(target) > 0:
            if target.right:
                self.recur_append(target.right, node)
            else:
                target.right = node
    
    def pre_order(self):
        self.pre_recur(self.root)
        
    def pre_recur(self, node):
        if not node:
            return 
        global answer
        answer[0].append(node.value)
        self.pre_recur(node.left)
        self.pre_recur(node.right)
        
    def post_order(self):
        self.post_recur(self.root)
    
    def post_recur(self, node):
        if not node:
            return 
        global answer
        self.post_recur(node.left)
        self.post_recur(node.right)
        answer[1].append(node.value)
                
class Node:
    def __init__(self, x, value):
        self.x = x
        self.value = value
        self.left = None
        self.right = None

    def compare(self, node):
      if self.x > node.x:
        return 1
      elif self.x < node.x:
        return -1
      else:
        return 0

def solution(nodeinfo):
    kv = dict()
    for i, v in enumerate(nodeinfo):
        v = tuple(v)
        kv[v] = i + 1 
        
    # O(nlogn) 
    nodeinfo.sort(reverse = True, key = lambda x: x[1])

    btree = None
    
    # nlogn
    # O(n) - 10,000
    for i, v in enumerate(nodeinfo):
        v = tuple(v)
        if i == 0:
            root = Node(v[0], kv[v])
            btree = BinaryTree(root)
            continue
        # O(logn)
        btree.append(Node(v[0], kv[v]))
        
    # O(2^log_2n) = O(n)
    btree.pre_order()
    btree.post_order()
    
    return answer

# 시간복잡도도 널널하고 BST만 구현할 줄 알면 풀 수 있는 문제 
# 병목구간은 O(nlogn)