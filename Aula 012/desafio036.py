# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("Bank of Canada")

valor_casa = float(input("Qual o valor da casa que quer comprar: "))
salario_comprador = float(input("Qual o salario do comprador: "))
anos_do_emprestimo = int(input("Quantidade de anos para pagamento: "))
prestacao_mensal = (valor_casa / anos_do_emprestimo)/12
aprovacao = salario_comprador * 0.3

if(prestacao_mensal > aprovacao):
    print("O seu crédito nao pode ser aprovado, desculpe")
else:
    print("Parabéns seu crédito foi aprovado!!!!")


