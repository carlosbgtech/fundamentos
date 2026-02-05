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