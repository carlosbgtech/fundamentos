# Lista de Filmes
movieList = ["Matrix", "O Poderoso Chefão", "Interestelar", "Parasita", "A Origem"]

# 1 - Interando valores de uma lista
for movie in movieList:
    print("Filme:", movie)
    
#  2 - Quando a condição for atendida, interrompe o loop
for movie in movieList:
    if movie == "O Poderoso Chefão":
        break
    print( movie)
    
# 3 - Quando a condição for atendida, pula para a próxima iteração
for movie in movieList:
    if movie == "O Poderoso Chefão":
        continue
    print( movie)
    
#  4 - Avaliação do Filme:
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite a avaliação do filme (1-5):\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    
if movieRating > 0:
    average = total / movieRating
else:
    average = 0
print(f"A média das avaliações para o filme '{movieName}' é: {average:.2f}")