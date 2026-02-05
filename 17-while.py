# Lista de Filmes
movieList = ["Matrix", "O Poderoso Chefão", "Interestelar", "Parasita"]

# 1 - Interando valores de uma lista de filmes usando while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1
    
# 2 - Quando a condição for atendida, o loop será interrompido
index = 0
while index < len(movieList):
    if movieList[index] == "O Poderoso Chefão":
        break
    print(movieList[index])
    index += 1
    
# 3 - Quando a condição for atendida, o Loop pula para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "O Poderoso Chefão":
        index += 1
        continue
    print(movieList[index])
    index += 1
    
# 4 - Avaliação do Filme com While
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
count = 0


while count < movieRating:
    note = float(input(f"Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0
print(f"A média das avaliações para o filme '{movieName}' é: {average:.2f}")