from pytokr import item, items
from class_individu import individu
from class_bintree import BinTree

class conjunt_individus:
    
    def __init__(self, num_individus, num_cromosomes, marca = 0):
        self.numero_individus = num_individus
        self.numero_cromosomes = num_cromosomes
        self.__individus = [None]
        self.__arbre = self.__llegir_arbre(marca)
        for _ in range(0, self.numero_individus):
            self.afegir_individu(item())
        print(f"experiment {self.numero_individus} {self.numero_cromosomes}")
    
    def __llegir_arbre(self, marca):
        x = int(item())
        if x != marca:
            l = self.__llegir_arbre(marca)
            r = self.__llegir_arbre(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def inordre_distribucio(self, tret):
        inordre = self.__arbre_distribucio_tret(self.__arbre, tret)
        if inordre == None:
            return []
        else:
            return self.__arbre_distribucio_tret(self.__arbre, tret).inorder()
    
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
            
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))

    def afegir_tret(self, tret, numero_individu):
        self.__individus[numero_individu].afegir_tret(tret)

    def treure_tret(self, tret, numero_individu):
        self.__individus[numero_individu].treure_tret(tret)

    def individu(self, numero_individu):
        return self.__individus[numero_individu]
    
    def consulta_individu(self, numero_individu):
        print(f"consulta_individu {numero_individu}")
        print(self.__individus[numero_individu])


        
    

    
        


