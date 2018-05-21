# -*- coding:utf-8 -*-
class LinkedListUnderflow(ValueError):
	pass

class LNode: #链表结点类
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_


class LList:  #链表类
	def __init__(self):
		self._head = None
	
	def is_empty(self):
		return self._head is None
	
	def prepend(self, elem):
		self._head = LNode(elem, self._head)
	
	def pop(self):#表头取值
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem
		self._head = self._head.next
		return e

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return
		p = self._head
		while p.next is not None:
			p = p.next
		p.next = LNode(elem)

	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_last")
		p = self._head
		if p.next is None:
			e = p.elem
			p = None
			return e
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		return e

	def find(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				return p.elem
			p = p.next

	def printall(self):
		p = self._head
		while p is not None:
			print(p.elem, end = '')
			if p.next is not None:
				print(', ', end='')
			p = p.next
		print('')

	def elements(self):#定义可迭代对象
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next

	def filter(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				yield p.elem
			p = p.next

class LList1(LList): 
	def __init__(self):
		LList.__init__(self)
		self._rear = None

	def prepend(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._head = LNode(elem, self._head)

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._rear.next = LNode(elem)
			self._rear = self._rear.next

	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_last")
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			return e
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		self._rear = p
		return e

class LClist:
	def __init__(self):
		self._rear = None

	def is_empty(self):
		return self._rear is None

	def prepend(self, elem):
		p = LNode(elem)
		if self._rear is None:
			p.next = p
			self._rear = p
		else:
			p.next = self._rear.next
			self._rear.next = p
