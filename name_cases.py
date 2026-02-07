felipe = 'Olá, Felipe! tudo bem?'
print(felipe)
pessoa = 'Felipe Deivison'
print(pessoa.lower())
print(pessoa.upper())
print(pessoa.title())

autor = 'Steve Jobs'
citacao = (
    '“Seu trabalho vai preencher boa parte da sua vida, e a única maneira de '
    'estar realmente satisfeito é fazer o que você acredita ser um ótimo '
    'trabalho. E a única maneira de fazer um ótimo trabalho é amar '
    'o que você faz.”'
    )
print(f'{autor} disse uma vez: {citacao}')

famous_person = ' Steve Jobs '
message = (
    '“Seu trabalho vai preencher boa parte da sua vida, e a única maneira de '
    'estar realmente satisfeito é fazer o que você acredita ser um ótimo '
    'trabalho. E a única maneira de fazer um ótimo trabalho é amar '
    'o que você faz.”'
    )

print(f'{famous_person.lstrip().rstrip()} disse uma vez:\n \t{message.strip()}')

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))