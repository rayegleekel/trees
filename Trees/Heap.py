'''
'''

from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)    

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        left_condition = True
        right_condition = True

        if node is None:
            return True
        if node.left:
            left_condition = node.left.value >= node.value and Heap._is_heap_satisfied(node.left)
        if node.right:
            right_condition = node.right.value >= node.value and Heap._is_heap_satisfied(node.right)

        if left_condition == True and right_condition == True:
            return True
        else:
            return False

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        node.descendents += 1
        binary = "{0:b}".format(node.descendents)

        if binary[1] == '0':
            if node.left is None:
                node.left = Node(value)
                node.left.descendents = 1
            else:
                Heap._insert(value, node.left)
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        elif binary[1] == '1':
            if node.right is None:
                node.right = Node(value)
                node.right.descendents = 1
            else:
                Heap._insert(value, node.right)
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for elem in xs:
            self.insert(elem)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if Heap.is_heap_satisfied(self):
            return self.root.value
    
    def remove_min(self):
        if self.root is None:
            pass
        elif self.root and self.root.left is None:
            self.root = None
        elif self.root.left is not None:
            temp = Heap.find_last(self.root)
            self.root.value = temp
            if Heap.is_heap_satisfied(self) == False:
                Heap.swap(self.root)


    @staticmethod 
    def find_last(node):
        binary = "{0:b}".format(node.descendents)
        node.descendents -= 1
        if len(binary) == 2:
            if binary[1] == '1':
                temp = node.right
                node.right = None
            elif binary[1] == '0':
                temp = node.left
                node.left = None
            return temp.value
        else:
            if binary[1] == '0':
                return Heap.find_last(node.left)
            elif binary[1] == '1':
                return Heap.find_last(node.right)



    @staticmethod
    def swap(node):
        if node.left and node.right is None:
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
                Heap.swap(node.left)
        elif node.right and node.left is None:
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value
                Heap.swap(node.right)
        elif node.left and node.right:
            if node.value > node.left.value and node.left.value <= node.right.value:
                node.value, node.left.value = node.left.value, node.value
                Heap.swap(node.left)
            elif node.value > node.right.value and node.left.value >= node.right.value:
                node.value, node.right.value = node.right.value, node.value
                Heap.swap(node.right)
