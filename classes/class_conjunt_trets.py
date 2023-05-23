from provaporro import parell_cromosomes
import copy

class conjunt_trets:
    def __init__(self, experiment):
        self.__experiment = experiment
        self.__trets = {}
  
    def afegir_tret(self, tret, numero_individu):
        self.__experiment.afegir_tret(tret, numero_individu)
        if tret in self.__trets:
            if numero_individu not in self.__trets[tret][1]:
                self.__trets[tret][1].add(numero_individu)
                self.__trets[tret][0].interseccio(self.__experiment.individu(numero_individu).parell())
        else:
            self.__trets[tret] = (copy.deepcopy(self.__experiment.individu(numero_individu).parell()), {numero_individu})

    def treure_tret(self, tret, individu):
        if individu in self.__trets[tret][1]:
            self.__experiment.treure_tret(tret, individu)
            if len(self.__trets[tret][1]) == 1:
                self.__trets.pop(tret)
            else:
                self.__trets[tret][1].remove(individu)
                self.__recalcular_tret(tret)

    def __recalcular_tret(self, tret):
        self.__trets[tret][0].reiniciar()
        llista_individus = []
        for i in self.__trets[tret][1]:
            self.__trets[tret][0].interseccio(self.__experiment.individu(i).parell())
        
    def info_tret(self, tret):
        if tret in self.__trets:
            print(f"  {tret}")
            print(self.__trets[tret][0])
            for a in self.__trets[tret][1]:
                print(f"  {a}")

    
        



    


        



    