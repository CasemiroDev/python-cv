lado1 = float(input("Digite o valor de um lado: "))
lado2 = float(input("Digite o valor de outro lado: "))
lado3 = float(input("Digite o valor de mais um lado: "))
if lado1 <= lado2 + lado3 and lado2 <= lado1 + lado3 and lado3 <= lado1 + lado2 :
    print("É possível fazer um triângulo.")
else :
    print("Impossível fazer um triângulo.")