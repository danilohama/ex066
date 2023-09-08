"""Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar ova-
lor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (des-
considerando o flag)
"""
from time import sleep

num = soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para Parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
sleep(2)
print(f'A soma dos {cont} valores foi {soma}!')
