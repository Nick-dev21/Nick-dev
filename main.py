num1 = float(input("Digite um valor: "))
num2 = float(input("Digite um valor: "))

print("Qual operação você deseja fazer?")
print("\t 1 - soma")
print("\t 2 - subtração")
print("\t 3 - divisão")
print("\t 4 - multiplicação")

op = input("Digite o valor entre (1-4)?")

if (op == "1"):
  print(num1, "+", num2," = ", num1+num2)
elif(op == "2"):
    print(num1, "-", num2," = ", num1 - num2)
elif(op == "3"):
  print(num1, "/", num2," = ", num1 / num2)
elif(op == "4"):
  print(num1, "*", num2," = ", num1 * num2)
elif(op == "1"):
  print(num1, "+", num2," = ", num1 + num2)

if(num1 + num2) == 42.0:
  print("omaigotto vose acho o ister égui")
else:
   print("Você adcionou uma opção inválida.")
