class conjunt_trets:
    def __init__(self, experiment):
        self.__experiment = experiment
        self.__trets = {}

    def afegir_tret(self, tret, individu):
        self.__experiment.afegir_tret(tret, individu)
        if tret in self.__trets:
            self.__trets[tret][1].add(individu)
        else:
            self.__trets[tret] = (None, {individu})
        self.__actualitzar_tret(tret)

    def __actualitzar_tret(self, tret):
        pass
        



    


        



    