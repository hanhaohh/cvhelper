from exception import Error_LinkList
class Node(object):
	__slots__ = "word", "docId","count","_next"
	def __init__(self,word = None,docId =None,count= None,node=None):
		self.word = str(word)
		self.docId = int(docId)
		self.count = int(count)
		self._next = node
	@property
	def next_node(self):
		return self._next
	@next_node.setter
	def next_node(self,value):
		if isinstance(value,Node):
			self._next = value
		else:
			raise Error_LinkList("The next node have to be an intance of Node")
	def __str__(self):
		return "Word %s @ Doc-ID %s Frequence is %s" %(self.word,str(self.docId),str(self.count))
		# return str(self.docId)
class LinkedList(object):
	def __init__(self,head =None,tail = None):
		self.head = head
		self.tail = tail 
		self.size = 0 

	def append(self,node = None):
		if self.head is None:
			self.head = node 	
			self.tail = node
		else:
			if node.docId >self.tail.docId:
				self.tail.next_node = node 
				self.tail = node 
			else:
				pre_node = self.head
				trav_node = self.head
				while trav_node:
					if trav_node.docId < node.docId:
						pre_node = trav_node
						trav_node = trav_node.next_node
					else:
						break
				if  trav_node ==  self.head:
 					node.next_node = self.head
 					self.head = node
 				else:
 					node.next_node = trav_node
 					pre_node.next_node = node
	 	self.size = self.size + 1

	def if_exist(self,node):
		word = node.word
		trav_node = self.head
		while trav_node:
			if  trav_node.word == word:
				return True  
			trav_node = trav_node.next_node
	def get_doc_ID(self):
		trav_node = self.head
		li = []
		first = 1
		while trav_node:
			for i in range(first,trav_node.docId+1):
				if i == trav_node.docId:
					li.append(trav_node.count)
				else:
					li.append(0)
			if trav_node.docId:
				first = trav_node.docId+1
				trav_node = trav_node.next_node
		while (2000-first):
			first = first + 1
			li.append(0) 
		return li
	def  __getitem__(self, key):
		trav_node = self.head 
		try:
			while (key):
				key = key - 1 
				trav_node = trav_node.next_node
			return trav_node
		except:
			return None

	def __str__(self):
		if self.size != 0 :
	 		return "Linkedlist Head word @ %s and the Tail word@ %s,size is %s" %(self.head.word,self.tail.word,self.size)
	 	else:
	 		return "empty list"


if __name__ == "__main__":
	ll = LinkedList()
	a = Node("hao","1","1")
	b= Node("hao","5","2")
	c = Node("hanha","7","3")
	d = Node("he","8","4")
	e = Node("he","8","4")
	f = Node("hes","8","4")

	ll.append(a)
	print "***"
	ll.append(b)
	print "***"
	ll.append(c)
	print "***"
	ll.append(d)
	print "***"
	ll.append(e)
	print "***"
	ll.append(f)
	print ll[0],ll[1],ll[2],ll[3],ll[4],ll[5],ll[6]


