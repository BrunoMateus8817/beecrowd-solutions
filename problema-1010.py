# Problema 1010 - Cálculo Simples (Beecrowd)
# Calcula o valor total a pagar por duas peças com quantidade e preço unitário

# Leitura da primeira linha de dados
linha1 = input().split()
cod1 = int(linha1[0])
qtd1 = int(linha1[1])
valor1 = float(linha1[2])

# Leitura da segunda linha de dados
linha2 = input().split()
cod2 = int(linha2[0])
qtd2 = int(linha2[1])
valor2 = float(linha2[2])

# Cálculo do valor a pagar
total = (qtd1 * valor1) + (qtd2 * valor2)

# Exibição do valor formatado
print(f"VALOR A PAGAR: R$ {total:.2f}") 