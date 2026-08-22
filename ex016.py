'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo 
teclado e mostre na tela a sua porção Inteira.'''

'''valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e sua porção inteira {int(valor)}')'''


from math import trunc
valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e sua porção inteira {trunc(valor)}')
