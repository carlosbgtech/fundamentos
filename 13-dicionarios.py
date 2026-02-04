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