#Importem la funció item per poder llegir el fitxer input. També importem les classes conjunt_individus i conjunt_trets.

from pytokr import item
from class_conjunt_individus import conjunt_individus
from class_conjunt_trets import conjunt_trets

#Bucle que llegeix el fitxer input i executa les instruccions corresponents.

instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        """
        Crea un nou conjunt d'individus (experiment) i un nou conjunt de trets vinculat a aquest experiment.
        Aquestes instàncies s'asignen a les variables experiment_actual i trets_actuals, i seran les que s'utilitzaran
        per executar les altres instruccions.
        """
        experiment_actual = conjunt_individus()
        trets_actuals = conjunt_trets(experiment_actual)
    
    elif instruccio == 'afegir_tret':
        trets_actuals.afegir_tret()
    
    elif instruccio == 'treure_tret':
        trets_actuals.treure_tret()
    
    elif instruccio == 'consulta_tret':
        trets_actuals.consulta_tret()
        
    elif instruccio == 'consulta_individu':
        experiment_actual.consulta_individu()
        
    elif instruccio == 'distribucio_tret':
        trets_actuals.distribucio_tret()
    
    instruccio = item()
print("fi")

