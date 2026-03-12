from datetime import datetime
import os
import random
from playsound import playsound

def descobrir_signo(dia,mes):
    if (mes == 1 and dia >=20) or (mes ==2 and dia <=19):
        return "Aquário"
    elif (mes == 2 and dia >=19) or (mes ==3 and dia <=20):
        return "Peixes"
    elif (mes == 3 and dia >=21) or (mes == 4 and dia <=19):
        return "Áries"
    elif (mes == 4 and dia >=20) or (mes == 5 and dia <=20):
        return "Touro"
    elif (mes == 5 and dia >=21) or (mes == 6 and dia <=20):
        return "Gêmeos"
    elif (mes == 6 and dia >=21) or (mes == 7 and dia <=22):
        return "Câncer"
    elif (mes == 7 and dia >=23) or (mes == 8 and dia <=22):
        return "Leão"
    elif (mes == 8 and dia >=23) or (mes == 9 and dia <=22):
        return "Virgem"
    elif (mes == 9 and dia >=23) or (mes == 10 and dia <=22):
        return "Libra"
    elif (mes == 10 and dia >=23) or (mes == 11 and dia <=21):
        return "Escorpião"
    elif (mes == 11 and dia >=22) or (mes == 12 and dia <=21):
        return "Sagitário"
    elif (mes == 12 and dia >=22) or (mes == 1 and dia <=19):
        return "Capricórnio"
    else:
         return None

while True:
    entrada = input("Digite sua data de nascimento: ")

    if entrada.lower() == "sair":
       break

    try:
        data = datetime.strptime(entrada, "%d/%m")
        dia = data.day
        mes = data.month
        signo = descobrir_signo(dia, mes)

        if signo:
            print(f"\nSeu signo é: {signo}")
        else:
            print("Não consegui identificar seu signo.")
    except ValueError:
        print("Formato inválido! Use dd/mm")
        continue


    caminho_musicas = "musicas"
    todas_as_musicas = [nome for nome in os.listdir(caminho_musicas) if nome.endswith(".mp3")]
    todas_as_musicas_formatadas = [nome.strip().lower() for nome in todas_as_musicas]

    arquivo_tocadas = "tocadas.txt"

    if os.path.exists(arquivo_tocadas):
       with open (arquivo_tocadas,"r") as f:
        musicas_tocadas = [linha.strip() for linha in f.readlines()]
    else:
      musicas_tocadas = []

    musicas_disponiveis = [orig for orig, norm in zip(todas_as_musicas, todas_as_musicas_formatadas) if norm not in musicas_tocadas]
    if len(musicas_disponiveis) == 0:
      with open(arquivo_tocadas, "w") as f:
         f.write("")
      musicas_tocadas = []
      musicas_disponiveis = todas_as_musicas.copy()

    musica_escolhida = random.choice(musicas_disponiveis)
    nome_musica = musica_escolhida.replace(".mp3", "")
    print(f"Sua música é: {nome_musica}")


    caminho_musicas_completo = os.path.join(caminho_musicas, musica_escolhida)

    with open(arquivo_tocadas, "a") as f:
      f.write(musica_escolhida.strip().lower() + "\n")
    playsound(caminho_musicas_completo)
    playsound(caminho_musicas_completo)

    repetir = input("\nDeseja encerrar o programa? Digite 'sair' ou pressione Enter para continuar: ")
    if repetir.strip().lower() == "sair":
       break



