print("JOGO PEDRA, PAPEL E TESOURA!!")
c1 = 0
c2 = 0
loop = "s"
jogo = ["m1", "m2", "m3"]

qst = int(input(f"você deseja jogar melhor de 1 ou melhor de 3? digite '1' para melhor de 1 e '2' para melhor de 3: "))
if qst == 1:
    while loop.lower() == "s":
        print("MELHOR DE 1!!")
        while True:
            j1 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
            if j1 not in jogo:
                print("voce digitou um caractere inválido, tente novamente.")
            else:
                break
        while True:
            j2 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
            if j2 not in jogo:
                print("voce digitou um caractere inválido, tente novamente.")
            else:
                break
        if (j1 == "m1" and j2 == "m3") or (j1 == "m2" and j2 == "m1") or (j1 == "m3" and j2 == "m2"):
            print("o jogador n°1 ganhou!")
        elif (j1 == "m1" and j2 == "m2") or (j1 == "m2" and j2 == "m3") or (j1 == "m3" and j2 == "m1"):
            print("o jogador n°2 ganhou!")
        elif (j1 == "m1" and j2 == "m1") or (j1 == "m2" and j2 == "m2") or (j1 == "m3" and j2 == "m3"):
            print("o jogo empatou.")
        loop = input("você deseja jogar novamente? (s/n): ")
        if loop.lower() != "s":
            break
else:
    while loop.lower() == "s":
        print("MELHOR DE 3!!")
        for x in range(3):
            print(f"{x + 1}° rodada")
            while True:
                j1 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
                if j1 not in jogo:
                    print("voce digitou um caractere inválido, tente novamente.")
                else:
                    break
            while True:
                j2 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
                if j2 not in jogo:
                    print("voce digitou um caractere inválido, tente novamente.")
                else:
                    break
            if (j1 == "m1" and j2 == "m3") or (j1 == "m2" and j2 == "m1") or (j1 == "m3" and j2 == "m2"):
                c1 += 1
                print("o jogador n°1 ganhou essa rodada.")
            elif (j1 == "m1" and j2 == "m2") or (j1 == "m2" and j2 == "m3") or (j1 == "m3" and j2 == "m1"):
                c2 += 1
                print("o jogador n°2 ganhou essa rodada.")
            elif (j1 == "m1" and j2 == "m1") or (j1 == "m2" and j2 == "m2") or (j1 == "m3" and j2 == "m3"):
                print("essa rodada foi empate.")
        if c1 >= 2 or (c1 == 1 and c2 == 0):
            print("o jogador n°1 ganhou a melhor de 3!!")
        elif c2 >= 2 or (c2 == 1 and c1 == 0):
            print("o jogador n°2 ganhou a melhor de 3!!")
        else:
            print("o jogo foi empate!!")
        loop = input("você deseja jogar novamente? (s/n): ")
        if loop.lower() != "s":
            break
print("programa finalizado")
