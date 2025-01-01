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
		#delete!!!
		self.size = 5
		

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
	@return the node's balance factor (right - left)
	@rtype: int
	"""
	def get_balance_factor(self):
		if not self.is_real_node():
			return 0
		return self.right.height - self.left.height

	"""
	check if the height diff with children is 0 or 1 
	@return True if node is valid AVL node, False otherwise
	"""
	def is_valid_AVL_node(self):
		return self.get_balance_factor() in (0, 1, -1) and self.height == max(self.left.height, self.right.height) + 1



"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None
		self.size = 0
		# A virtual node used for null children
		self.virtual_leaf = AVLNode(None, None)
		self.virtual_leaf.height = -1

	"""
	set new root
	@type root: AVLNode
	"""
	def set_root(self, root):
		self.root = root
		self.root.parent = None

	"""
	@type parent_node: AVLNode
	@type child_node: AVLNode 
	@param parent_node: parent of child node
	@param child_node: child node of parent node
	@param direction: 'r' for right rotate, 'l' for left rotate
	@rtype: (AVLNode, AVLNode)
	@returns: new child node (parent_node), new parent node (child_node)
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
		# set heights
		parent_node.set_height()
		child_node.set_height()
		# return new child, new parent
		return parent_node, child_node

	"""searches for a node in the dictionary corresponding to the key (starting at the node we are getting and going down)

	@type key: int
	@param starting_node: a node which we start the search from in direction up->down
	@param ending_key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e,p) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1, and p is the parent node
	"""

	def search_from_key_to_key(self, starting_node, ending_key):
		number_of_edges = 0
		node_to_return = None
		parent_node = None

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

	"""searches for a node in the dictionary corresponding to the key, starting at the max

		@type key: int
		@param key: a key to be searched
		@rtype: (AVLNode,int, AVLNode)
		@returns: a tuple (x,e, parent) where x is the node corresponding to key (or None if not found),
		and e is the number of edges on the path between the starting node and ending node+1
		parent is the parent of the node (or who would be the parent if the key is not in the tree).
		"""
	def _finger_search_with_parent(self, key):
		number_of_edges = 0
		node_to_return = None
		node = self.max_node()
		# if node is root of empty tree
		if node == None:
			return node_to_return, number_of_edges, node
		# if given key is larger than the maximum key - return None
		if node.key != None and node.key < key:
			return node_to_return, 1, node
		# runs over the tree keys and find the first node that smaller than the given key
		while node.parent != None and node.parent.key != None:
			# if the given key is bigger or equal to the key we are in - go to the node parent
			if node.key <= key:
				break
			node = node.parent
			# add one to the edges counter
			number_of_edges += 1

		if node.key == key:
			tup = node, 1, node.parent
		else:
			tup = self.search_from_key_to_key(node, key)

		return tup[0], number_of_edges + tup[1], tup[2]

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key):
		tup = self._finger_search_with_parent(key)
		return tup[0], tup[1]


	"""
	rebalance tree after insertion or join
	@type start_node: AVLNode
	@param start_node: starting node to balance
	@type promote_count: int
	@param end_node: counts promotions
	@type action: String
	@param action: "i" if rebalance after insert, "j" if rebalance after join
	@rtype: int
	@returns: promote_count - number of promotions
	"""
	def rebalance_tree(self, start_node, promote_count, action):
		start_node.set_height()

		if start_node.is_valid_AVL_node():
			# case 1 - problem is fixed or moved up
			if start_node.parent is None:
				return promote_count + 1
			return self.rebalance_tree(start_node.parent, promote_count + 1, action)

		balance_factor = start_node.get_balance_factor()
		if balance_factor == 2:
			if start_node.right.get_balance_factor() in {0, 1}:
				# case 2 - single rotation left
				self.rotate(start_node, start_node.right, 'l')
			else:
				# case 3 - double rotation right and left
				new_child, new_parent = self.rotate(start_node.right, start_node.right.left, 'r')
				self.rotate(new_parent.parent, new_parent, 'l')

		elif balance_factor == -2:
			if start_node.left.get_balance_factor() in {0, -1}:
				# case 2 - single rotation right
				self.rotate(start_node, start_node.left, 'r')

			else:
				# case 3 - double rotation left and right
				new_child, new_parent = self.rotate(start_node.left, start_node.left.right, 'l')
				self.rotate(new_parent.parent, new_parent, 'r')
		if action == "i":
			return promote_count
		if action == "j":
			return self.rebalance_tree(start_node.parent, promote_count + 1, action)

	"""
	get a key and a value to insert to the dictionary and create a new valid leaf with virtual leafs
	
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: AVLNode
	@returns: the new node
	
	"""
	def _build_new_node(self, key, val):
		new_node = AVLNode(key, val)
		# set virtual children
		new_node.left = self.virtual_leaf
		new_node.right = self.virtual_leaf
		return new_node

	"""inserts a new node into the dictionary as parent's child

		@type new_node: AVLNode
		@pre: new_node.key currently does not appear in the dictionary, new_node is a valid leaf, if new_node was in the dictionary it was parent's child
		@param new_node: new node that is to be inserted to self
		@type parent: AVLNode
		@param val: the parent of new_node
		@rtype: (AVLNode,int)
		@returns: a 2-tuple (x,h) where x is the new node,
		and h is the number of PROMOTE cases during the AVL rebalancing
		"""
	def _insert_node_to_parent(self, new_node, parent):
		promote_count = 0
		# if parent is root
		if parent is None:
			self.root = new_node
			new_node.set_height()
		else:
			is_parent_leaf = not parent.left.is_real_node() and not parent.right.is_real_node()
			new_node.parent = parent
			if parent.key > new_node.key:
				parent.left = new_node
			else:
				parent.right = new_node
			# the parent is not a leaf
			if not is_parent_leaf:
				new_node.set_height()
				new_node.parent.set_height()
			# the parent is a leaf
			else:
				promote_count = self.rebalance_tree(new_node, -1, "i")
		return new_node, promote_count


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
		new_node = self._build_new_node(key, val)

		# find where to insert - get father and e
		tup = self.search_from_key_to_key(self.root, key)
		parent = tup[2]
		e = tup[1]

		#insert new node to place
		new_node, promote_count = self._insert_node_to_parent(new_node, parent)
		return new_node, e, promote_count



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
		# create new node
		new_node = self._build_new_node(key, val)

		# find where to insert - get father and e
		tup = self._finger_search_with_parent(key)
		parent = tup[2]
		e = tup[1]

		# insert new node to place
		new_node, promote_count = self._insert_node_to_parent(new_node, parent)
		return new_node, e, promote_count


	"""
    connect root of shorter tree and node of taller tree as children of connector_node
    and connect connector_node to the taller tree.
    @type node: AVLNode
    @param node: the node that is to be connected
    @type root: AVLNode
    @param root: the root of the shorter tree
    @type connector_node: AVLNode
    @param connector_node: an AVLNode that should become parent of node and root and child of node.parent
    @type direction: String
    @param direction: the direction of the shorter tree 
    @pre: direction == 'l' if root is smaller in keys, and 'r' if root is larger in keys.
    The height difference between the node and the root is at most 1.
    """

	def connect_trees(self, node, root, connector_node, direction_of_root):
		if direction_of_root == 'l':
			# connect root to the left
			node.parent.left = connector_node
			connector_node.parent = node.parent
			connector_node.right = node
			connector_node.left = root
		else:
			# connect root to the right
			node.parent.right = connector_node
			connector_node.parent = node.parent
			connector_node.right = root
			connector_node.left = node
		node.parent = connector_node
		root.parent = connector_node

	"""joins self with item and another AVLTree

        @type tree2: AVLTree 
        @param tree2: a dictionary to be joined with self
        @type connector_node: AVLNode
        @param connector_node: an AVLNode that should become the new root. 
        @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
        or the opposite way. connector_node.key is between the trees values. self and tree2 has the same height. 
        """

	def join_same_height(self, tree2, connector_node):
		if connector_node.key > tree2.root.key:
			connector_node.left = tree2.root
			connector_node.right = self.root
		else:
			connector_node.left = self.root
			connector_node.right = tree2.root
		connector_node.right.parent = connector_node
		connector_node.left.parent = connector_node
		self.set_root(connector_node)
		self.root.set_height()

	"""
    walks on the tree in the given direction until finding node that it's height equals height or 1 shorter
    @return the node that was found
    """

	def find_node_at_height(self, height, direction):
		node = self.root
		if direction == 'l':
			while node.height > height and node.left.is_real_node():
				node = node.left
			return node
		while node.height > height and node.right.is_real_node():
			node = node.right
		return node

	"""deletes node from the parent

			@type node: AVLNode
			@pre: node is a real pointer to a node in self
			"""
	def delete_node(self, node):
		parent = node.parent
		if parent.key > node.key:
			# if a leaf only delete, else pass it child
			if node.height == 0:
				parent.left = self.virtual_leaf
			else:
				if node.right.key != None:
					parent.left = node.right
					node.right.parent = parent
				else:
					parent.left = node.left
					node.left.parent = parent
		else:
			# if a leaf only delete, else pass it child
			if node.height == 0:
				parent.right = self.virtual_leaf
			else:
				if node.right.key != None:
					parent.right = node.right
					node.right.parent = parent
				else:
					parent.right = node.left
					node.left.parent = parent

		self.size = self.size - 1

	"""demote nodes height and it parent up to the root

		@type node: AVLNode
		@pre: node is a real pointer to a node in self
		"""
	def demote_node(self, node):
		parent_loop = node
		while parent_loop != None:
			right_diff = parent_loop.height - parent_loop.right.height
			left_diff = parent_loop.height - parent_loop.left.height
			if right_diff == 2 and left_diff == 2:
				parent_loop.height = parent_loop.height - 1
			else:
				break

			parent_loop = parent_loop.parent

	"""balancing the tree after deleting node

			@type node: AVLNode
			@type brother: AVLNode - the other child of the parent of the deleted node
			@pre: node and brother is a real pointer to a node in self
			"""
	def balance_the_tree(self, node, brother):
		# add the symmetrical case
		dire = "l"
		node_to_rotate = brother
		if brother.key < node.parent.key:
			dire = "r"

		parent = node.parent
		# if the two children of the node brother node is even
		if brother.left.height == brother.right.height:
			self.rotate(parent, node_to_rotate, dire)
		# brother's right child is higher, and brother is lower than node (or the opposite)
		elif (brother.left.height < brother.right.height and dire == "r") or (
				brother.right.height < brother.left.height and dire == "l"):
			# first rotation according to height
			if brother.left.height > brother.right.height:
				new_node_to_rotate = brother.left
				self.rotate(brother, new_node_to_rotate, "r")
				# second rotate
				self.rotate(parent, new_node_to_rotate, dire)
			else:
				new_node_to_rotate = brother.right
				self.rotate(brother, new_node_to_rotate, "l")
				# second rotate
				self.rotate(parent, new_node_to_rotate, dire)

			# fix tree heights - go up and decrease the parents height if needed
			parent.height = parent.height - 1
			self.demote_node(parent.parent)
		# if the left child of the node brother node is higher, and the node brother is higher than the deleted node or the opposite
		elif (brother.left.height < brother.right.height and dire == "l") or (
				brother.right.height < brother.left.height and dire == "r"):
			self.rotate(parent, node_to_rotate, dire)
			# fix tree heights - go up and decrease the parents height if needed
			parent.height = parent.height - 1
			self.demote_node(parent.parent)

	"""finds the successor of a given node

			@type node: AVLNode
			@pre: node is a real pointer to a node in self
			"""
	def get_successor(self, node):
		# if the node hase right child return the min of its tree
		if node.right.key != None:
			node = node.right
			while node.left.key != None:
				node = node.left
			return node
		# go up in the tree until the node is the right child
		parent = node.parent
		while parent.key != None and node == parent.right:
			node = parent
			parent = parent.parent
		return parent

	"""finds the predecessor of a given node

				@type node: AVLNode
				@pre: node is a real pointer to a node in self
				"""
	def get_predecessor(self, node):
		# if the node hase right child return the min of its tree
		if node.left.key != None:
			node = node.left
			while node.right.key != None:
				node = node.right
			return node
		# go up in the tree until the node is the right child
		parent = node.parent
		while parent.key != None and node == parent.left:
			node = parent
			parent = parent.parent
		return parent


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node):
		use_decessor = False
		node_to_replace = None
		node_to_delete = node
		# if the node exists
		if node.left.key != None and node.right.key != None:
			use_decessor = True
			node_to_delete = node
			# replace the node with its successor or predecessor to make sure we are deleting node with one child
			max_node = self.max_node()
			if max_node.key == node.key:
				node = self.get_predecessor(node)
			else:
				node = self.get_successor(node)
			node_to_replace = node

		#### what will we do in a case this is tha maximal node when there is no successor????

		# check which side is the node
		parent = node.parent
		brother = node.parent.left
		node_dir = "r"
		if node.key < node.parent.key:
			brother = node.parent.right
			node_dir = "l"

		# if the other child of my parent is lower than the given node - demote and rotate
		if brother.key == None or brother.height == node.height - 1:
			self.delete_node(node)
			# fix tree heights - go up and decrease the parents height if needed
			parent.height = parent.height - 1
			self.demote_node(parent.parent)

		# if the other child of my parent is with the same height as the given node - only delete
		elif brother.height == node.height:
			self.delete_node(node)

		# if the other child of my parent is higher than the given node - delete and rotate
		elif brother.height == node.height + 1:
			# balance the tree
			self.balance_the_tree(node, brother)

			self.delete_node(node)


		# replace the node with its succussore if needed
		if use_decessor:
			node_to_replace.left = node_to_delete.left
			if node_to_delete.left.key != None:
				node_to_delete.left.parent = node_to_replace

			node_to_replace.right = node_to_delete.right
			if node_to_delete.right.key != None:
				node_to_delete.right.parent = node_to_replace

			node_to_replace.height = node_to_delete.height
			node_to_replace.value = node_to_delete.value
			node_to_replace.parent = node_to_delete.parent
			if node_to_delete.parent != None and node_to_delete.parent.key != None:
				if node_to_delete.parent.key < node_to_replace.key:
					node_to_delete.parent.right = node_to_replace
				else:
					node_to_delete.parent.left = node_to_replace

			if node_to_delete == self.root:
				self.root = node_to_replace

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
		# creat connector node
		connector_node = AVLNode(key, val)

		# if the trees equally tall, join them
		if tree2.root.height == self.root.height:
			return self.join_same_height(tree2, connector_node)

		# else find the taller tree and set as self
		if tree2.root.height > self.root.height:
			temp_root = self.root
			self.root = tree2.root
			tree2.root = temp_root

		# find direction to connect
		if key < self.root.key:
			direction = 'l'
		else:
			direction = 'r'

		# find node at self that it's height is equal to tree2.root or shorter by 1
		node = self.find_node_at_height(tree2.root.height, direction)

		# connect node and tree2.root as children of connector_node
		self.connect_trees(node, tree2.root, connector_node, direction)

		# rebalance tree
		connector_node.set_height()
		self.rebalance_tree(connector_node.parent, 0, "j")



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
		left_tree_to_return = None
		right_tree_to_return = None
		original_node_key = node.key
		# if the node exists
		while node != None:
			# if the original node is smaller than this node
			if node.key >= original_node_key:
				# just add to the right tree and continue
				if node.right.key != None:
					sub_tree = AVLTree()
					sub_tree.set_root(node.right)
					# if the arr to return is empty
					if right_tree_to_return == None:
						right_tree_to_return = sub_tree
						# if the node need to be added to the new tree
						if node.key != original_node_key:
							right_tree_to_return.insert(node.key, node.value)
					else:
						right_tree_to_return.join(sub_tree, node.key, node.value)

			# if the original node is bigger than this node
			if node.key <= original_node_key:
				if node.left.key != None:
					sub_tree = AVLTree()
					sub_tree.set_root(node.left)
					# if the arr to return is empty
					if left_tree_to_return == None:
						left_tree_to_return = sub_tree
						# if the node need to be added to the new tree
						if node.key != original_node_key:
							left_tree_to_return.insert(node.key, node.value)
					else:
						sub_tree = AVLTree()
						sub_tree.set_root = node.left
						left_tree_to_return.join(sub_tree, node.key, node.value)

			node = node.parent

		return left_tree_to_return, right_tree_to_return

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array_rec(self, arr_to_return, node):
		if node.key == None:
			return

		self.avl_to_array_rec(arr_to_return, node.left)
		tup = node.key, node.value
		arr_to_return.append(tup)
		self.avl_to_array_rec(arr_to_return, node.right)

	"""returns an array representing dictionary 

		@rtype: list
		@returns: a sorted list according to key of touples (key, value) representing the data structure
		"""
	def avl_to_array(self):
		arr_to_return = []
		node = self.root
		if node.key != None:
			self.avl_to_array_rec(arr_to_return, node.left)
			tup = node.key, node.value
			arr_to_return.append(tup)
			self.avl_to_array_rec(arr_to_return, node.right)
		return arr_to_return


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		maximum_node = None
		root = self.root
		# runs over the tree keys
		while root != None and root.key != None:
			if root.right.key == None:
				maximum_node = root
				break
			root = root.right

		return maximum_node

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.size


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		if self.root.is_real_node():
			return self.root
		return None
