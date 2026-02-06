# 1 - Função de potência de um número
power = lambda num: num ** 2

# 2 - Função que verifica se um número é par
is_even = lambda x: x % 2 == 0

# 3 - Função que divide um número por outro
div_num = lambda x, y: x / y

# 4 - Função que inverte uma string
reverse_string = lambda s: s[::-1]

print(power(5))  # Saída: 25
print(power(9))  # Saída: 81
print(is_even(27))  # Saída: False
print(is_even(30))  # Saída: True
print(div_num(10, 2))  # Saída: 5.0
print(div_num(6, 2))  # Saída: 3.0
print(reverse_string("Python"))  # Saída: nohtyP
print(reverse_string("JavaScript"))  # Saída: tpircSavaJ

# 5 - Funcionalidades relacionadas aos filmes:
movies_list = ["Inception", "The Dark Knight", "Interstellar", "Dunkirk", "Star Wars", "The Godfather"]
ratings = {
    "Inception": [8.5, 9.0, 7.5],
    "The Dark Knight": [9.0, 9.5, 8.5],
    "Interstellar": [8.0, 8.5, 9.0],
    "Dunkirk": [7.5, 8.0, 7.0],
    "Star Wars": [8.0, 8.5, 9.0],
    "The Godfather": [9.5, 9.0, 9.5],
}

# 6 - Função para calcular a média das avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

# 7 - Função para verificar se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list

# 8 - Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de avaliação {average_rating(movie_name):.2f}"

print(f"Média de Avaliação do filme Star Wars: {average_rating('Star Wars')}")  # Saída: Média de Avaliação do filme Star Wars: 8.5 
print(f"O filme 'Inception' está na lista? {check_movie('Inception')}")  # Saída: O filme 'Inception' está na lista? True
print(f"{recommend_movie('The Godfather')}")  # Saída: Recomendo assistir The Godfather com média de avaliação 9.33