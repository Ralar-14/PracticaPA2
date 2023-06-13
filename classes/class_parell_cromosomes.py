class parell_cromosomes:
    def __init__ (self, cromosomes=""):
        self.__cromosomes_sup = cromosomes[0:len(cromosomes)//2]
        self.__cromosomes_inf = cromosomes[len(cromosomes)//2:len(cromosomes)]

    def interseccio(self, nou_parell):
        if self.__cromosomes_sup == "":
            self.__cromosomes_sup = nou_parell.__cromosomes_sup
            self.__cromosomes_inf = nou_parell.__cromosomes_inf
        else:
            for i in range(len(self.__cromosomes_sup)):
                if self.__cromosomes_sup[i] != nou_parell.__cromosomes_sup[i]:
                    self.__cromosomes_sup = self.__cromosomes_sup[:i] + "-" + self.__cromosomes_sup[i+1:]
                    self.__cromosomes_inf = self.__cromosomes_inf[:i] + "-" + self.__cromosomes_inf[i+1:]
                elif self.__cromosomes_inf[i] != nou_parell.__cromosomes_inf[i]:
                    self.__cromosomes_sup = self.__cromosomes_sup[:i] + "-" + self.__cromosomes_sup[i+1:]
                    self.__cromosomes_inf = self.__cromosomes_inf[:i] + "-" + self.__cromosomes_inf[i+1:]

    def reiniciar(self):
        self.__cromosomes_sup = ""
        self.__cromosomes_inf = ""
                
    def __str__ (self):
        return f"  {self.__cromosomes_sup}" + "\n" + f"  {self.__cromosomes_inf}"  
    



