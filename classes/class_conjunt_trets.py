#Importem la funció item per poder llegir el fitxer input. També la classe parell_cromosomes.
#També importem la estructura de dades namedtuple. Aquesta estructura de dades ens permet crear una tupla 
#etiquetada, i ens facilita l'accés als seus elements. 

from pytokr import item
from class_parell_cromosomes import parell_cromosomes
from collections import namedtuple

#Definim la tupla Tret, que conté el parell de cromosomes i el conjunt d'individus que tenen aquest tret.
Tret = namedtuple("tret", ["parell_tret", "individus"])

class conjunt_trets:
    def __init__(self, experiment):
        """
        Pre: experiment és una instància de la classe conjunt_individus.
        Inicialitza el conjunt de trets relacionat amb l'experiment.
        """
        self.__experiment = experiment
        self.__trets = {}
        
    def afegir_tret(self):
        """
        Si el tret no existeix, crea el tret, afegeix el tret al individu i calcula la combinació de parells. 
        Si el tret existeix i el individu no té el tret, afegeix el tret al individu i calcula la combinació de parells. 
        En cas contrari, escriu error a la sortida.
        """
        tret = item()
        numero_individu = int(item())
        print(f"afegir_tret {tret} {numero_individu}")
        if tret in self.__trets:    #Si el tret ja existeix
            if numero_individu in self.__trets[tret].individus:   #Si l'individu ja té el tret
                print("  error")
            else:   #Si l'individu no té el tret
                self.__experiment.afegir_tret(tret, numero_individu)
                self.__trets[tret].individus.add(numero_individu)
                self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(numero_individu).parell())
        else:    #Si el tret no existeix
            self.__experiment.afegir_tret(tret, numero_individu)
            self.__trets[tret] = Tret(parell_cromosomes(), {numero_individu})
            self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(numero_individu).parell())
    
    def treure_tret(self):
        """
        Si el tret existeix i el individu té el tret, treu el tret al individu i es calcula la nova combinació de parells.
        En cas de que sigui el últim individu amb aquest tret, elimina el tret.
        En cas contrari, escriu error a la sortida.
        """
        tret = item()
        numero_individu = int(item())
        print(f"treure_tret {tret} {numero_individu}")
        if not tret in self.__trets: #Si el tret no existeix
            print("  error")
        else:    #Si el tret existeix
            if not numero_individu in self.__trets[tret].individus: #Si l'individu no té el tret
                print("  error")
            else: #Si l'individu té el tret
                self.__experiment.treure_tret(tret, numero_individu)
                if len(self.__trets[tret].individus) == 1:
                    self.__trets.pop(tret)
                else:
                    self.__trets[tret].individus.remove(numero_individu)
                    self.__trets[tret].parell_tret.reiniciar()
                    for a in self.__trets[tret].individus:
                        self.__trets[tret].parell_tret.interseccio(self.__experiment.individu(a).parell())
    
    def distribucio_tret(self):
        """
        Si el tret existeix, escriu la distribució del tret a la sortida.
        En cas contrari, escriu error a la sortida.
        """
        tret = item()
        print(f"distribucio_tret {tret}")
        if not tret in self.__trets: #Si el tret no existeix
            print("  error")
        else: #Si el tret existeix
            inordre = self.__experiment.inordre_distribucio(tret)
            print(end=" ")
            for i in inordre:
                print(f" {i}", end="")
            print()
    
    def consulta_tret(self):
        """
        Si el tret existeix, escriu la informació del tret a la sortida.
        En cas contrari, escriu error a la sortida.
        """
        tret = item()
        print(f"consulta_tret {tret}")
        if not tret in self.__trets: #Si el tret no existeix
            print("  error")    
        else: #Si el tret existeix
            print(f"  {tret}")
            print(self.__trets[tret].parell_tret)
            individus = sorted(self.__trets[tret].individus)
            for a in individus:
                print(f"  {a}")

    
        



    


        



    