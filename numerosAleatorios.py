import random
import requests
import os

# Verifica se o arquivo existe, caso exista o arquivo é deletado
if os.path.exists("numerosAleatorios.csv"):
    os.remove("numerosAleatorios.csv")

# Cria um novo arquivo, gera 5 números aleatórios e os escreve no arquivo 

arquivo = open("numerosAleatorios.csv","a")
contador = 0
while contador != 5:
    contador = contador + 1
    arquivo.write(str(random.randint(0,100)))
    arquivo.write("\n")
arquivo.close()

# Acessa o arquivo, lê cada número, gera uma curiosidade no site numbersapi e as insere em uma lista

frases = []
arquivo = open("numerosAleatorios.csv","r+")
while True:
    numeroArquivo = arquivo.readline().rstrip("\n")
    if(numeroArquivo == '') : break
    linkCuriosidadeNumeros = "http://numbersapi.com/{}".format(numeroArquivo)
    curiosidadeNumero = requests.get(linkCuriosidadeNumeros)
    frase = curiosidadeNumero.text
    frases.append(frase)
arquivo.close()

# Deleta o arquivo original

os.remove("numerosAleatorios.csv")

# Cria um novo arquivo inserindo as curiosidades de cada número

arquivo = open("numerosAleatorios.csv","a")
for indice in frases:
    arquivo.write(indice)
    arquivo.write("\n")
arquivo.close()







