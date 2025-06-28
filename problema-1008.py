# Problema 1008 - Salário (Beecrowd)
# Este programa calcula o salário de um funcionário com base no número, horas trabalhadas e valor/hora

# Leitura dos dados
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Impressão dos resultados no formato solicitado
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}") 