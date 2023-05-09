from class_cua import Cua

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
    def preorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the pre-order traversal.
        """
        def _preorder(t):
            if t is None:
                return []
            else:
                return [t._element] + _preorder(t._left) + _preorder(t._right)

        if self.empty():
            return []
        else:
            return _preorder(self._root)        

    def postorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the post-order traversal.
        """
        def _postorder(t):
            if t is None:
                return []
            else:
                return _postorder(t._left) + _postorder(t._right) + [t._element] 

        if self.empty():
            return []
        else:
            return _postorder(self._root)
        
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

    def levelorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the levels-order traversal.
        """
        if self.empty():
            return []
        else:
            resultat = []
            q = Cua()
            q.enqueue(self._root)
            while not q.buida():
                tt = q.dequeue()
                resultat.append(tt._element)
                if tt._left is not None:
                    q.enqueue(tt._left)
                if tt._right is not None:
                    q.enqueue(tt._right)
            return resultat

    def poda_subarbre(self,x):
        """
        Pre: self té tots els elements diferents
        Si x es el valor d'algun node de self, la funció retorna True i elimina de self 
        el node amb valor x i tots els seus descendents; altrament, el resultat es False 
        i self no varia (és a dir, es queda igual).
        """
        def poda_auxiliar(node,x):
            # Pre: node is not None and node._element != x
            trobat = False
            if node._left is not None: 
                if node._left._element == x:
                    trobat = True
                    node._left = None
                else:
                    trobat = poda_auxiliar(node._left,x)
            if not trobat and node._right is not None: 
                if node._right._element == x:
                    trobat = True
                    node._right = None
                else:
                    trobat = poda_auxiliar(node._right,x)
            return trobat
        
        if self._root is None:
            return False
        else:
            if self._root._element == x:
                self._root = None
                return True
            else: 
                return poda_auxiliar(self._root,x)

    def __repr__(self):
        if self.empty():
            return 'BinTree()'
        elif self.leaf():
            rt = self.get_root().__repr__()
            return f"BinTree({rt})"
        else:  #  Algun dels fills no és buit
            rt = self.get_root().__repr__()
            if self.get_right().empty():  # El fill dret és buit?
                r_esq = self.get_left().__repr__()
                return f"BinTree({rt}, left={r_esq})"
            elif self.get_left().empty(): # El fill esquerre és buit?
                r_dre = self.get_right().__repr__()
                return f"BinTree({rt}, right={r_dre})"
            else:                         # Cap fill és buit
                r_esq = self.get_left().__repr__()
                r_dre = self.get_right().__repr__()
                return f"BinTree({rt}, left={r_esq}, right={r_dre})"

    def __eq__(self, b):
        def eq_aux(n1, n2):
            if n1 is None:
                return n2 is None
            elif n2 is None:
                return False
            else:
                if n1._element != n2._element:
                    return False
                else:
                    return eq_aux(n1._left, n2._left) and eq_aux(n1._right, n2._right)
            return eq_aux(self._root, b._root)