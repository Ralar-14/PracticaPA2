from pytokr import items, item
from class_conjunt_individus import conjunt_individus
from class_conjunt_trets import conjunt_trets

instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        experiment_actual = conjunt_individus(int(item()),int(item()))
        trets_actuals = conjunt_trets(experiment_actual)
    
    elif instruccio == 'afegir_tret':
        trets_actuals.afegir_tret(item(),int(item()))
    
    elif instruccio == 'treure_tret':
        trets_actuals.treure_tret(item(), int(item()))
    
    elif instruccio == 'consulta_tret':
        trets_actuals.consulta_tret(item())
        
    elif instruccio == 'consulta_individu':
        experiment_actual.consulta_individu(int(item()))
        
    elif instruccio == 'distribucio_tret':
        trets_actuals.distribucio_tret(item())
    
    instruccio = item()
print("fi")

