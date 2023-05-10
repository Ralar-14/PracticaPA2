class Parell_Cromosomes:
    def __init__ (self, cromosoma1, cromosoma2):
        self.__cromosoma1 = cromosoma1
        self.__cromosoma2 = cromosoma2

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
    
    def __str__ (self):
        a, b = "  ", "  "
        for i in self.__cromosoma1:
            a += f"{i} "
        for i in self.__cromosoma2:
            b += f"{i} "
        return a + "\n" + b 