def fibonacci():
    a = 1
    b = 0
    while a < 144:
        soma = a + b
        a = b
        b = soma
        print(b)
fibonacci()