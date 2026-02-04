filmInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Adventure", "Comedy", "Horror"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recuperar um elemento do dicionário
print(filmInception["genre"])
print(filmInception.get("imbRating"))

# 2 - Buscar as chaves do dicionário
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionário
print(filmInception.values())

# 4 - Buscar itens do dicionário com (chave, valor)
print(filmInception.items())

# 5 - Adicionar itens ao dicionário
filmInception["director"] = "Christopher Nolan" 
print(filmInception)

#  6 - Atulizar itens no dicionário
filmInception.update({"imbRating": 9.0})
print(filmInception)

# 7 - Remover itens do dicionário
filmInception.pop("director")
print(filmInception)