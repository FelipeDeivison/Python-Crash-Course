class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Ontem fui para o restaurante {self.restaurant_name}')
        print(f'Lá fazem a melhor comida {self.cuisine_type}')

    def open_restaurant(self):
        print('Restaurante Aberto!')

restaurant = Restaurant('Japa do Fê', 'Japônesa')

restaurant.open_restaurant()

restaurant.describe_restaurant()