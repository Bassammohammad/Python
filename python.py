  import random

max_tentatives = 10
rejouer = 'o'

while rejouer == 'o' :
    random_num = random.randint(1, 100)
    tentatives = 0
    print("Bienvenue dans le jeu")

    while tentatives < max_tentatives:
        devine = int(input("Veuillez choisir un nombre entre 1 et 100 : "))

        if devine < random_num :
            print("Plus haut")
        elif devine > random_num :
            print("Plus bas")
        else:
            print("Bravo, vous avez trouvé le nombre !")
            break

        tentatives += 1

    if tentatives >= max_tentatives :
        print(f"Vous avez épuisé vos {max_tentatives} tentatives. Le nombre était {random_num}.")

    rejouer = input('Voulez-vous rejouer ? o/n: ').lower()

print("Merci d'avoir joué !")
