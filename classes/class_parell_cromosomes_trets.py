class parell_cromosomes_trets:
    def __init__ (self, primer_parell):
        self.__llista_combinacions_parelles = [[0,0,0,0] for _ in range(len(primer_parell._llista_parelles))]
        self.__num_individus = 0
        self.afegir_parell(primer_parell)
        
    def afegir_parell(self, parell_cromosomes):
        self.__num_individus += 1
        for i in range(len(parell_cromosomes._llista_parelles)):
            self.__llista_combinacions_parelles[i][parell_cromosomes._llista_parelles[i]] += 1

    def treure_parell(self, parell_cromosomes):
        self.__num_individus -= 1
        for i in range(len(parell_cromosomes._llista_parelles)):
            self.__llista_combinacions_parelles[i][parell_cromosomes._llista_parelles[i]] -= 1

    def __str__(self):
        str1, str2 = "  ", "  "
        for i in range(len(self.__llista_combinacions_parelles)):
            if self.__llista_combinacions_parelles[i][0] == self.__num_individus:
                str1 += "0"
                str2 += "0"
            elif self.__llista_combinacions_parelles[i][1] == self.__num_individus:
                str1 += "0"
                str2 += "1"
            elif self.__llista_combinacions_parelles[i][2] == self.__num_individus:
                str1 += "1"
                str2 += "0"
            elif self.__llista_combinacions_parelles[i][3] == self.__num_individus:
                str1 += "1"
                str2 += "1"
            else:
                str1 += "-"
                str2 += "-"
        return str1 + "\n" + str2