# Problema 1013 - O Maior (Beecrowd)
# Calcula o maior entre três números usando a fórmula dada

# Leitura dos valores inteiros
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

# Função para calcular o maior entre dois valores usando a fórmula dada
def maior(x, y):
    return int((x + y + abs(x - y)) / 2)

# Calcula o maior entre a e b, depois compara com c
maior_ab = maior(a, b)
maior_abc = maior(maior_ab, c)

# Exibe o resultado no formato solicitado
print(f"{maior_abc} eh o maior") 