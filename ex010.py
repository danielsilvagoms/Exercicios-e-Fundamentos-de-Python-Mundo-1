'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

din = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${din} você pode comprar US${din/5.08:.2f}')
