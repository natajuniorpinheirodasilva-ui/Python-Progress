# Esse código foi feito com base no enunciado abaixo:
# 
# Desenvolva um programa em Python que solicite ao usuário uma quantidade de números inteiros e, 
# após receber todas as entradas, realize uma análise completa sobre esses números. O programa deve
# identificar quais números são múltiplos de 2 e quais são múltiplos de 3, armazenando-os em estruturas
# de dados apropriadas. Para cada categoria de múltiplos (múltiplos de 2, múltiplos de 3 e múltiplos de ambos),
# o programa deve exibir a quantidade de elementos, seus respectivos valores com as posições, o maior e menor
# valor da categoria e a soma total. Além disso, o programa deve calcular e exibir a média aritmética de todos
# os números fornecidos e indicar quais números não são múltiplos nem de 2 nem de 3. O programa não deve aceitar
# o zero como entrada válida e deve tratar possíveis erros de entrada de dados, permitindo que o usuário reinicie
# o programa ao final da execução.

import time
import os
while True:
    try:
        
        a = int(input('Forneça a quantia de loops: '))
        
        if a <= 0:
            print('Deve ser maior que 0')
            continue
        
        num = []
        m2 = []
        m3 = []
        m2_e_m3 = []
        m2m3 = 0
        c2 = 0
        c3 = 0

        for i in range(a):
            while True:
                numero = int(input(f"Forneça o {i + 1}° número: "))
                if numero == 0:
                    print('Zero não é permitido. Digite outro número.\n')
                else:
                    num.append(numero)
                    break
            
            if num[i] % 2 == 0:
                m2.append(num[i])
                c2 += 1
                print(f'{num[i]} é múltiplo de 2.\n')
            
            if num[i] % 3 == 0:
                m3.append(num[i])
                c3 += 1
                print(f'{num[i]} é múltiplo de 3.\n')
            
            if (num[i] % 2 == 0 and num[i] % 3 == 0):
                m2_e_m3.append(num[i])
                m2m3 += 1
             
            if num[i] % 2 != 0 and num[i] % 3 != 0:
                print(f'{num[i]} não é múltiplo de 2, nem de 3\n')
        time.sleep(2)
        
        os.system('cls')
        media = sum(num) / a
        print(f'Os números fornecidos foram: {", ".join(map(str, num))}')

        print(f'A média deles é de: {media}\n')
        while i != 'chupa':
            continuar = input('Digite Y para continuar: ').lower().strip()
            if continuar in ('y', 'yes'):
                break
            else:
                continue
        os.system('cls')
        
        if c2 >= 1:
            print(f'Há {c2} múltiplo(s) de 2. Sendo ele(s): ')
            
            for i in range(c2):
                print(f'{m2[i]} na posição {i+1}')
            soma2 = sum(m2)
            maior2 = max(m2)
            menor2 = min(m2)
            print(f'O maior número múltiplo de 2 é: {maior2}. E o menor: {menor2}')
            if c2>= 2:
                print(f'A soma dos múltiplo(s) de 2 é: {soma2}')
            else:
                print(f'Não há mais de um número para somar. Valor final: {soma2}')
        else:
            print('\nNão há múltiplos de 2.')

        if c3 >= 1:
            print(f'\nHá {c3} múltiplo(s) de 3. Sendo ele(s): ')
            
            for i in range(c3):
                print(f'{m3[i]} na posição {i+1}')
            soma3 = sum(m3)
            maior3 = max(m3)
            menor3 = min(m3)
            print(f'O maior número múltiplo de 3 é: {maior3}. E o menor: {menor3}')
            if c3 >= 2:
                print(f'A soma dos múltiplo(s) de 3 é: {soma3}')
            else:
                print(f'Não há mais de um número para somar. Valor final: {soma3}')
        else:
            print('\nNão há múltiplos de 3.')
        
        if m2m3 >= 1:
            print(f'\nHá {m2m3} múltiplo(s) de 2 e 3. Sendo ele(s): ')
            for i in range(m2m3):
                print(f'{m2_e_m3[i]} na posição {i+1}')
            soma2_3 = sum(m2_e_m3)
            maior2_3 = max(m2_e_m3)
            menor2_3 = min(m2_e_m3)
            print(f'O maior número múltiplo de 2 e 3 é: {maior2_3}. E o menor: {menor2_3}')
            if m2m3 >= 2:
                print(f'A soma dos múltiplos de 2 e 3 é: {soma2_3}')
            else:
                print(f'Não há mais de um número para somar. Valor final: {soma2_3}')
        else:
            print('\nNão há múltiplos de 2 e 3.')

        break
    except ValueError:
        print('Erro de valor. Resetando o código em 3s')
        print('3s')
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('Resetando...\n')
        time.sleep(1.5)
        continue