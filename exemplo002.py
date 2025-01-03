##Inteiros (int)
##Escreva um programa que soma dois números inteiros inseridos pelo usuário.
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

resultado = a + b

print(resultado)
##Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
a = int(input("Digite um numero: "))

resultado = (a / 5)
print(resultado)
##Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

resultado = a * b

print(resultado)
#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

resultado = a / b

print(resultado)

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.#
a = int(input("Digite um numero: "))

quadrado = a ** 2
print(quadrado)

#Números de Ponto Flutuante (float)
#Escreva um programa que receba dois números flutuantes e realize sua adição.
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))

soma = a + b

print(soma)
#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))

soma = (a + b) /2

print(soma)
#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
a = float(input("Digite um base: "))
b = float(input("Digite um expoente: "))

soma = a ** b

print(soma)
#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite uma temperatura: "))

fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite um raio: "))

area = 3.14 * (raio ** 2)

print(area)

#Strings (str)
#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

a = (input("Digite seu nome:"))

nome = a.upper()

print(nome)
#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
a = (input("Digite seu nome:"))

nome = a.lower()

print(nome)
#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
a = (input("Digite seu nome:"))

nome = a.strip()

print(nome)
#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato 'dd/mm/aaaa': ")

dia, mes, ano = data.split('/')
print(dia)
print(mes)
print(ano)

#Escreva um programa que concatene duas strings fornecidas pelo usuário.
a = str(input("Digite um nome: "))
b = str(input("Digite um nome: "))

resultado = a + b

print(resultado)
#Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
verdadeiro = True
falso = False

print(verdadeiro and verdadeiro)
print(falso and verdadeiro)

#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

a = input("Digite o primeiro valor booleano (True/False): ").strip().capitalize()
b = input("Digite o segundo valor booleano (True/False): ").strip().capitalize()

bool1 = a == 'True'
bool2 = b == 'True'

resultado = bool1 or bool2

print(resultado)
#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

a = input("Digite o primeiro valor booleano (True/False): ").strip().capitalize()
b = input("Digite o segundo valor booleano (True/False): ").strip().capitalize()

bool1 = a == 'True'
bool2 = b == 'True'

resultado = bool1 or bool2

print(not resultado)

#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

a = input("Digite um numero de 1 a 5 ").strip()
b = input("Digite um numero de 1 a 5  ").strip()

if a == b:
    print('São iguais')
else:
    print('São diferentes')


