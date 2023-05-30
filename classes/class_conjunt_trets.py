from class_parell_cromosomes_trets import parell_cromosomes_trets
from collections import namedtuple

Tret = namedtuple("tret", ["parell_tret", "individus"])

class conjunt_trets:
    def __init__(self, experiment):
        self.__experiment = experiment
        self.__trets = {}
        
  
    def afegir_tret(self, tret, numero_individu):
        self.__experiment.afegir_tret(tret, numero_individu)
        if tret in self.__trets:
            if numero_individu not in self.__trets[tret][1]:
                self.__trets[tret].individus.add(numero_individu)
                self.__trets[tret].parell_tret.afegir_parell(self.__experiment.individu(numero_individu).parell())
        else:
            self.__trets[tret] = Tret(parell_cromosomes_trets(self.__experiment.individu(numero_individu).parell()), {numero_individu})
        
    def treure_tret(self, tret, numero_individu):
        if numero_individu in self.__trets[tret].individus:
            self.__experiment.treure_tret(tret, numero_individu)
            if len(self.__trets[tret][1]) == 1:
                self.__trets.pop(tret)
            else:
                self.__trets[tret].individus.remove(numero_individu)
                self.__trets[tret].parell_tret.treure_parell(self.__experiment.individu(numero_individu).parell())
        
    def existeix_tret(self, tret):
        return tret in self.__trets
    
    def info_tret(self, tret):
        if tret in self.__trets:
            print(f"  {tret}")
            print(self.__trets[tret][0])
            for a in self.__trets[tret][1]:
                print(f"  {a}")

    
        



    


        



    