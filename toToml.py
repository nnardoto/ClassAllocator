#!/bin/env python3
import unicodedata
import tomllib as toml


with open("3Tri/3Tri.csv") as File:
    FullData = File.readlines()
   
    toFile = {}
    j = 1
    for Lines in FullData[1:]:
        SplittedLine = Lines.replace('""', '0').replace('\n', '').split(',')
        Time        = SplittedLine[0].replace('"','')
        Name        = SplittedLine[1].replace('"','').upper().strip()
        Serie       = SplittedLine[2].replace('°', '').replace('M', ' ').replace('"', '').split()[0]
        Turma       = SplittedLine[2].replace('°', '').replace('M', ' ').replace('"', '').split()[1]
        Escolhas    = []
        for i in range(9):
            Escolhas.append(int(SplittedLine[3 + i].replace('"', '')))
    
        # REMOVE ACENTOS DOS NOMES
        Name = unicodedata.normalize('NFKD', Name).encode('ASCII', 'ignore').decode('ASCII')

        # Write toml file    
        toFile[f'{Name}'] = {"Serie": f"{Serie}", "Turma": f"{Turma}", "Escolhas": f"{Escolhas}", "Time": f'{Time}', "Alocation": 0}


with open("3Tri/3Tri.toml", 'w') as File:
    for Names in toFile:
        File.write(f"['{Names}']\n")
        File.write(f"\tSerie\t=\t{toFile[Names]['Serie']}\n")
        File.write(f"\tTurma\t=\t{toFile[Names]['Turma']}\n")
        File.write(f"\tEscolhas\t=\t{toFile[Names]['Escolhas']}\n")
        File.write(f"\tAlocation\t=\t0\n")
        File.write(f"\tHora\t=\t'{toFile[Names]['Time']}'\n")
        File.write('\n')

