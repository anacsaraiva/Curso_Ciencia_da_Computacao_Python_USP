largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 0
j = 0
while i < altura:
    while j < largura:
        print("#",end="")
        j +=1
    print()
    j = 0
    i += 1
