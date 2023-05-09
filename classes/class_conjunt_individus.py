from class_individu import individu

class conjunt_individus:
    def __init__(self, numero_individus, numero_cromosomes, arbre, individus):
        assert len(individus) == numero_individus
        self.__numero_individus = numero_individus
        self.__numero_cromosomes = numero_cromosomes
        self.__arbre = arbre
        self.__individus = [None] + [individu(i, numero_cromosomes) for i in individus]
        for i in self.__individus:
            print(i)

a = conjunt_individus(4,4,"hola",["00110111", "00110110", "00110101", "11110111"])
