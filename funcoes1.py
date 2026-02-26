def make_shirt(tamanho, frase):
    """Função que pede o tamanho da camiseta e a frase que deseja como 
    estampa."""
    print(f'O tamanho da camiseta será {tamanho.upper()}.\n'
          f'A frase na estampa será: "{frase.title()}\n"'
        )
    
make_shirt('m', 'i love Python')

make_shirt(frase= 'I love Python', tamanho= 'GG')

def make_shirt1(frase = 'i LOVE Python', tamanho = 'G'):
    """Função que pede o tamanho da camiseta e a frase que deseja como 
    estampa."""
    print(f'O tamanho da camiseta será {tamanho.upper()}.\n'
          f'A frase na estampa será: "{frase}\n"'
        )

make_shirt1(tamanho= 'M')
make_shirt1(frase= 'Hello Word!')
make_shirt1(tamanho= 'P', frase= 'Gosto muito da linguagem Python')

def describe_city(cidade, pais = 'Brasil'):
    print(f'{cidade} está em {pais}!\n')

describe_city('Rio de Janheiro')
describe_city('São Paulo')
describe_city(cidade= 'Medellín', pais= 'Colombia')

