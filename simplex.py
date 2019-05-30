# -*- coding: utf-8 -*-

matrix_simplex = [
    ['z', 'x1', 'x2', 's1', 's2', 's3', 't'], # nome das variáveis
    [1, -3, -5, 0, 0, 0, 0], # função Z
    [0, 2, 4, 1, 0, 0, 10], # restrição 1
    [0, 6, 1, 0, 1, 0, 20], # restrição 2
    [0, 1, -1, 0, 0, 1, 30] # restrição 3
                            # restrição N...
    ]

def condicao_parada():
    for i in matrix_simplex[1]:
        if i < 0:
            return False
    return True

while not condicao_parada():

    menor = matrix_simplex[1][0]
    coluna_pivo = 0

    for i in range(1, len(matrix_simplex[1])):
        if matrix_simplex[1][i] < menor:
            menor = matrix_simplex[1][i]
            coluna_pivo = i

    print('A coluna pivo é a de: ' + matrix_simplex[0][coluna_pivo])
    menor_div = 0
    linha_pivo = 0
    for i in range(2, len(matrix_simplex)):
        current_div = matrix_simplex[i][len(matrix_simplex[1])-1] / float(matrix_simplex[i][coluna_pivo])

        if i == 2:
            linha_pivo = i
            menor_div = current_div
        elif current_div > 0 and current_div <= menor_div:
            menor_div = current_div
            linha_pivo = i

    print('A linha pivo é: ' + str(linha_pivo))
    elem_pivo = matrix_simplex[linha_pivo][coluna_pivo]
    print('O elemento pivo é: ' + str(elem_pivo))


    for i in range(0, len(matrix_simplex[linha_pivo])):
        matrix_simplex[linha_pivo][i] = matrix_simplex[linha_pivo][i] / float(elem_pivo)


    for linha in range(1, len(matrix_simplex)):
        if linha == linha_pivo:
            continue
        elem_pivo_atual = -matrix_simplex[linha][coluna_pivo]
        for col in range(0, len(matrix_simplex[linha])):
            matrix_simplex[linha][col] = (elem_pivo_atual * matrix_simplex[linha_pivo][col]) + matrix_simplex[linha][col]

    print('nova matrix: ' + str(matrix_simplex)) 

