designs = ['phone case', 'robot pendant', 'dodecahedron',]
designs_concluidos = []

while designs:
    listra_desins = designs.pop(0)
    print(f'O modelo {listra_desins} está feito!\n')
    designs_concluidos.append(listra_desins)

    print('Modelos comcluídos:\n')
    for design_concluido in designs_concluidos:
        print(design_concluido)