class User:
    def __init__(self, first_name, last_name, age, location, login_attempts=0,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(
            f'Informações do Usuário:\n'
            f'Nome: {self.first_name}\n'
            f'Sobrenome: {self.last_name}\n'
            f'Idade: {self.age} Anos    Cidade: {self.location}'
            )

    def greet_usr(self):
        print(f'Olá {self.first_name} {self.last_name}, seja Bem-Vindo!\n')

    def increment_login_attempts(self,):
        self.login_attempts += 1
        print(self.login_attempts)
    
    def reset_login_attempts(self,):
        self.login_attempts = 0
        print(self.login_attempts)
        

    
user = User('Felipe', 'Angelo', 23, 'São Paulo', login_attempts=25)

user.describe_user()
user.greet_usr()

user2 = User('Natiara', 'Angelo', 32, 'Bela Cruz')
user2.describe_user()
user2.greet_usr()
    

user.increment_login_attempts()

user.reset_login_attempts()

print(user.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name, age, location, login_attempts=0):
        super().__init__(first_name, last_name, age, location, login_attempts)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]
    
    def show_privileges(self):
        for number, privelege in enumerate(self.privileges, start=1):
            print(number, '-' ,privelege.title())

admin = Admin('Felipe', 'Angelo', 23, 'São Paulo',)
admin.show_privileges()