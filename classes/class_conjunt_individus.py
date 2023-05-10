from pytokr import item, items
from class_individu import individu
from class_bintree import BinTree

class conjunt_individus:
    def __init__(self, numero_individus, numero_cromosomes, marca = 0):
        self.__numero_individus = numero_individus
        self.__numero_cromosomes = numero_cromosomes
        self.__individus = [None]
        self.__arbre = self.llegir_arbre(marca)
    """
    def introduir_arbre(self, marca):
        self.__arbre = self.llegir_arbre(marca)
    """
    def llegir_arbre(self, marca):
        x = int(item())
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes, self.__numero_cromosomes))
        
    

    
        

a = conjunt_individus(4,4,"hola",["00110111", "00110110", "00110101", "11110111"])
