'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''


l = float(input('Largura de parede: '))
h = float(input('Altura de parede: '))
a = l*h
print(
    f'Sua parede tem dimensão de {l}x{h} e sua área é de {a}m².Para pintar essa parede, você precisará de {(l*h/2):.2f}l de tinta.')
