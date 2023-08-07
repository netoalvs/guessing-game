import random

print("Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

secret_number = random.randint(1, 100)

guess = None
attempts = 0
max_attempts = 3  # Definindo o limite de tentativas

while guess != secret_number and attempts < max_attempts:
    try:
        guess = int(input("Tente adivinhar o número: "))
        attempts += 1

        if guess < secret_number:
            print("Tente um número maior.")
        elif guess > secret_number:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número em {attempts} tentativa(s).")
            break
    except ValueError:
        print("Por favor, insira um número válido.")

if guess != secret_number:
    print(f"Você não conseguiu adivinhar o número. O número era {secret_number}.")
