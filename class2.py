#Importando o modúlo do arquivo "class0.py"

import class0


japa = class0.Restaurant('kami', 'japonesa')
japa.describe_restaurant()

#importando somemte um classe do modúlo "class0.py"

from class0 import Restaurant

japa2 = Restaurant('kami 2', 'japonesa', 103)
japa2.describe_restaurant()
japa2.open_restaurant()
japa2.number_served()