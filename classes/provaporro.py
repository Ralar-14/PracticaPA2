import copy

class parell_cromosomes:
    def __init__ (self, cromosomes=""):
        self.__crear_estructura(cromosomes)
    
    def __crear_estructura(self, cromosomes):
        '''
        Els cromosomes venen definits per una llista de enters. 0 representa (0,0), 1 representa (0,1), 2 representa (1,0) i 3 representa (1,1))
        '''
        self.__llista_parelles = [0] * (len(cromosomes)//2)
        for i in range(len(cromosomes)//2):
            if cromosomes[i] == "1":
                self.__llista_parelles[i] = 2
        for i in range(len(cromosomes)//2):
            if cromosomes[i + len(cromosomes)//2] == "1":
                self.__llista_parelles[i] += 1
        self.__primera_llista_parelles = copy.deepcopy(self.__llista_parelles)
    
    
    def interseccio(self, parell):
        for i in range(len(self.__llista_parelles)):
            if self.__llista_parelles[i] != parell.__llista_parelles[i]:
                self.__llista_parelles[i] = "-"
    
    def reiniciar(self):
        self.__llista_parelles = copy.deepcopy(self.__primera_llista_parelles)
    
    def __str__ (self):
        str1, str2 = "  ", "  "
        for i in self.__llista_parelles:
            if i == 0:
                str1 += "0 "
                str2 += "0 "
            elif i == 1:
                str1 += "0 "
                str2 += "1 "
            elif i == 2:
                str1 += "1 "
                str2 += "0 "
            elif i == 3:
                str1 += "1 "
                str2 += "1 "
            else:
                str1 += "- "
                str2 += "- "
        return str1 + "\n" + str2
    



    
