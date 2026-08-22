'''Exercício Python 006: Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.'''

num = int(input('Digite um número: '))
print(f'O dobre de {num} é {num*2}')
print(f'O triplo de {num} é {num*3}')
print(f'A raiz de {num} é {num**(1/2):.2f}')
