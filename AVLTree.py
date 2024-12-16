#id1:
#name1:
#username1:
#id2:
#name2:
#username2:


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

	def is_real_node(self):
		return self.key is not None

	"""set node height from his children
	
	"""
	def set_height(self):
		self.height = 1 + max(self.left.height, self.right.height)


"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None

	"""
	set new root
	@type root: AVLNode
	"""
	def set_root(self, root):
		self.root = root

	"""
	@type parent_node: AVLNode
	@type child_node: AVLNode 
	@param parent_node: parent of child node
	@param child_node: child node of parent node
	@param direction: 'r' for right rotate, 'l' for left rotate
	@rtype: AVLTree
	@returns: self after rotation
	"""
	def rotate(self, parent_node, child_node, direction):
		if direction == "r": # rotate right
			# move subtree from child to parent
			sub_tree = child_node.right
			parent_node.left = sub_tree
			# set parent as child's child
			child_node.right = parent_node
		else: # rotate left
			# move subtree from child to parent
			sub_tree = child_node.left
			parent_node.right = sub_tree
			# set parent as child's child
			child_node.left = parent_node

		if sub_tree.is_real_node():
			sub_tree.parent = parent_node

		# if parent_node is root
		if parent_node.parent is None:
			self.set_root(child_node)
		# if parent_node have parent set child_node as his child
		else:
			child_node.parent = parent_node.parent
			if parent_node.parent.left == parent_node:
				parent_node.parent.left = child_node
			else:
				parent_node.parent.right = child_node

		parent_node.parent = child_node
		return self

	"""searches for a node in the dictionary corresponding to the key (starting at the node we are getting and going down)

	@type key: int
	@param starting_node: a node which we start the search from in direction up->down
	@param ending_key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e.p) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1, and p is the parent node
	"""

	def search_from_key_to_key(self, starting_node, ending_key):
		number_of_edges = 0
		node_to_return = None

		root = starting_node
		# runs over the tree keys
		while root != None and root.key != None:
			# add one to the edges counter
			number_of_edges += 1
			# if the key was found end the loop
			if root.key == ending_key:
				node_to_return = root
				break
			# if the given key is bigger that the key we are in - go to the right child
			elif root.key < ending_key:
				parent_node = root
				root = root.right
			# if the given key is smaller that the key we are in - go to the left child
			else:
				parent_node = root
				root = root.left

		return node_to_return, number_of_edges, parent_node


	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search(self, key):

		tup = self.search_from_key_to_key(self.root, key)

		return tup[0], tup[1]


	"""searches for a the node with the maximum key (starting at the root)

		@returns: the maximum node.
		"""
	def get_max(self):
		maximum_node = None
		root = self.root
		# runs over the tree keys
		while root.key != None:
			if root.right.key == None:
				maximum_node = root
				break
			root = root.right

		return maximum_node

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key):
		number_of_edges = 0
		node_to_return = None
		node = self.get_max()

		# if given key is larger than the maximum key - return None
		if node.key != None and node.key < key:
			return node_to_return, number_of_edges
		# runs over the tree keys and find the first node that smaller than the given key
		while node.parent != None and node.parent.key != None:
			# if the given key is bigger or equal to the key we are in - go to the node parent
			if node.key <= key:
				break
			node = node.parent
			# add one to the edges counter
			number_of_edges += 1

		if node.key == key:
			tup = node, 1
		else:
			tup = self.search_from_key_to_key(node, key)

		return tup[0], number_of_edges + tup[1]


	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def insert(self, key, val):
		# create new node
		new_node = AVLNode(key, val)
		# find where to insert - get father
		parent = None

		# the parent is not a leaf
		if parent.left.is_real_node() or parent.right.is_real_node():
			if parent.key > key:
				parent.left = new_node
			else:
				parent.right = new_node
		#the parent is a leaf
		#else:


		# set all new_node and parent fields

		return None, -1, -1


	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def finger_insert(self, key, val):
		return None, -1, -1


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node):
		return	

	
	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2, key, val):
		return


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None, None

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		return None

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1	


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return None
