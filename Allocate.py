#!/bin/env python3
import tomllib

#! Definições de Funções
def Cont(Data):
    nonAlocated = 0

    for Names in Data:
        if (Data[Names]['Alocation'] == 0):
            nonAlocated = nonAlocated + 1

    return nonAlocated

#! Inicio do Programa

with open("3Tri/3Tri.toml", 'rb') as File:
    inData = tomllib.load(File)

#! Define o Numero de Vagas
with open("config.toml", 'rb') as File:
    config = tomllib.load(File)


NumEletivas = config['Global']['Num_Eletivas']
Vagas       = config['Global']['Vagas']

print(f'{NumEletivas}\t{Vagas}')
print(Cont(inData))

Aloc = NumEletivas*[Vagas]
print(f'{Cont(inData)}: {Aloc}')

#while (Cont(inData) != 0):
while (Cont(inData) > 0):
    for Eletiva in range(NumEletivas):
        for Serie in range(3, 0, -1):
            for Rank in range(1, 6):
                for Names in inData:
                    if inData[Names]['Serie'] == Serie and inData[Names]['Escolhas'][Eletiva] == Rank and Aloc[Eletiva]:
                        if inData[Names]['Alocation'] == 0: 
                            inData[Names]['Alocation'] = Eletiva + 1
                            Aloc[Eletiva] = Aloc[Eletiva] - 1
                            print(f"{Cont(inData):03}: {Aloc}")


for Eletiva in range(NumEletivas):
    i = 1
    with open('Eletiva_' + f'{Eletiva+1:02}.txt', 'w') as File:
        for Names in inData:
            if (inData[Names]['Alocation'] == Eletiva + 1):
                File.write(f'{i}\t{inData[Names]['Escolhas'][Eletiva]}\t{Names}\n')
                i = i + 1
