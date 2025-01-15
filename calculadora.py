nome = input('Qual e o seu nome? \n')
print('Bem vindo a calculadora', nome)

num1 = 0
num2 = 0
resultado = 0

print('Digite 2 numeros que deseja calcular')
num1 = int(input('Digite o primeiro numero\n'))
num2 = int(input('Digite o segundo numero\n'))

print('Qual a operacao que deseja fazer?')
print('1. Soma')
print('2. Subtracao')
print('3. Divisao')
print('4. Multiplicacao')
print('5. Potenciacao')

calculo = input()

if calculo == '1':
	resultado = num1 + num2
	print('O resultado da soma e', resultado)
elif calculo == '2':
	resultado = num1 - num2
	print('O resultado da subtracao e', resultado)
elif calculo == '3':
	resultado = float(num1) / float(num2)
	print('O resultado da divisao e', resultado)
elif calculo == '4':
	resultado = num1 * num2
	print('O resultado da multiplicacao e', resultado)
elif calculo == '5':
	resultado = num1 ** num2
	print('O resultado da potenciacao e', resultado)
else:
	print('Digite um valor valido para podermos continuar')
