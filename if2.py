# nomes = ['Admin', 'Felipe', 'Natiara', 'Francisca', 'Eliezer']
nomes =[]

if nomes:
    for nome in nomes:
        if nome == 'Admin':
            print('Olá Administrador, gostaria de ver o relatório de status?')
        else:
            print(f'Bem-vindo de volta {nome}!')
else:
    print('Usuários não encontrados!')



current_users = ['Admin', 'Felipe', 'Natiara', 'Francisca', 'Eliezer']
new_users = ['Admin', 'Felipe', 'Natiara', 'Francisca', 'Eliezer', 'João',
             'Maria']
for new_user in new_users:
    if new_user in current_users:
        print(f'O Usuário {new_user} já em uso, por favor utilize outro nome!')
    else:
        print(f'O nome {new_user} está disponivel')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')