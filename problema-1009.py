# Problema 1009 - Salário com Bônus (Beecrowd)
# Calcula o salário total de um vendedor com 15% de comissão sobre as vendas

# Leitura de dados
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

# Cálculo do salário total
salario_total = salario_fixo + (0.15 * total_vendas)

# Exibe o resultado formatado
print(f"TOTAL = R$ {salario_total:.2f}") 