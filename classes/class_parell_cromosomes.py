class parell_cromosomes:
    def __init__ (self, cromosomes):
        self.__cromosoma1 = list(cromosomes[len(cromosomes)//2:]) #Dividim la llista de cromosomes en dues parts
        self.__cromosoma2 = list(cromosomes[len(cromosomes)//2:])

    """
    def get_cromosoma1(self):
        return self.__cromosoma1
    
    def get_cromosoma2(self):
        return self.__cromosoma2
    def modificacio(self, cromosomes, numero_cromosomes):
        self.__cromosoma1 = list(cromosomes[:numero_cromosomes])
        self.__cromosoma2 = list(cromosomes[numero_cromosomes:])
   """
   
    def __str__ (self):
        a, b = "  ", "  "
        for i in self.__cromosoma1:
            a += f"{i} "
        for i in self.__cromosoma2:
            b += f"{i} "
        return a + "\n" + b 