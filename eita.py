#Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem:"Múltiplo de 10"

# import time

# def func():
#     a = 1
        
#     for a in range(1, 51):
#         if (a % 10 == 0):
#             print(f'{a} é Múltiplo de 10')
#         else:
#             print(a)
#         a += 1
# func()

# 37) Escreva um algoritmo que receba 10 números e exiba o maior deles e o menor deles.

# i = []
# b = 0

# for b in range(3):
#     i.append(float(input('Número: ')))
#     b += 1
# print(f'O maior valor foi: {max(i)}. O menor valor foi: {min(i)}')



# 38) Escreva um algoritmo que receba um número inteiro e calcule e exiba o seu fatorial.

# a = int(input(':'))
# b = 1
# while a > 0:
#     b *= a
#     a -= 1
# print(b)

# 39) Escreva um algoritmo que receba um número inteiro e exiba se esse número é ou não primo.

# while True:
#     a = int(input('Forneça o número: '))
#     primo = True

#     for i in range(2, a-1):
#         if a % i == 0:
#             primo = False
#             break
#     if primo == False:
#         print('Não é primo')
#     else:
#         print('É primo')
    
#     while True:
#         resposta = input('Quer testar outro? S e N: ').lower().strip()
#         if resposta == 's' or resposta == 'sim':
#             print('Perfeito. Código resetado.\n')
#             break
#         elif resposta == 'n' or resposta == 'não':
#             print('Perfeito. Adeus!')
#             break
#         else:
#             print('Forneça apenas S/Sim ou N/Não: ')
#             continue
#     if resposta == 's' or resposta == 'sim':
#         continue
#     else:
#         break

# 40) Faça um algoritmo que leia 100 números inteiros e, informe, quantos e quais deles são pares.

# a = []
# b = 3

# while b > 0:
#     a.append(float(input(f'Forneça o {b}° número: ')))
#     b -= 1
#     for num in a:
#         if num % 2 == 0:
#             print('Par')
#         else:
#             print('Impar')
# print(a)

# 46) Armazenar 50 números num arranjo e verificar se existem números iguais. A resposta deve

# num = []

# for i in range(5):
#     num.append(float(input(f'Forneça o {i+1}° número: ')))

# b = False

# for i in range(5):
#     for j in range(i + 1, 5):
#         if num[i] == num[j]:
#             b = True
# print(b)

# 47) Crie um algoritmo que armazene 10 números inteiros num vetor. Depois mostre:

# num = []
# final = 0
# media = 0

# for i in range(10):
#     num.append(float(input(f"Forneça o {i+1}° número: ")))
#     final += num[i]
# media = final / 10
# print(f'Média = {media:.1f}, Valor final = {final}')

# 48) Faça um algoritmo que leia 15 números reais e armazene-os num vetor.
# Depois o programa deve mostrar:
# O maior número digitado
# A posição (índice começando em 1) onde esse maior número se encontra
# O menor número digitado
# A posição (índice começando em 1) onde esse menor número se encontra

# num = []
# i = 0

# while i < 3:
#     num.append(float(input(f"Forneça o {i+1}° número: ")))
#     i += 1

# maior = num[0]
# menor = num[0]
# posme = 1
# posma = 1

# for i in range(3):
#     if (num[i] >= maior):
#         maior = num[i]
#         posma = i + 1
#     if (num[i] <= menor):
#         menor = num[i]
#         posme = i + 1
# print("-"*60)
# print(f"O maior número é {maior}. O maior está na posição {posma}")
# print("-"*60)
# print(f"O menor é {menor}. O menor está na posição {posme}.")
# print("-"*60)

# 48) Dada uma relação de 1000 números em graus Célsius, faça um algoritmo que imprima o seguinte relatório: Graus Fahrenheit Graus Célsius t f t c t f t c

# c = []
# f = []
# i = 0

# while i < 4:
#     c.append(float(input(f'Forneça o {i + 1}° grau c°: ')))
#     f.append((c[i] * 9/5) + 32)
#     i += 1
# for i in range(4):
#     print("Graus F°: ",f[i],"Graus C°: ", c[i])

# 49) Faça um algoritmo que receba duas notas de 6 alunos e calcule e imprima:
# a) a média entre essas 2 notas de cada aluno;
# b) a mensagem de acordo com a tabela abaixo;
# c) o total de alunos aprovados e o total de alunos reprovados.
#  Média Mensagem
# 0 ≤ média < 5 Reprovado
# 5 ≤ média < 7 Exame
# 7 ≤ média ≤ 10 Aprovado 

# i = 0
# p1 = []
# p2 = []
# mf = []
# r = 0
# e = 0
# a = 0
# for i in range(5):
#     p1.append(float(input("Forneça a p1: ")))
#     p2.append(float(input("Forneça a p2: ")))
#     mf.append((p1[i] + p2[i]) / 2)
#     if 0 <= mf[i] < 5:
#         r += 1
#     elif 5 <= mf[i] < 7:
#         e += 1
#     elif 7 <= mf[i] <= 10:
#         a += 1
# for i in range(1):
#     print(f"Total de alunos aprovados: {a}", f"Total de alunos reprovados: {r}", f"Total de alunos em exame: {e}")

import math

def exibir_menu():
    print("\n" + "="*50)
    print("   MOVIMENTO UNIFORMEMENTE VARIADO (MUV)")
    print("="*50)
    print("Fórmulas disponíveis:")
    print("  [1] Velocidade final        → v = v₀ + a·t")
    print("  [2] Posição final           → s = s₀ + v₀·t + ½·a·t²")
    print("  [3] Equação de Torricelli   → v² = v₀² + 2·a·Δs")
    print("  [4] Calcular tudo (completo)")
    print("  [0] Sair")
    print("="*50)

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  ⚠ Valor inválido! Digite um número (ex: 9.8 ou -3).")

def calcular_velocidade_final():
    print("\n📐 Velocidade Final: v = v₀ + a·t")
    v0 = ler_float("  Velocidade inicial v₀ (m/s): ")
    a  = ler_float("  Aceleração a (m/s²): ")
    t  = ler_float("  Tempo t (s): ")

    v = v0 + a * t

    print(f"\n✅ Resultado:")
    print(f"  Velocidade final v = {v:.4f} m/s")

def calcular_posicao():
    print("\n📐 Posição Final: s = s₀ + v₀·t + ½·a·t²")
    s0 = ler_float("  Posição inicial s₀ (m): ")
    v0 = ler_float("  Velocidade inicial v₀ (m/s): ")
    a  = ler_float("  Aceleração a (m/s²): ")
    t  = ler_float("  Tempo t (s): ")

    s = s0 + v0 * t + 0.5 * a * t**2

    print(f"\n✅ Resultado:")
    print(f"  Posição final s = {s:.4f} m")

def calcular_torricelli():
    print("\n📐 Equação de Torricelli: v² = v₀² + 2·a·Δs")
    v0       = ler_float("  Velocidade inicial v₀ (m/s): ")
    a        = ler_float("  Aceleração a (m/s²): ")
    delta_s  = ler_float("  Deslocamento Δs (m): ")

    v2 = v0**2 + 2 * a * delta_s

    print(f"\n✅ Resultado:")
    if v2 < 0:
        print(f"  v² = {v2:.4f} → Velocidade final imaginária (o objeto não alcança esse ponto).")
    else:
        v = math.sqrt(v2)
        print(f"  v² = {v2:.4f} m²/s²")
        print(f"  Velocidade final v = ±{v:.4f} m/s")

def calcular_completo():
    print("\n📐 Cálculo Completo do MUV")
    s0 = ler_float("  Posição inicial s₀ (m): ")
    v0 = ler_float("  Velocidade inicial v₀ (m/s): ")
    a  = ler_float("  Aceleração a (m/s²): ")
    t  = ler_float("  Tempo t (s): ")

    v       = v0 + a * t
    s       = s0 + v0 * t + 0.5 * a * t**2
    delta_s = s - s0
    v2      = v0**2 + 2 * a * delta_s

    print(f"\n✅ Resultados:")
    print(f"  {'Velocidade final (v):':<30} {v:.4f} m/s")
    print(f"  {'Posição final (s):':<30} {s:.4f} m")
    print(f"  {'Deslocamento (Δs):':<30} {delta_s:.4f} m")
    print(f"  {'v² (Torricelli):':<30} {v2:.4f} m²/s²")

    # Tipo de movimento
    print(f"\n🔍 Análise do movimento:")
    if a == 0:
        print("  → Aceleração nula: Movimento Uniforme (MU).")
    elif (v0 >= 0 and a > 0) or (v0 <= 0 and a < 0):
        print("  → Movimento Acelerado (v₀ e a têm o mesmo sentido).")
    else:
        print("  → Movimento Retardado (v₀ e a têm sentidos opostos).")
        if a != 0:
            t_parada = -v0 / a
            if t_parada > 0:
                print(f"  → O objeto para em t = {t_parada:.4f} s.")

def main():
    print("\nBem-vindo ao calculador de MUV!")

    opcoes = {
        "1": calcular_velocidade_final,
        "2": calcular_posicao,
        "3": calcular_torricelli,
        "4": calcular_completo,
    }

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("\nEncerrando... Até logo! 👋\n")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("  ⚠ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()