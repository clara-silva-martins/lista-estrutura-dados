#Primeira função: Adicionar itens em uma lista

entrada = []
numeros = ((input('Digite um número de 1 a 30')).split())

def adicionar_numeros():
    entrada.extend(map(int,numeros))
    return entrada

minha_lista = adicionar_numeros()

print("Valores armazenados", minha_lista)

#Segunda função: Verificar se um item está na lista

numero_verificar = int(input('Digite um número de 1 a 30 e verifique se ele está na lista'))

def procurar_numero(num):
    if numero_verificar in minha_lista:
        return print('O número está na lista')
    else:
        return print('O número não está na lista')

procurar_numero(numero_verificar)

#Tericeira função: Ordenar de forma crescente e decrescente

ler = (input('Você deseja ordenar a lista de qual maneira? Digite crescente ou decrescente'))

def verificar_ordem():
    if ler == 'crescente':
        return sorted(minha_lista, key=int)
    else:
        return sorted(minha_lista, key=int, reverse=True)

lista_ordenada = verificar_ordem()

print("Lista ordenada: ", lista_ordenada)








