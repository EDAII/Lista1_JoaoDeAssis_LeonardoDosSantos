import numpy
import time
import os
import random
import math    
def simpleSearch(vector):
    print("Valores: " + str(vector))
    start_time = time.time()
    numSearch = str(input('Qual valor desejado? '))
    for i in range(len(vector)):
        if(numSearch == vector[i]):
            print('Valor encontrado!'+ '\n')
            elapsed_time = time.time() - start_time
            print('tempo gasto: ' + str(elapsed_time))
            return i
    elapsed_time = time.time() - start_time
    print('tempo gasto: ' + str(elapsed_time))

def binarySearch(vector):
    start_time = time.time()
    inf_limit = 0
    sup_limit = len(vector) - 1
    median = sup_limit/2
    median = math.floor(median)
    
    print("Valores: " + str(vector))
    numSearch = int(input('Qual valor desejado? '))

    for i in range(len(vector)):
        if (numSearch == vector[median]):
            print('Valor encontrado!' + '\n')
            elapsed_time = time.time() - start_time
            print('tempo gasto: ' + str(elapsed_time) + '\n' + 'Posição: ' + str(median))
            return median
        elif(numSearch < vector[i]):
            inf_limit = median + 1
            median = (inf_limit+1 + (sup_limit - median))/2
            print('Valor encontrado!' + '\n')
            elapsed_time = time.time() - start_time
            print('tempo gasto: ' + str(elapsed_time) + '\n' + 'Posição: ' + str(median))
            return i
        elif(vector[i] < numSearch):
            sup_limit = median - 1
            median = (median - 1) - (sup_limit - median)/2
            print('Valor encontrado' + '\n')
            elapsed_time = time.time() - start_time
            print('tempo gasto: ' + str(elapsed_time) + '\n' + 'Posição: ' + str(median))
            return i
        else:
            print('Valor não encontrado!')
            elapsed_time = time.time() - start_time
            print('tempo gasto: ' + str(elapsed_time))
    
def interpolationSearch(vector):
    start_time = time.time()
    sup_limit = vector[len(vector) - 1]
    inf_limit = vector[0]
    print("Valores: " + str(vector))
    numSearch = input('Qual valor desejado? ')

    median = inf_limit + (sup_limit - inf_limit) * ((numSearch - vector[0])/((vector[len(vector) - 1]) - vector[0]))
    
    if vector[median] == numSearch:
        elapsed_time = time.time() - start_time
        print('tempo gasto: ' + str(elapsed_time))
        return median
    else:
        print('Valor não encontrado!')
        return

def bubbleSort(vector):
    trade = True
    while trade == True:
        for i in range(len(vector) - 2):
            if(vector[i] > vector[i + 1]):
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux
        trade = False
            
def setRange(vector):
    iF = int(input('Defina a quantidade de elementos da lista: '))
    while len(vector) < iF:
          rnd = random.randint(0, iF - 1)
          if rnd in vector:
              continue
          else:
              vector += [rnd]
    return iF

vector = []
setRange(vector)

def menu():
    print("---------------------------------------")
    print("                MENU                   ")
    print("---------------------------------------")
    print("1 - Busca sequencial simples") # precisa ser ordenado pra dar certo
    print("2 - Busca sequencial binaria") # nao necessariamente
    print("3 - Busca sequencial interpolação") # nao necessariamente
    print("0 - Sair")
    print("---------------------------------------")
    opt = input("Digite uma Opção: ")
    return opt

opt = 0
while opt != '4':
    opt = menu()
    if opt == '1':
        bubbleSort(vector)
        simpleSearch(vector)
    elif opt == '2':
        binarySearch(vector)
    elif opt == '3':
        interpolationSearch(vector)
    elif opt == '0':
        print('\n' + 'Obrigado =)' + '\n' + 'Leonardo dos Santos' + '\n' + 'João de Assis')
        break
    else:
        print('Opção Invalida!')
        break
