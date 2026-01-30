movieName = "Top Gun"

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
    muito consagrado na indústria
"""

print(movieName.upper())  # Deixa todas as letras maiúsculas    
print(movieName.lower())  # Deixa todas as letras minúsculas
print(movieName.capitalize())  # Deixa a primeira letra maiúscula
print(movieName.title())  # Deixa a primeira letra de cada palavra maiúscula
print(movieName.center(10, '-')) # Centraliza a string em um campo de 10 caracteres, preenchendo com '-' 
print(movieName.find("u")) # Retorna a posição de uma determinado caractere
print(movieName.find("o")) # Conta caracteres
print(movieName.replace("Top", "Matrix")) # Substitui um caractere por outro
print(movieDescription.split(',')) # Divide a string em uma lista, usando o caractere especificado como separador