class BinTree:

    #------------------- nested _Node class --------------------------
    class _Node:
        __slots__ = '_element', '_left', '_right'   # streamline memory usage

        def __init__(self, element, left = None, right = None):
            self._element = element
            self._left    = left
            self._right   = right

        
    #--------------- BinTree public methods ------------------------

    # Beware the distinction between an empty BinTree, and an empty _Node (that is None)
    
    def __init__(self,v=None,left=None,right=None):
        """
        Warning, an empty tree is NOT None
        An empty tree is a BinTree with self._root equal to None
        The object created by a call to BinTree() is an empty tree
        Requirement: If the value v is None, so must be the two children.
        """
        assert (v is None and left is None and right is None) or v is not None
        if v is None:
            self._root = None   # Empty tree
        else:
            l = left._root  if (left  is not None) else None    # <== ATENCIÓ!!!
            r = right._root if (right is not None) else None    # <== ATENCIÓ!!!
            self._root = self._Node(v, l, r)
            
    # Getters
    def get_root(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the value at the root of the BinTree
        """
        return self._root._element
    
    def get_left(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the left child of the BinTree
        """
        lft = BinTree()
        lft._root = self._root._left
        return lft
    
    def get_right(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the right child of the BinTree
        """
        rft = BinTree()
        rft._root   = self._root._right
        return rft

    # Setters
    def set_root(self,v):
        """
        changes the value at the root of the BinTree
        """
        assert(v is not None)
        if not self.empty():
            self._root._element = v
        else:
            self._root = self._Node(v)
        
    def set_left(self,left):
        """
        Pre: left is a BinTree and the BinTree is not empty
        changes the left child of the BinTree
        """
        self._root._left = left._root
        
    def set_right(self,right):
        """
        Pre: right is a BinTree and the BinTree is not empty
        changes the right child of the BinTree
        """
        self._root._right = right._root
        
    # Other operations
    def empty(self):
        """
        returns True if the BinTree is empty, False in other case
        """
        return self._root == None
        
    def leaf(self):
        """
        returns True if the BinTree is a leaf, False if not. The BinTree is not empty
        """
        return self._root._left is None and self._root._right is None
   
    # Traversals 
    def inorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the in-order traversal.
        """
        def _inorder(t):
            if t is None:
                return []
            else:
                return _inorder(t._left) + [t._element] + _inorder(t._right)

        if self.empty():
            return []
        else:
            return _inorder(self._root)

    
