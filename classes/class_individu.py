from class_parell_cromosomes import parell_cromosomes

class individu:
    def __init__(self, cromosomes):
        self.__parell = parell_cromosomes(cromosomes)
        self.__trets = set()
    
    def afegir_tret(self, tret):
        self.__trets.add(tret)

    def treure_tret(self, tret):
        self.__trets.remove(tret)

    def parell(self):
        return self.__parell
    
    def te_tret(self, tret):
        return tret in self.__trets
    
    def __str__(self):
        trets = ""
        for i in sorted(self.__trets):
            trets += f"\n  {i}"
        return str(self.__parell) + trets



