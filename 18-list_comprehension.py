# 1 - Listanto valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de Filmes
movieList = ["Matrix", "O Poderoso Chefão", "Interestelar", "Parasita"]

# 2 - Filmes que possuem a leta 'e' no Título
moviesWithE = [movie for movie in movieList if 'e' in movie.lower()]
print(moviesWithE)

# 3 - Filmes que eu assisti
moviesWatched = [movie for movie in movieList if movie != "Parasita" ]
print(moviesWatched)

# 4 - Encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme que deseja encontrar (ou 'sair' para encerrar):\n")
    if searchName.lower() == 'sair':
        print("Programa encerrado")
        break
    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {searchName}:")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme encontrado com o nome: {searchName}. Tente novamente.!")