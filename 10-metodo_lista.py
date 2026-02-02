filmsList = ["Inception", "The Dark Knight", "Interstellar", "Dunkirk", "Star Wars", "The Godfather"]

# 1- Tamanho da lista
print(len(filmsList))

# 2- Recuperar um item da lista pelo índice
print(filmsList.index("Dunkirk"))

# 3- Adicionar um item ao final da lista
filmsList.append("Pulp Fiction")
print(filmsList)

#  4 - Ordenar a Lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de Lista para outra
filmsCopy = filmsList.copy()
print(filmsCopy)

filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

#  6 - Remover todos os itens da lista
filmsList.clear()
print(filmsList)