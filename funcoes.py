def greet_user():
    # Essa parte entre aspas triplas é chamada de docstring que explica
    # o que a função faz.

    """Exibe um simples comprimento"""
    print('Hello!')

greet_user()

def display_message():
    """Uma menssagem sobre o capítulo do livro ao qual estou estudando"""
    print('O capítulo que estou estudando é sobre funções')

display_message()

def favorite_book(bookname):
    """Livro Favorito do usuário"""
    print(f'Um dos meus livros favoritos é {bookname.title()}')

favorite_book('O pequeno príncipe')
