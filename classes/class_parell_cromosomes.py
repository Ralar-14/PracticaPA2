class parell_cromosomes:
    def __init__ (self, cromosomes=""):
        self.__crear_estructura(cromosomes)
    
    def __crear_estructura(self, cromosomes):
        '''
        Els cromosomes venen definits per una llista de enters. 0 representa (0,0), 1 representa (0,1), 2 representa (1,0) i 3 representa (1,1))
        '''
        self._llista_parelles = [0] * (len(cromosomes)//2)
        for i in range(len(cromosomes)//2):
            if cromosomes[i] == "1":
                self._llista_parelles[i] = 2
        for i in range(len(cromosomes)//2):
            if cromosomes[i + len(cromosomes)//2] == "1":
                self._llista_parelles[i] += 1
                
    def __str__ (self):
        str1, str2 = "  ", "  "
        for i in self._llista_parelles:
            if i == 0:
                str1 += "0"
                str2 += "0"
            elif i == 1:
                str1 += "0"
                str2 += "1"
            elif i == 2:
                str1 += "1"
                str2 += "0"
            else:
                str1 += "1"
                str2 += "1"
        return str1 + "\n" + str2
    



