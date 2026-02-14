niles = {
    'Nilo': 'Egito',
    'Amazonas': 'Brasil',
    'Yangtzé': 'China',
}
print('Os três principais rios do mundo, em termos de extensão, são:')

for nile in niles:
    if nile == 'Nilo':
        print(f'O Rio Nilo passa principalmente pelo Egito')
    elif nile == 'Amazonas':
        print('O Rio Amazonas que atravessa o Brasil.')
    else:
        print('O Rio Yangtzé que cruza a China.')

print('\nCada um é essencial para a vida e história dessas regiões.')

print('\nOs três rios são:\n')
for nile in niles.keys():
    print(nile)

print('\nOs paises que eles passam:\n')
for egypt in niles.values():
    print(egypt)

