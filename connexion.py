import random
print("Voici les prénoms à deviner : Ali, Mohammed, Yacine")
prenom = ["ali", "mohammed", "yacine"]
choix = random.choice(prenom)
reponse = input("Entrez le prénom à deviner :").strip().lower()

if reponse == choix :
    print("Bien joué ^^ !")
else :
    print("Dommage, la réponse était", choix)
