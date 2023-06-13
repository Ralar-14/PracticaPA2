from class_parell_cromosomes import parell_cromosomes
from collections import namedtuple

Tret = namedtuple("tret", ["parell_tret", "individus"])

class conjunt_trets:
    def __init__(self, experiment):
        self.__experiment = experiment
        self.__trets = {}
        
    def afegir_tret(self, tret, numero_individu):
        print(f"afegir_tret {tret} {numero_individu}")
        if tret in self.__trets:
            if numero_individu in self.__trets[tret].individus:
                print("  error")
            else:
                self.__experiment.afegir_tret(tret, numero_individu)
                self.__trets[tret].individus.add(numero_individu)
                self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(numero_individu).parell())
        else:
            self.__experiment.afegir_tret(tret, numero_individu)
            self.__trets[tret] = Tret(parell_cromosomes(), {numero_individu})
            self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(numero_individu).parell())
    
    def treure_tret(self, tret, numero_individu):
        print(f"treure_tret {tret} {numero_individu}")
        if not numero_individu in self.__trets[tret].individus:
            print("  error")
        else:
            self.__experiment.treure_tret(tret, numero_individu)
            if len(self.__trets[tret].individus) == 1:
                self.__trets.pop(tret)
            else:
                self.__trets[tret].individus.remove(numero_individu)
                self.__trets[tret].parell_tret.reiniciar()
                for a in self.__trets[tret].individus:
                    self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(a).parell())
    
    def distribucio_tret(self, tret):
        print(f"distribucio_tret {tret}")
        if not tret in self.__trets:
            print("  error")
        else:
            inordre = self.__experiment.inordre_distribucio(tret)
            print(end=" ")
            for i in inordre:
                print(f" {i}", end="")
            print()
    
    def consulta_tret(self, tret):
        print(f"consulta_tret {tret}")
        if not tret in self.__trets:
            print("  error")    
        else:
            print(f"  {tret}")
            print(self.__trets[tret].parell_tret)
            for a in self.__trets[tret].individus:
                print(f"  {a}")

    
        



    


        



    