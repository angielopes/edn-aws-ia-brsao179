# %%
"""1- Programa de Saudação
* Crie um programa que imprima a mensagem "Olá, mundo!" na tela."""

print("Olá, mundo!")
# %%
"""2- Calculadora de Soma
* Desenvolva um programa que soma dois números.
Use as variáveis numero1 = 12 e numero2 = 14.
O programa deve calcular a soma e exibir o resultado."""

numero1 = int(input("Digite um número inteiro positivo: "))
numero2 = int(input("Digite outro número inteiro positivo: "))

soma = numero1 + numero2

print(f"A soma de {numero1} e {numero2} é: {soma}")
# %%
"""3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³."""

comprimento = int(input("Comprimento: "))
largura = int(input("Largura: "))
altura = int(input("Altura: "))

volume = comprimento * largura * altura

print(f"{volume}cm³.")
# %%
