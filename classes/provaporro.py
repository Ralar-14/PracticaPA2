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
    


class parell_cromosomes_trets:
    def __init__ (self, primer_parell):
        self.__llista_combinacions_parelles = [[0,0,0,0] for _ in range(len(primer_parell._llista_parelles))]
        for i in range(len(primer_parell._llista_parelles)):
            self.__llista_combinacions_parelles[i][primer_parell._llista_parelles[i]] += 1

    def afegir_parell(self, parell_cromosomes):
        for i in range(len(parell_cromosomes._llista_parelles)):
            self.__llista_combinacions_parelles[i][parell_cromosomes._llista_parelles[i]] += 1

    def treure_parell(self, parell_cromosomes):
        for i in range(len(parell_cromosomes._llista_parelles)):
            self.__llista_combinacions_parelles[i][parell_cromosomes._llista_parelles[i]] -= 1

    def __str__(self):
        str1, str2 = "  ", "  "
        for i in range(len(self.__llista_combinacions_parelles)):
            suma = sum(self.__llista_combinacions_parelles[i])
            if self.__llista_combinacions_parelles[i][0] == suma:
                str1 += "0 "
                str2 += "0 "
            elif self.__llista_combinacions_parelles[i][1] == suma:
                str1 += "0 "
                str2 += "1 "
            elif self.__llista_combinacions_parelles[i][2] == suma:
                str1 += "1 "
                str2 += "0 "
            elif self.__llista_combinacions_parelles[i][3] == suma:
                str1 += "1 "
                str2 += "1 "
            else:
                str1 += "- "
                str2 += "- "
        return str1 + "\n" + str2
