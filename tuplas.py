buffets = ('Café da manhã', 'Almoço balanceado', 'Lanchinho da tarde', 'Jantar leve', 'Ceia leve')
for buffet in buffets:
    print(buffet)
#Tuplas não podem ser modificadas, segue exemplo:

#buffets[3] =  ('jantar')
#print(buffets)

#Porém elas podem ser substituidas
buffets = ('Café da manhã', 'Almoço balanceado', 'Lanchinho da tarde', 'Jantar', 'Merenda da noite')
for buffet in buffets:
    print(buffet)