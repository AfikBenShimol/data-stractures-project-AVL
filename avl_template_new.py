#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  




class AVLNode(object):
	""" AVL Node
		--------
		A class represnting a node in an AVL tree
		@inv: for each node, left.value <= value < node.right.value # BST
		@inv: for each node, abs(left.height - right.height) <= 1   # AVL
		
		fields
		------
			value: data held in node @type: str @default: None
		
		pointer fields
			left: left child of self @type: AVLNode @default: None
			right: right child of self @type: AVLNode @default: None
			parent: self is a child of self @type:AVLNode @default: None
		
		help fields
			height: length of the longest path from self to a leaf @type: int 
			rank: the number of nodes in the tree which self is its root @type: int
		"""
	
	def __init__(self, value):
		"""Constructor, you are allowed to add more fields. 

		@type value: str
		@param value: data of your node
		"""
		self.value = value
		# pointers
		self.left = None
		self.right = None
		self.parent = None
		# help fields
		self.height = -1 
		self.rank = -1

	def getLeft(self):
		"""returns the left child

		@rtype: AVLNode
		@returns: the left child of self, None if there is no left child
		"""
		return self.left
		

	def getRight(self):
		"""returns the right child

		@rtype: AVLNode
		@returns: the right child of self, None if there is no right child
		"""
		return self.right
		

	def getParent(self):
		"""returns the parent 

		@rtype: AVLNode
		@returns: the parent of self, None if there is no parent
		"""
		return self.parent

	def getValue(self):
		"""return the value

		@rtype: str
		@returns: the value of self, None if the node is virtual
		"""
		return self.value

	def getHeight(self):
		"""returns the height (assumes correct field)

		@rtype: int
		@returns: the height of self, -1 if the node is virtual
		"""
		return self.height

	def getBalanceFactor(self):
		"""returns the balance_factor (assumes correct field)

		@rtype: int
		@returns: the balace factor of self, 0 if the node is virtual
		"""
		right_height = self.getRight().getHeigth()
		left_height = self.getLeft().getHeigth()
		return left_height - right_height
	
	def setLeft(self, node):
		"""sets left child without rebalance

		@pre: node.value <= self.value
		@post: updates help fields
		@post: delete old right node
		@type node: AVLNode
		@param node: a node
		"""
		#TODO make sure this is right
		self.left = node
		self.updateHeight()
		

	def setRight(self, node):
		"""sets right child without rebalance

		@pre: node.value > self.value
		@post: updates help fields
		@post: delete old right node
		@type node: AVLNode
		@param node: a node
		"""
		#TODO make sure this is right
		self.right = node
		self.updateHeight()

	def setParent(self, node):
		"""sets parent and update the parent node.
		if there were some child where self needs to go, it is deleted

		@post: updated help fields
		@type node: AVLNode
		@param node: a node
		"""
		#TODO
		return None

	def setValue(self, value):
		"""sets value

		@type value: str
		@param value: data
		"""
		#TODO
		return None

	def setHeight(self, h):
		"""sets the height of the node

		@type h: int
		@param h: the height
		"""
		self.height = h

	def updateHeight(self):
		"""sets the height based on the height of the left and the right children
		
		@pre: childrens heights are updated
		"""
		left_height = self.getLeft().getHeight()
		right_height = self.getRight().getHeight()

		self.setHeight(max(left_height, right_height) + 1)

	def deepHeights(self):
		"""searches into the tree recursivly, 
		updates the height at each node.

		@rtype: int 
		@return: height of the node
		"""
		# handle virtual nodes		
		if (not self.isRealNode):
			return -1
		
		# recursivly find height of left and right nodes
		left_node = self.getLeft()
		left_height = 0
		if (left_node != None):
			left_height = left_node.setHeight()
		
		right_node = self.getRight()
		right_height = 0
		if (right_node != None):
			right_height = right_node.setHeight()
		
		# set the field
		self.height = max(right_height, left_height) + 1
		return self.getHeight()


	def deepBalanceFactor(self):
		"""serches into the tree recursively,
		updated the height at each node, 
		and then returns the balance factor
		
		@rtype: int
		@return: balance factor of the tree
		"""
		self.deepHeights()
		return self.getBalanceFactor()


	def isRealNode(self):
		"""returns whether self is not a virtual node 

		@rtype: bool
		@returns: False if self is a virtual node, True otherwise.
		"""
		return self.value != None


	def rebalance(self, is_insert = False):
		"""rebalance the tree after insertion or deletion of self

		@type is_insert: bool
		@param is_insert: if rebalance is after insertion
		"""
		parent = self.getParent()
		old_height = parent.getHeight()
		while parent != None:
			balance_factor = parent.getBalanceFactor()
			new_height = parent.getHeight()
			
			if old_height == new_height:
				return
			
			else:
				if (balance_factor == 2):
					# self.left cannot be None 
					left_node = self.getLeft()
					if left_node.getBalanceFactor() == -1:
						left_node.rotateLeft()
					self.rotateRight()
					if is_insert:
						return
				
				elif (balance_factor == -2):
					# self.right cannot be None 
					right_node = self.getRight()
					if right_node.getBalanceFactor() == 1:
						right_node.rotateRight()
					self.rotateLeft()
					if is_insert:
						return
				
				else: # balance_factor < 2
					parent = parent.getParent()
			


	def rotateLeft(self):
		"""makes self the left child of self.right
		
		@pre: height and balance factor were correct
		"""
		#TODO update help fields
		# prepare pointers
		parent = self.getParent()
		child = self.getRight()
		childs_left = child.getLeft()

		# rotate
		self.setRight(childs_left)
		child.setLeft(self)
		child.setParent(parent)	
		
		# update height fields
		AVLNode.updateConnectedNodes(parent, child, self)

	
	"""makes self the right child of self.left"""
	def rotateRight(self):
		#TODO update help fields
		# prepare pointers
		parent = self.getParent()
		child = self.getLeft()
		childs_right = child.getRight()

		# rotate
		self.setLeft(childs_right)
		child.setRight(self)
		child.setParent(parent)

		# update height fields
		AVLNode.updateConnectedNodes(parent, child, self)


	@staticmethod
	def updateConnectedNodes(node, child, grandchild):
		"""Updated the height field for three connected nodes
			parent
 			  L> child 
				  L> grandchild

		@pre: all other nodes have correct height field
		@post: height fields will be correct for given nodes
		@type node, child, grandchild: AVLNode
		@param node, child, grandchild: nodes in order of parantage
		"""
		# update bottom up
		grandchild.updateHeight()
		child.updateHeight()
		node.updateHeight()
	


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return None


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return None

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None


