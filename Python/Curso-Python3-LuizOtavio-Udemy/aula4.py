#Tipos de dados em Python
#int = numeros inteiros
print(11-1) # int = 10

#float = numeros com ponto flutuante
print(10.9)

print(type('letras'))

print(10 == 10) # Sim  => True, verdadeiro
print(10 == 11) #Não => False, falso

print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))


#convertendo tipos

print(int('1'), type(int('1'))) #convertendo um str em int
print(type(float('1')+1)) #convertendo um str em float e somando mais 1
print(bool(' ')) #convertendo um str vazio em bool
print(str(11) + 'b') #convertendo pra str em somando b

# aula 7
# variáveis

nome_completo = 'Vitor Hugo Marçal Pereira'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade, 'é maior?', maior_de_idade)