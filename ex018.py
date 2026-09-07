'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''


from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem COSSENO de {cosseno:.2f}')
tangete = tan(radians(angulo))
print(f'O ângulo de {angulo} tem COSSENO de {tangete:.2f}')
