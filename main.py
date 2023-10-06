# Exercicio 3
#
# a = int(input("Digite um valor: "))
# b = 0
#
# while b < a:
#     b = b + 1
#     if b % 2 == 0:
#         print(b)
#     if b == a:
#         break
#     else:
#         continue
#

# Exercicio 4

# a = int(input("Digite um valor: "))
# b = 0
#
# while b < a:
#     b = b + 1
#     if b % 2 == 1:
#         print(b)
#     if b == a:
#         break
#     else:
#         continue

# Exercicio 5

# i = int(input("Valor Inicial do intervalor: "))
# f = int(input("Valor Final do intervalor: "))
#
# a = 0
#
# print(f"A soma de todos os pares entre o intervalo de {i} e {f}")
#
# while i <= f:
#     i = i + 1
#     if i % 2 == 0:
#         print(i)
#         a += i
#     if i == f:
#         break
#
# print(f"É {a}")

# Exercicio 6

# i = int(input("Valor Inicial do intervalor: "))
# f = int(input("Valor Final do intervalor: "))
#
# a = 0
#
# print(f"A soma de todos os pares entre o intervalo de {i} e {f}")
#
# while i <= f:
#     i = i + 1
#     if i % 2 == 1:
#         print(i)
#         a += i
#     if i == f:
#         break
#
# print(f"É {a}")

# Exercicio 7

# notas = 0
# i = 0
#
# n = int(input("Quantas notas serão inseridas? "))
#
# c = 0
# sum = 0
#
# while i < notas:
#     notas += 1
#     if notas == n:
#         break
#
# while c < n:
#     nota = int(input(f"Nota {c + 1}: "))
#     sum += nota
#     c += 1
#     media = sum / n
#
# print(f"A Media das notas é {media}")

# Exercicio 8

# tabu = int(input("Deseja ver a tabuada de qual numero: "))
#
# mult = 0
#
# while mult < 10:
#     mult += 1
#     print(f"{mult} x {tabu} = {mult * tabu}")

# Exercicio 9

# tabu = int(input("Deseja ver a tabuada de qual numero: "))
# fim = int(input("Até onde vai a tabuada: "))
#
# mult = 0
#
# while mult < fim:
#     mult += 1
#     print(f"{mult} x {tabu} = {mult * tabu}")

# Exercicio 10 ( Incompleto )

# n = int(input("Digite um numero: "))
# i = 0
#
# while i < n:
#     i += 1
#     m = int(input("Digite mais um numero: "))
#     print(m)
#     if m == 0:
#         break

# Exercicio 11

# precos = {
#     "C1": 0.5,
#     "C2": 1,
#     "C3": 4,
#     "C5": 7,
#     "C9": 8,
# }
#
# total = 0
#
# while True:
#     codigo = input("Código do produto: ")
#
#     if codigo not in precos:
#         print("Código inválido!")
#         continue
#
#     quantidade = int(input("Quantidade comprada: "))
#
#     valor = precos[codigo] * quantidade
#
#     total += valor
#
#     print(f"Valor: R$ {valor}")
#
#     opcao = input("Deseja continuar (S/N)? ")
#
#     if opcao.upper() == "N":
#         break
#
# print(f"Total: R$ {total}")

# Exercicio 12

# mult = 0
#
# while True:
#
#     tabu = int(input("Deseja ver a tabuada de qual numero: "))
#     ope = input("Usando qual operação ? (+,-,*,/): ")
#
#     mult = 0
#     adi = 0
#     sub = 0
#     div = 0
#
#     if ope == "+":
#         while adi < 10:
#             adi += 1
#             print(f"{tabu} + {adi} = {tabu + adi}")
#     elif ope == "-":
#         while sub < 10:
#             sub += 1
#             print(f"{tabu} - {sub} = {tabu - sub}")
#     elif ope == "*":
#         while mult < 10:
#             mult += 1
#             print(f"{tabu} * {mult} = {tabu * mult}")
#     elif ope == "/":
#         while div < 10:
#             div += 1
#             print(f"{tabu} / {div} = {tabu / div}")
#     else:
#         print("Operação Invalida")
#         break
#
#     opcao = input("Deseja uma nova tabuada (S/N)? ")
#
#     if opcao.upper() == "N":
#         break


# Exercicio 13

# numero = int(input("Escolha um numero: "))
#
# if numero <= 1:
#     print(f"{numero} Não é primo")
#
# elif numero == 2:
#     print(f"{numero} é Primo")
#
# elif numero % 2 == 0:
#     print(f"{numero} Não é Primo")
#
# else:
#     i = 3
#     while i*i <= numero:
#         if numero % i == 0:
#             print(f"{numero} Não é primo")
#             break
#         i += 2
#     else:
#         print(f"{numero} é Primo")

# COMO CRIAR OBJETOS EM PYTHON
# a = {
#     "nome": "Lucas",
#     "idade": 17,
# }
#
# print(a["nome"])


