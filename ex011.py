l = float(input('Largura de parede: '))
h = float(input('Altura de parede: '))
a = l*h
print(
    f'Sua parede tem dimensão de {l}x{h} e sua área é de {a}m².Para pintar essa parede, você precisará de {(l*h/2):.2f}l de tinta.')
