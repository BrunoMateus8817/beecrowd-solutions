# Problema 1011 - Esfera (Beecrowd)
# Calcula o volume de uma esfera dado o raio, exibindo com 3 casas decimais

# Leitura do raio
raio = float(input())

# Definição de PI
PI = 3.14159

# Cálculo do volume
volume = (4/3) * PI * (raio ** 3)

# Exibição do resultado formatado
print(f"VOLUME = {volume:.3f}") 