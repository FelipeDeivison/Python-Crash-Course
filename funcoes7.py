def sanduiche(*ingredientes):
    '''A função recebe como parâmetros, ingrediente para um sanduiche'''
    si = []
    for ingrediente in ingredientes:
        si.append(ingrediente)
        
    ingredientes_san = ', '.join(si)
    print(f'O sanduíche irá conter {ingredientes_san}')

sanduiche('Pão Francês', 'Calabresa')

def build_profile(first, last, **user_infos):
    '''A função cria um perfil com nome e sobrenome e outras informações
      de um usuário'''
    user_infos['name: '] = first
    user_infos['last name: '] =  last
    return user_infos
user_infos = build_profile('Felipe', 'Angelo', 
                           location = 'São Paulo', 
                           idade= '23')
print(user_infos)
