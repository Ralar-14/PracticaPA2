from class_parell_cromosomes import parell_cromosomes

class individu:
    def __init__(self, cromosomes, m):
        self.__parell = parell_cromosomes(cromosomes, m)
        self.__trets = set()
    
    def afegir_tret(self, tret):
        self.__trets.add(tret)

    def obtenir_parelles(self):
        return self.__parell.obtenir_parelles()

    def __str__(self):
        trets = ""
        for i in self.__trets:
            trets += f"\n  {i}"
        return str(self.__parell) + trets



