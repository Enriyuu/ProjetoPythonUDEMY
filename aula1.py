nome = input("Qual o seu nome?")
sobrenome = input("Qual o seu sobrenome?")
idade = int(input("Qual a sua idade?"))
ano_de_nascimento = input("Qual o seu ano de nascimento?")
altura = input("Qual a sua altura?")
print("O nome do usuário é:", nome, sobrenome)
print("A idade do usuário é: ,", idade, "Nascida em: ", ano_de_nascimento)
if idade < 18:
    print("O usuário é de menor")
elif idade >= 18:
    print("O usuário é de maior: ")
print("A altura do usuário é de: ", altura)