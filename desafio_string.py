'''
1 — Ordenar Títulos
Desafio:

O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.

A lista de títulos é fornecida como uma string chamada “títulos”, onde cada título está em uma nova linha.

Segue exemplo de lista:

titulos = """O Senhor dos Anéis 
Harry Potter e a Pedra Filosofal 
O Lobo da Estepe 
Cem Anos de Solidão 
A Metamorfose 
A Revolução dos Bichos 
Crime e Castigo 
Macunaíma"
'''
titulo = ['O Senhor dos Anéis', 'Harry Potter e a Pedra Filosofal', 'O Lobo da Estepe','Cem Anos de Solidão','A Metamorfose','A Revolução dos Bichos','Crime e Castigo','Macunaíma']

titulo_ordenado = sorted(titulo)
print(titulo_ordenado)

'''Manpulando'''
# Consultando:
print(titulo[2])

#Consultando pela posição negativa:
print(titulo[-1])

#Adicionando um item a lista:
titulo_ordenado2 = titulo_ordenado.append('Alta Frequência')
titulo_ordenado2 = sorted(titulo_ordenado)
print(titulo_ordenado2)

#Removendo um item por posição:
del titulo_ordenado2[7]
print(titulo_ordenado2)

#Removendo um item pelo valor:
titulo_ordenado2.remove('A Metamorfose')
print(titulo_ordenado2)

#Removendo o último da iten da lista, porém sem excluílo, o armazenando em outra variável:
item = titulo_ordenado2.pop(-1)
print(titulo_ordenado2)
print(item)