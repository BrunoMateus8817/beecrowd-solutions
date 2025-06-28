# Problema 1006 - Média 2 (Beecrowd)
# Este programa lê três notas, calcula a média ponderada e exibe com 1 casa decimal

# Leitura das notas
A = float(input())
B = float(input())
C = float(input())

# Cálculo da média ponderada
MEDIA = (A * 2 + B * 3 + C * 5) / 10

# Exibe o resultado formatado com 1 casa decimal
print(f"MEDIA = {MEDIA:.1f}")
# A função `input()` é usada para ler as notas.
# A variável `MEDIA` armazena o resultado da média ponderada.
# O uso de `f-string` permite formatar a saída com precisão específica. 