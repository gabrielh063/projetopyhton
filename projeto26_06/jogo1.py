import random

def jogar_forca():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'teclado', 'sistemas']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_'] * len(palavra_secreta)
    tentativas = 10
    letras_chutadas = []

    while True:
        print('\n' + ' '.join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras chutadas: {' '.join(letras_chutadas)}")

        chute = input("Digite uma letra: ").lower()

        if chute in letras_chutadas:
            print("Você já chutou essa letra!")
            continue

        letras_chutadas.append(chute)

        if chute in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_descobertas[i] = chute

            if '_' not in letras_descobertas:
                print("Parabéns, você ganhou!")
                break
        else:
            print("Letra errada!")
            tentativas -= 1

            if tentativas == 0:
                print("Você perdeu!")
                print(f"A palavra secreta era: {palavra_secreta}")
                break

jogar_forca()
