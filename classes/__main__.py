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
        pass
    # ...llegir dades addicionals i processar 'afegir_tret'
    elif instruccio == 'treure_tret': # només grups 3 persones
        pass
    # ...llegir dades addicionals i processar 'treure_tret'
    elif instruccio == 'consulta_tret':
        pass
    # ...llegir dades addicionals i processar 'consulta_tret'
    elif instruccio == 'consulta_individu':
        numero = int(item())
        info = experiment_actual.informació_individu(numero)
        print(f"consulta_individu {numero}")
        print(info)
        pass
    # ...llegir dades addicionals i processar 'consulta_individu'
    elif instruccio == 'distribucio_tret':
        pass
    # ...llegir dades addicionals i processar 'distribucio_tret'
    instruccio = item()
