from Parell import Parell_Cromosomes

class Individu:
    def __init__(self, llista1, llista2):
        self.__parell = Parell_Cromosomes(llista1, llista2)
        self.__atributs = set()

    def obtenir_atribut(self, atribut):
        self.__atributs.add(atribut)

    def __str__(self):
        atr = ""
        for i in self.__atributs:
            atr+=f"\n{i}"
        return str(self.__parell) + atr

m = 4

a = Individu([1,0,1,1],[0,1,1,0])
a.obtenir_atr("trompa")
a.obtenir_atr("potes")
print(a)
