class User:
    def __init__(self, first_name, last_name, age, location,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(
            f'Informações do Usuário:\n'
            f'Nome: {self.first_name}\n'
            f'Sobrenome: {self.last_name}\n'
            f'Idade: {self.age} Anos    Cidade: {self.location}'
            )

    def greet_usr(self):
        print(f'Olá {self.first_name} {self.last_name}, seja Bem-Vindo!')

    
user = User('Felipe', 'Angelo', '23', 'São Paulo')

user.describe_user()
user.greet_usr()
    
        