from provaporro import parell_cromosomes

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
    
    def __str__(self):
        trets = ""
        for i in self.__trets:
            trets += f"\n  {i}"
        return str(self.__parell) + trets



