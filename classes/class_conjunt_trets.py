from class_parell_cromosomes import parell_cromosomes

class conjunt_trets:
    def __init__(self, experiment):
        self.__experiment = experiment
        self.__trets = {}

    def afegir_tret(self, tret, individu):
        self.__experiment.afegir_tret(tret, individu)
        if tret in self.__trets:
            self.__trets[tret][1].add(individu)
        else:
            self.__trets[tret] = [None, {individu}]
        self.__actualitzar_tret(tret)

    def __individus_tret(self, tret):
        if tret in self.__trets:
            return self.__trets[tret][1]
        
    def info_tret(self, tret):
        print(tret)
        print(self.__trets[tret][0])
        for a in self.__trets[tret][1]:
            print(f"  {a}")

    def __actualitzar_tret(self, tret):
        cromosomes_tret = self.__experiment.cromosomes_comuns(self.__trets[tret][1])
        self.__trets[tret][0] = parell_cromosomes(cromosomes_tret, self.__experiment.numero_cromosomes())
        
        



    


        



    