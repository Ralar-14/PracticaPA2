class Queue:
    # ----------------------------------------------------
    # Cada element de la cua serà una instància de _Node
    class _Node:
        __slots__ = '_element', '_next' 
        def __init__(self, element, next):
            self._element = element 
            self._next = next              
    # ------------------------------------------

    def __init__(self):
        self.__cap = None
        self.__cua = None
        self.__mida = 0

    def buida(self):
        return self.__mida == 0
 
    def mida(self):
        return self.__mida

    def first(self):
        # Pre: La cua no és buida
        return (self.__cap)._element

    def enqueue(self, e):
        # nou node al final de la cua
        nou = self._Node(e, None)   
        if self.buida():
            # cas especial, cua buida
            self.__cap = nou       
        else:
            self.__cua._next = nou
        # actualitzar referència al darrer node
        self.__cua = nou            
        self.__mida += 1

    def dequeue(self):
        # Pre: La cua no és buida
        resposta = self.__cap._element
        self.__cap = self.__cap._next
        self.__mida -= 1
        if self.buida():               
            # cas especial, cua buida
            # el __cap eliminat també
            # era la cua
            self.__cua = None          
        return resposta

