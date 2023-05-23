from pytokr import item, items
from class_individu import individu
from class_bintree import BinTree

class conjunt_individus:
    def __init__(self, numero_individus, numero_cromosomes, marca = 0):
        #self.__numero_individus = numero_individus
        #self.__numero_cromosomes = numero_cromosomes
        self.__individus = [None]
        self.__arbre = self.__llegir_arbre(marca)
    """
    def introduir_arbre(self, marca):
        self.__arbre = self.llegir_arbre(marca)
    """
    def __llegir_arbre(self, marca):
        x = int(item())
        if x != marca:
            l = self.__llegir_arbre(marca)
            r = self.__llegir_arbre(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))

    def afegir_tret(self, tret, numero_individu):
        self.__individus[numero_individu].afegir_tret(tret)

    def treure_tret(self, tret, numero_individu):
        self.__individus[numero_individu].treure_tret(tret)

    def individu(self, numero_individu):
        return self.__individus[numero_individu]
    


        
    

    
        


