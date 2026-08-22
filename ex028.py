from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('PROCESSANDO...')
sleep(3)
print('-=-'*20)
pc = randint(0, 5)
num = int(input('Em que número pensei? '))
if num == pc:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {num}')
