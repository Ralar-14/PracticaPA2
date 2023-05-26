from pytokr import items, item
from class_conjunt_individus import conjunt_individus
from class_conjunt_trets import conjunt_trets

# ...importar les classes que calgui, fetes per vosaltres
# ...inicialitzacions


instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        num_individus = int(item())
        num_cromosomes = int(item())
        experiment_actual = conjunt_individus(num_individus,num_cromosomes)
        for _ in range(0, num_individus):
            experiment_actual.afegir_individu(item())
        trets_actuals = conjunt_trets(experiment_actual)
        print(f"experiment {num_individus} {num_cromosomes}")
        pass
    # ...llegir dades addicionals i processar 'experiment'
    elif instruccio == 'afegir_tret':
        tret = item()
        individu = int(item())
        print(f"afegir_tret {tret} {individu}")
        if experiment_actual.individu(individu).te_tret(tret):
            print(" error")
        else:
            trets_actuals.afegir_tret(tret, individu)
        pass
    # ...llegir dades addicionals i processar 'afegir_tret'
    elif instruccio == 'treure_tret': # només grups 3 persones
        tret = item()
        individu = int(item())
        print(f"treure_tret {tret} {individu}")
        if not experiment_actual.individu(individu).te_tret(tret):
            print(" error")
        else:
            trets_actuals.treure_tret(tret, individu)
        
        pass
    # ...llegir dades addicionals i processar 'treure_tret'
    elif instruccio == 'consulta_tret':
        tret = item()
        print(f"consulta_tret {tret}")
        if not trets_actuals.existeix_tret(tret):
            print(" error")
        else:
            trets_actuals.info_tret(tret)
        pass
    # ...llegir dades addicionals i processar 'consulta_tret'
    elif instruccio == 'consulta_individu':
        numero = int(item())
        individu = experiment_actual.individu(numero)
        print(f"consulta_individu {numero}")
        print(individu)
        pass
    # ...llegir dades addicionals i processar 'consulta_individu'
    elif instruccio == 'distribucio_tret':
        tret = item()
        print(f"distribucio_tret {tret}")
        if not trets_actuals.existeix_tret(tret):
            print(" error")
        else:
            inordre = experiment_actual.inordre_distribucio(tret)
            for i in inordre:
                print(f"  {i}", end="")
            print()
    # ...llegir dades addicionals i processar 'distribucio_tret'
    instruccio = item()
print("fi")

