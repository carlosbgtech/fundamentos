"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter na nossa função.
- Os argumentos são passados como uma tupla
**kwargs - Além dos valores passados como argumentos, também passamos o nome do argumento, ou seja, a chave e o valor.
- Os argumentos são passados como um dicionário
"""
# 1 - Soma de números utilizando *args
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7, 9)
sum(7, 9, 10, 11)
sum(7, 9, 10, 11, 12)

# 2 - Apresentação de Curso utilizando **kwargs
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de cursos:")

presentation(name = "Python", category = "Backend", Level = "Inciante")
presentation(name = "Visão Computacional com Python", category = "IA", Level = "Avançado")
presentation(name = "Dashboards com Dash", category = "Data Science", Level = "Intermediário")