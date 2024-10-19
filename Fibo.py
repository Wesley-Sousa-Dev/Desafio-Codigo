def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

cont = 1
num = int(input("Numero que deseja encontrar: "))
while(num > fibonacci(cont)):
    cont += 1

resultado_proximo = fibonacci(cont)

if(resultado_proximo == num or num == 0):
    print(f"O numero {num} pertence à sequência de Fibonacci")
else:
    print(f"O numero {num} não pertence à sequência de Fibonacci, o numero mais proximo é {resultado_proximo}")