import os
import random
import time
import requests
from colorama import Fore, Style, init
from tqdm import tqdm

os.system("title Nitro Generator by YoannCHVL .gg/Jm2huzaMBm")

init(autoreset=True)

def afficher_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
  _   _ _                      _____                           _             
 | \ | (_)                    / ____|                         | |            
 |  \| |_  __ _  __ _  __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | . ` | |/ _` |/ _` |/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |\  | | (_| | (_| | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_| \_|_|\__, |\__, |\__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
           __/ | __/ |                                                       
          |___/ |___/                                                          
    """)

    print(Fore.YELLOW + "[1] Nitro Generator")
    print(Fore.YELLOW + "[2] Nitro Checker")
    print(Fore.YELLOW + "[3] Crédits")
    print(Fore.YELLOW + "[0] Fermer\n")

def generer_code():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choices(caracteres, k=16))

def verifier_nitro(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

def afficher_credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "Ce tool a été créé par YoannCHVL")
    print(Fore.YELLOW + "Si vous avez des questions rejoignez ce serveur discord : https://discord.gg/Jm2huzaMBm")
    print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
    input()

def main():
    while True:
        afficher_menu()
        choix = input(Fore.CYAN + "[->] Choisissez une option : ")
        
        if choix == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + "Combien de nitro voulez-vous générer ?")
            try:
                nombre = int(input(Fore.CYAN + "[->] Entrez un nombre : "))
                os.system('cls' if os.name == 'nt' else 'clear')

                fichier = open("nitro.txt", "w")
                print(Fore.RED + "Génération des nitro en cours...")
                for _ in tqdm(range(nombre), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Style.RESET_ALL)):
                    code = f"https://discord.gift/{generer_code()}"
                    fichier.write(code + "\n")
                    time.sleep(0.01)
                fichier.close()

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Les codes ont été stockés dans le fichier nitro.txt")
                print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
                input()
            
            except ValueError:
                print(Fore.RED + "[Erreur] Veuillez entrer un nombre valide.")
                time.sleep(2)
        
        elif choix == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + "Le Nitro Checker va checker les nitro de 'nitro.txt'...")
            try:
                with open("nitro.txt", "r") as fichier:
                    lignes = fichier.readlines()

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.YELLOW + "Lancement du Nitro Checker...\n")
                valid_codes = []

                for ligne in tqdm(lignes, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Style.RESET_ALL)):
                    code = ligne.strip().split('/')[-1]
                    if verifier_nitro(code):
                        valid_codes.append(ligne.strip())

                if valid_codes:
                    with open("validnitro.txt", "w") as valid_fichier:
                        for valid_code in valid_codes:
                            valid_fichier.write(valid_code + "\n")
                    print(Fore.GREEN + "\nLes codes valides ont été stockés dans 'validnitro.txt'.")
                else:
                    print(Fore.RED + "\nAucun code valide trouvé.")

                print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
                input()
            except FileNotFoundError:
                print(Fore.RED + "[Erreur] Le fichier 'nitro.txt' n'a pas été trouvé.")
                time.sleep(2)

        elif choix == "3":
            afficher_credits()

        elif choix == "0":
            print(Fore.RED + ":(")
            break

        else:
            print(Fore.RED + "[Erreur] Choix invalide. Veuillez réessayer.")
            time.sleep(2)

if __name__ == "__main__":
    main()
