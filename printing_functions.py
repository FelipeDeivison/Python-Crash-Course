#Módulo usado no arquivo funcoes9.py (IMPORTANDO FUNÇÕES)
def print_models(unprinted_designs, completes_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completes_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following modeld have been printed:')
    for completed_model in completed_models:
        print(completed_model)