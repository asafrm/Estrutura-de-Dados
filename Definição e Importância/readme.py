#sem usar nenhuma estrutura de dados:
#lista de alunos e suas notas
nome1 = "João"
nota1 = 8.5
nome2 = "Maria"
nota2 = 9.0
nome3 = "Pedro"
nota3 = 7.0

soma_notas = nota1 + nota2 + nota3

# Calculo da media
media = soma_notas / 3

print(f"A média das notas é: {media}")

#Aqui podemos observar que as informações dos alunos estão desorganizadas. Se for preciso colocar mais alunos
#teríamos que criar novas variáveis e modificar partes do código, assim ficando mais complexo e propenso a erros.


#usando uma estrutura de dados:

alunos = [
    {"nome": "João", "nota": 8.5},
    {"nome": "Maria", "nota": 9.0},
    {"nome": "Pedro", "nota": 7.0}
]

soma_notas = sum(aluno["nota"] for aluno in alunos)

# Calculo da média
media = soma_notas / len(alunos)

print(f"A média das notas é: {media}")

#Observa-se que com o uso de uma lista de dicionários, o código está mais organizado.
#Se quisermos adicionar mais alunos, basta adicionar um novo dicionário à lista sem a necessidade de criar novas variáveis.