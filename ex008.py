'''Exercício Python 8: Escreva um programa que leia um valor em metros 
e o exiba convertido em centímetros e milímetros.'''

metros = float(input('Uma distância em metros: '))
print(f'A medida de {metros}m corresponde a \n{metros/1000} km n{metros/100} hm \n{metros/10} dam \n{metros*10} \n{metros*100}cm \n{metros*1000}mm')
