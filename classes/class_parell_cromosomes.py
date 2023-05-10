class parell_cromosomes:
    def __init__ (self, cromosomes="", numero_cromosomes=0):
        self.__cromosoma1 = list(cromosomes[:numero_cromosomes])
        self.__cromosoma2 = list(cromosomes[numero_cromosomes:])

    """
    def get_cromosoma1(self):
        return self.__cromosoma1
    
    def get_cromosoma2(self):
        return self.__cromosoma2
    """

    def obtenir_parelles(self):
        a = self.__cromosoma1   #Guardem les dues llistes en dues variables per estalviar crides als mètodes
        b = self.__cromosoma2
        return [(a[i],b[i]) for i in range(0,len(self.__cromosoma1))]  
    
    def modificacio(self, cromosomes, numero_cromosomes):
        self.__cromosoma1 = list(cromosomes[:numero_cromosomes])
        self.__cromosoma2 = list(cromosomes[numero_cromosomes:])
   
    def __str__ (self):
        a, b = "  ", "  "
        for i in self.__cromosoma1:
            a += f"{i} "
        for i in self.__cromosoma2:
            b += f"{i} "
        return a + "\n" + b 