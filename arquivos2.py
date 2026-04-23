from pathlib import Path

nome = input('Digite seu nome: ')
path = Path('guest.txt')
path.write_text(nome)

lista_nomes = ''
while True:
    user_name = input('Digite o nome do usuário: ')
    
    if user_name.upper() == 'Q':
        print('Você saiu do programa...')
        break
        
    else:
        lista_nomes += user_name + '\n'

usuarios = Path('gues_book.txt')
usuarios.write_text(lista_nomes)