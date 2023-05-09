from class_parell_cromosomes import Parell_Cromosomes

class individu:
    def __init__(self, cromosomes, m):
        self.__parell = Parell_Cromosomes(list(cromosomes[:m]), list(cromosomes[m:]))
        self.__trets = set()
    
    def afegir_tret(self, tret):
        self.__trets.add(tret)

    def __str__(self):
        trets = ""
        for i in self.__trets:
            trets += f"\n  {i}"
        return str(self.__parell) + trets



