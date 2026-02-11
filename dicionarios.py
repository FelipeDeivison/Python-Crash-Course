pessoa = {
    'first_name': 'Felipe',
    'last_name': 'Angelo',
    'age': '23',
    'city': 'Bela Cruz',
}
print(pessoa)

favorites_numbers = {
    'natiara': '20',
    'felipe': '8',
    'nathan': '13',
    'roberta': '18',
    'francisca': '28',
}
print(favorites_numbers)

glossario = {
    'variável': 'É um nome que você cria para guardar algum valor na memória'
    ' do computador.',
    'atribuição': 'É o ato de dar um valor a uma variável usando o sinal =',
    'terminal': 'É um programa onde você digita comandos para o computador'
    ' executar.',
    'loop': 'É uma estrutura que repete um bloco de código várias vezes.',
    'repositorio': 'É um local onde você guarda e organiza seu código,'
    ' podendo salvar versões e compartilhar com outras pessoas.',
}

for chave, valor in glossario.items():
    print(f'{chave.title()}: {valor}\n')