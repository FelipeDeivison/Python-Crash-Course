class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, numbr_served=0,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbr_served = numbr_served

    def describe_restaurant(self):
        print(f'Ontem fui para o restaurante {self.restaurant_name}')
        print(f'Lá fazem a melhor comida {self.cuisine_type}')

    def open_restaurant(self):
        print('Restaurante Aberto!')
    
    def number_served(self):
        print(f'Número de clientes atendidos hoje: {self.numbr_served}')

    def increment_number_servet(self, numbr_served):
        self.numbr_served = numbr_served
        print(f'Número de clientes atendidos hoje: {self.numbr_served}')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, numbr_served=0):
        super().__init__(restaurant_name, cuisine_type, numbr_served)
        self.flovors = ['Leite', 'chocolate', 'flocos',]
    def sabores_sorvetes(self,):
        print(
            f'Sabores de Sorvetes disponiveis:\n'
            f'{self.flovors}'
            )

if __name__ == "__main__":

    restaurant = Restaurant('Japa do Fê', 'Japônesa')

    restaurant.open_restaurant()

    restaurant.describe_restaurant()

    restaurant.numbr_served = 10
    restaurant.number_served()

    restaurant.increment_number_servet(12)

    print()

    sorveteria = IceCreamStand('Doce Gelado', 'Sorveteria')

    sorveteria.sabores_sorvetes()
