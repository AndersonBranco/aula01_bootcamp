BONUS_USUARIO = 1000.00
nome_usuario = input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salário: "))
bonus_usuario = float(input("Digite o valor do bônus: "))
salario_usuario = BONUS_USUARIO + salario_usuario * bonus_usuario
print(f"O salário final de {nome_usuario} é: {salario_usuario}")