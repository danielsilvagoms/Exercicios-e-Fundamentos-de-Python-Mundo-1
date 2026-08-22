'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.2f} km')
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print(f'E o preço de sua passagem é R${preco:.2f}')
