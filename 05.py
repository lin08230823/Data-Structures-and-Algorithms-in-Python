# -*- coding:utf-8 -*-
#栈 后进先出 Last in First out
#队列 先进先出 First in First out
class StackUnderflow(ValueError): #空栈访问
	pass

class SStack:                   #基于顺序表技术实现的栈类
	def __init__(self):			#用list对象_elems存储栈中元素
		self._elems = []			#所有的栈操作映射到list操作

	def is_empty(self):
		return self._elems == []

	def top(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self.elems[-1]

	def push(self, elem):
		self._elems.append(elem)

	def pop(self):
		if self.elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems.pop()

class LNode:
	def __init__(self, elem, next=None):
		self.elem = elem
		self.next = next

class LStack:                  #栈的链接表实现
	def __init__(self):
		self._top = None

	def is_empty(self):
		return self._top is None

	def top(self):
		if self._top is None:
			raise StackUnderflow("in LStack.top()")
		return self._top.elem

	def push(self, elem):
		self._top = LNode(elem, self._top)

	def pop(self):
		if self._top is None:
			raise StackUnderflow("in LStack.top()")
		self._top = self._top.next
		return self._top.elem

list1 = ['d','s','e',2,4,]
st1 = SStack()
for x in list1:
	st1.push(x)
list2 = []
while not st1.is_empty():
	list2.append(st1.pop())
