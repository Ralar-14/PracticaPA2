from random import *

num_individus = 10
num_cromosomes = 10
num_experiments = 10

num_afegir = 10
num_treure = 10
num_consulta_t = 10
num_consulta_i = 10
num_distribucio_t = 10

for _ in range(num_experiments):
    print("experiment " + str(num_individus) + " " + str(num_cromosomes))
    def rand_key(p):
        key1 = ""
        for _ in range(p):
            temp = str(randint(0, 1))
            key1 += temp
        return(key1)

    for i in range(num_individus):
        str1 = rand_key(num_cromosomes*2)
        print(str1)
    print("\n")
    for _ in range(0, num_afegir):
        print("afegir_tret tret_" + str(randint(0,10)) + " " + str(randint(0,num_individus)))
    for _ in range(0, num_treure):
        print("treure_tret tret_" + str(randint(0,10)) + " " + str(randint(0,num_individus)))
    for _ in range(0, num_consulta_t):
        print("consulta_tret tret_" + str(randint(0,10)))
    for _ in range(0, num_consulta_i):
        print("consulta_individu " + str(randint(0,num_individus)))
    for _ in range(0, num_distribucio_t):
        print("distribucio_tret tret_" + str(randint(0,10)))

    print("fi \n")

