# Problema 1005 - Média 1 (Beecrowd)
# Este programa lê duas notas, calcula a média ponderada e exibe com 5 casas decimais

# Lê as notas como ponto flutuante
A = float(input())
B = float(input())

# Calcula a média ponderada
MEDIA = (A * 3.5 + B * 7.5) / 11

# Exibe o resultado formatado com 5 casas decimais
print(f"MEDIA = {MEDIA:.5f}")
# A função `input()` é usada para ler as notas.
# A variável `MEDIA` armazena o resultado da média ponderada.
# O uso de `f-string` permite formatar a saída com precisão específica.
# O programa é útil para entender como calcular médias ponderadas e formatar a saída em Python