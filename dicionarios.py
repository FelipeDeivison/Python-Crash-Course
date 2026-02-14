pessoa = {
    'first name': 'Felipe',
    'last name': 'Angelo',
    'age': '23',
    'city': 'Bela Cruz',
}
for key, value in pessoa.items():
    print(f'\n{key.title()}: {value}')

favorites_numbers = {
    'natiara': '20',
    'felipe': '8',
    'nathan': '13',
    'roberta': '18',
    'francisca': '28',
}
for pessoa, numero in favorites_numbers.items():
    print(f'\nO número favorito de {pessoa.title()} é {numero}')

glossario = {
    'variável': 'É um nome que você cria para guardar algum valor na memória'
    ' do computador.',
    'atribuição': 'É o ato de dar um valor a uma variável usando o sinal =',
    'terminal': 'É um programa onde você digita comandos para o computador'
    ' executar.',
    'loop': 'É uma estrutura que repete um bloco de código várias vezes.',
    'repositorio': 'É um local onde você guarda e organiza seu código,'
    ' podendo salvar versões e compartilhar com outras pessoas.',
    'Função': 'É um bloco de código reutilizável que executa uma tarefa.',
    'Lista' : 'É uma coleção ordenada de elementos que pode mudar.',
    'Dicionário': 'É uma coleção de pares chave-valor.',
    'Loop': 'É uma estrutura que repete uma ação enquanto uma condição for'
    ' verdadeira.'
}

for chave, valor in glossario.items():
    print(f'\n{chave.title()}: {valor}')