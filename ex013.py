'''Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Qual o salario do funcionário? R$ '))
desconto = salario - salario*(0.15)
print(
    f'Um funcionário que ganhava com R${salario}, com 15% de desconto, passa a receber R${desconto}')
