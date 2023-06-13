class parell_cromosomes:
    
    def __init__ (self, cromosomes=""):
        self.__num_cromosomes = len(cromosomes)//2
        self.__cromosomes_sup = cromosomes[:self.__num_cromosomes]
        self.__cromosomes_inf = cromosomes[self.__num_cromosomes:]

    def interseccio(self, nou_parell):
        if self.__num_cromosomes == 0:
            self.__num_cromosomes = nou_parell.__num_cromosomes
            self.__cromosomes_sup = nou_parell.__cromosomes_sup
            self.__cromosomes_inf = nou_parell.__cromosomes_inf
        else:
            nou_superior = ""
            nou_inferior = ""
            for i in range(self.__num_cromosomes):
                if self.__cromosomes_sup[i] != nou_parell.__cromosomes_sup[i]:
                    nou_superior += "-"
                    nou_inferior += "-"
                elif self.__cromosomes_inf[i] != nou_parell.__cromosomes_inf[i]:
                    nou_superior += "-"
                    nou_inferior += "-"
                else:
                    nou_superior += self.__cromosomes_sup[i]
                    nou_inferior += self.__cromosomes_inf[i]
            self.__cromosomes_sup = nou_superior
            self.__cromosomes_inf = nou_inferior

    def reiniciar(self):
        self.__num_cromosomes = 0
        self.__cromosomes_sup = ""
        self.__cromosomes_inf = ""
                
    def __str__ (self):
        return f"  {self.__cromosomes_sup}" + "\n" + f"  {self.__cromosomes_inf}"  
    
    