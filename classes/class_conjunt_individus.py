from pytokr import item, items
from class_individu import individu
from class_bintree import BinTree

class conjunt_individus:
    def __init__(self, numero_individus, numero_cromosomes, marca = 0):
        self.__numero_individus = numero_individus
        self.__numero_cromosomes = numero_cromosomes
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
        self.__individus.append(individu(cromosomes, self.__numero_cromosomes))

    def afegir_tret(self, tret, individu):
        self.__individus[individu].afegir_tret(tret)

    def treure_tret(self, tret, individu):
        self.__individus[individu].treure_tret(tret)

    def individu(self, numero_individu):
        return self.__individus[numero_individu]
    
    def numero_cromosomes(self):
        return self.__numero_cromosomes
    
    def cromosomes_comuns(self, conjunt_individus):
    #Input : conjunt_individus es un set amb enters
    #Output: cromosomes en comú dels individus indicats
        numero_individus = len(conjunt_individus)
        parelles = []
        for i in conjunt_individus:
            parelles.append(self.__individus[i].obtenir_parelles())
        resultat = parelles[0]
        for i in range(1, numero_individus):
            resultat = self.__interseccio(resultat, parelles[i])
        return self.__parelles_a_cromosomes(resultat)

    def __interseccio(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                a[i] = ("-","-")
        return a
    
    def __parelles_a_cromosomes(self, parelles):
        primer = ""
        segon = ""
        for a in parelles:
            primer += a[0]
            segon += a[1]
        return primer + segon




        
    

    
        


