from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem COSSENO de {cosseno:.2f}')
tangete = tan(radians(angulo))
print(f'O ângulo de {angulo} tem COSSENO de {tangete:.2f}')
