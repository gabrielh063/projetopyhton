import random

def adivinhe_o_numero():
    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Eu escolhi um número entre 1 e 100. Você tem 10 tentativas para adivinhar.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while tentativas < 10:
        try:
            palpite = int(input("Faça uma suposição: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue
        
        if palpite < 1 or palpite > 100:
            print("O número deve estar entre 1 e 100.")
            continue
        
        tentativas += 1
        
        if palpite < numero_secreto:
            print("O número correto é maior do que a suposição.")
        elif palpite > numero_secreto:
            print("O número correto é menor do que a suposição.")
        else:
            print(f"Parabéns! Você adivinhou corretamente o número em {tentativas} tentativas!")
            break
    
    if tentativas == 10:
        print(f"Fim de jogo! O número correto era {numero_secreto}. Você não conseguiu adivinhar.")

    jogar_novamente = input("Deseja jogar novamente? (sim/não): ")
    if jogar_novamente.lower() == "sim":
        adivinhe_o_numero()
    else:
        print("Obrigado por jogar! Até mais.")

adivinhe_o_numero()
