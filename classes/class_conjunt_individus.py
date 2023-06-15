#Importem la funció item per poder llegir el fitxer input. També la classe individu i la classe BinTree.

from pytokr import item
from class_individu import individu
from class_bintree import BinTree

class conjunt_individus:
    def __init__(self):
        """
        Inicialitza el conjunt d'individus, crea el arbre genealogic i 
        tots els individus.
        """
        self.numero_individus = int(item())
        self.numero_cromosomes = int(item())
        self.__individus = [None]
        self.__arbre = self.__llegir_arbre()
        for _ in range(self.numero_individus):
            self.afegir_individu(item())
        print(f"experiment {self.numero_individus} {self.numero_cromosomes}")
    
    def inordre_distribucio(self, tret):
        inordre = self.__arbre_distribucio_tret(self.__arbre, tret)
        if inordre == None:
            return []
        else:
            return inordre.inorder()
    
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))

    def afegir_tret(self, tret, numero_individu):
        self.__individus[numero_individu].afegir_tret(tret)

    def treure_tret(self, tret, numero_individu):
        self.__individus[numero_individu].treure_tret(tret)

    def individu(self, numero_individu):
        return self.__individus[numero_individu]
    
    def consulta_individu(self):
        numero_individu = int(item())
        print(f"consulta_individu {numero_individu}")
        if numero_individu < 1 or numero_individu > self.numero_individus:
            print("  error")
        else:
            print(self.__individus[numero_individu])

    def __llegir_arbre(self, marca = 0):
        x = int(item())
        if x != marca:
            l = self.__llegir_arbre(marca)
            r = self.__llegir_arbre(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def __arbre_distribucio_tret(self, arbre, tret):
        if arbre == None:
            return None
        elif arbre.leaf():
            if self.__individus[arbre.get_root()].te_tret(tret):
                return arbre
            else:
                return None
        elif self.__individus[arbre.get_root()].te_tret(tret):
            return BinTree(arbre.get_root(), self.__arbre_distribucio_tret(arbre.get_left(), tret), self.__arbre_distribucio_tret(arbre.get_right(), tret))
        else:
            res_l = self.__arbre_distribucio_tret(arbre.get_left(), tret)
            res_r = self.__arbre_distribucio_tret(arbre.get_right(), tret)
            if res_l == res_r == None:
                return None
            else:
                return BinTree(-(arbre.get_root()), res_l, res_r)
        
    

    
        


