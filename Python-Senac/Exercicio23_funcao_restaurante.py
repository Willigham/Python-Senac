import Exercicio22_funcao_restaurante as fun

valor = int(input("Informe o valor: "))


porcentagem = fun.calcular(valor)
novo_valor = porcentagem + valor

print("Valor:",valor)
print("Valor com acréscimo 11%:", novo_valor )
