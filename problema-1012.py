# Problema 1012 - Área (Beecrowd)
# Calcula diversas áreas geométricas a partir de três valores

# Leitura dos valores A, B, C
entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

# Definição de PI
PI = 3.14159

# Cálculos
area_triangulo = (A * C) / 2
area_circulo = PI * C ** 2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

# Exibição dos resultados formatados
print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")
# Este programa lê três valores reais (A, B, C) e calcula as áreas de um triângulo, círculo, trapézio, quadrado e retângulo,
# exibindo os resultados com três casas decimais. A constante PI é definida como 3.14159.
# A fórmula para cada área é aplicada corretamente, e os resultados são formatados para exibição. 