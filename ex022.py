'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
