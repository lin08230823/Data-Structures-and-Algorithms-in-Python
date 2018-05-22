# -*- coding:utf-8 -*-

#二叉树结点类
class BinTNode:
	def __init__(self, dat, left=None, right=None)
		self.data = dat
		self.left = left
		self.right = right

def count_BinTNodes(t):
	if t is None:
		return 0
	else:
		return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

#深度优先遍历 使用递归遍历二叉树 先根序遍历
def preorder(t): #proc是具体的结点数据操作
	if t is None:
		print("-", end="") #空树输出-
		return
	print("(" + str(t.data), end="")
	preorder(t.left)
	preorder(t.right)
	print(")", end="")

class BinTree:
	def __init(self):
		self._root = None

	def is_empty(self):
		return self._root is None

	def root(self):
		return self._root

	def leftchild(self):
		return self._root.left

	def rightchild(self):
		return self._root.right

	def set_root(self, rootnode):
		self._root = rootnode

	def set_left(self, leftnode):
		self._root.left = leftnode

	def set_right(self, rightnode):
		self._root.right = rightnode
