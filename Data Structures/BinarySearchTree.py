class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None #parent node current_node

class Tree:
    def __init__(self):
        self.root = None #Tree is empty to begin with
    
    def insert(self, value):
        if self.root == None: #if no root, set root equal to new Node with passed in value
            self.root = Node(value)
        else:
            self._insert(value, self.root) #call private _insert() function, looking at the root, with passed in value

    def _insert(self, value, cur_node):
        if value < cur_node.value: #check if value is < current_node.value
            if cur_node.left_child == None: #if current_node has no left_child, set new left_child
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node #set parent_node
            else: #otherwise call _insert() again with current_node.left_child as current_node
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value: #check if value >= current_node.value
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node #set parent_node
            else:
                self._insert(value, cur_node.right_child)
        else: #check if value is == to current_node.value
            print('Value already in tree!')

    def print_tree(self):
        if self.root != None: #check if root exists
            self._print_tree(self.root) #otherwise call _print_tree() with root as parameter

    def _print_tree(self, cur_node):
        #this is an inorder printing of the tree. tree should already be sorted
        if cur_node != None: #check that cur_node exists, then recursively call with cur_node.left_child and cur_node.right_child
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None: #check root isnt empty 
            return self._height(self.root, 0) 
        else: #if root == None, tree has height of 0, so we return 0
            return 0
    
    def _height(self, cur_node, cur_height):
        if cur_node == None: #if cur_node == None, return cur_height of 0
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height) #compare left_height and right_height, and return whichever height is larger

    # returns True/False if value exists in tree
    def search(self, value):
        if self.root != None: #check that root exists
            return self._search(value, self.root)
        else: #if no root, return False
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value: #check if value == cur_node.value, if yes return True
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child) #if value < current_node.value and current_node.left_child exists, return recursive call with left child
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child) #if value > current_node.value and current_node.right_child exists, return recursive call with right child
        return False #otherwise return False, meaning value was never found

    #returns the actualy node with specified input value
    def find(self, value):
        if self.root != None: # if root exists, use _find() to recursively find value
            return self._find(value, self.root)
        else:  #if root doesnt exist, return None
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child) #if value < current_node.value and current_node.left_child exists, return recursive call with left child
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child) #if value > current_node.value and current_node.right_child exists, return recursive call with right child
        return False #otherwise return False, meaning value was never found

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        #returns the node with min value in tree rooted at input node
        def min_value(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current
        
        #returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children
        
        #get the parent of the node to be deleted
        node_parent = node.parent
        #get the number of children of the node to be deleted
        node_children = num_children(node)

        #break operation into 3 different cases based on the structure of the tree and the node to be deleted

        #CASE 1: node has no children
        if node_children == 0:
            #remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        #CASE 2: node has a single child
        if node_children == 1:
            #get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            #replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            
            #correct the parent pointer in node
            child.parent = node_parent
        
        #CASE 3: node has two children
        if node_children == 2:
            #get the inorder successor of the deleted node
            successor = min_value(node.right_child)
            #copy the inorder successor's value to the node formerly holding the value we wisehd to delete
            node.value = successor.value
            #delete the inorder sucessor now that it's value was copied into the other node
            self.delete_node(successor)
            


def fill_tree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = Tree()
#tree = fill_tree(tree)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)

tree.print_tree()

print('Tree Height is: ' + str(tree.height()))

tree.delete_value(5)
tree.print_tree()
print('Tree Height is: ' + str(tree.height()))


tree.delete_value(4)
tree.print_tree()
print('Tree Height is: ' + str(tree.height()))