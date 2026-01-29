#f-string
nome = 'Felipe'
sobrenome = 'Deivison'
nome_inteiro = f'{nome} {sobrenome} Angelo'
print(nome_inteiro)

#title, rstrip, lstrip, strip, \n e \t

print(f'\nolá, {nome_inteiro}'.title())

menssage = f'\nolá, {nome_inteiro}'.title()
print(menssage)

favorite_linguage = 'Python '
print(favorite_linguage)
print(favorite_linguage.rstrip())
linguage = ' Python'
print(linguage)
print(linguage.lstrip())
linguage = '\n Python '
print(linguage.strip())

#removeprefix()
nostarch_url = 'https:\\nostarch.com'
print(nostarch_url.removeprefix('https:\\'))
