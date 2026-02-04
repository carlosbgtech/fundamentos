import pprint

filmsDict = {
        "Inception": {
            "yearRelease": 2010,
            "imbRating": 8.8,
            "genre": ["Sci-fi", "Action", "Adventure", "Comedy", "Horror"]
        },
        "The Dark Knight": {
            "yearRelease": 2008,
            "imbRating": 9.0,
            "genre": ["Action", "Crime", "Drama"]
        },
        "The Godfather": {
            "yearRelease": 1972,
            "imbRating": 9.2,
            "genre": ["Crime", "Drama"]
        },
}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["Inception"]["genre"])

#  2 - Adicionar novo item ao dicionário aninhado
filmsDict["Inception"]["director"] = "Christopher Nolan"
print(filmsDict["Inception"])

#  3- Excluir um dicionário aninhado
del filmsDict["The Godfather"]
pp.pprint(filmsDict)