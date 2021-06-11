import random
from mots import mots
import string


score = 0
nom_joueur = ""

def choisir_mot(mots):
    mot = random.choice(mots)
    return mot

def jouer_de_nouveau():
    jouer_jeu = input("Souhaitez vous continuer à jouer? (O = Oui, N = Non)")
    while jouer_jeu not in {"O","o", "N", "n"}:
        jouer_jeu = input("Souhaitez vous continuer à jouer? (O = Oui, N = Non)")
    if jouer_jeu == "O" or jouer_jeu == "o":
        hangman()
    elif jouer_jeu == "N" or jouer_jeu == "n":
        print("Merci d'avoir jouer et à bientôt !")
        exit()

def recuperer_nom_joueur():
    nom_joueur = input("Merci de saisir votre nom:")
    nom_joueur = nom_joueur.capitalize()
    if not nom_joueur.isalpha() or len(nom_joueur) < 4:
        print("Le nom que vous avez saisi est invalide")
        return recuperer_nom_joueur()
    else:
        return nom_joueur


def hangman():

    global nom_joueur
    if nom_joueur == "":
        nom_joueur = recuperer_nom_joueur()

    global score

    mot_original = choisir_mot(mots)
    mot = mot_original.upper()

    mot_lettre = set(mot)
    alphabet = set(string.ascii_uppercase)
    lettres_jouees = set()
    essai = 6

    while len(mot_lettre) > 0 and essai > 0:
        print("Vous avez", essai, "essai(s) et vous avez utilisé les lettres suivantes:", ','.join(lettres_jouees))
        mot_list = [lettre if lettre in lettres_jouees else "_" for lettre in mot]
        print("Le mot actuel est:", ' '.join(mot_list))

        lettre_choisie = input("Entrer une lettre !").upper()
        if lettre_choisie in alphabet - lettres_jouees:
            lettres_jouees.add(lettre_choisie)
            if lettre_choisie in mot_lettre:
                mot_lettre.remove(lettre_choisie)
                essai = 6
            else:
                essai -= 1
                print("Il vous reste", essai, "essai(s)")
        elif lettre_choisie in lettres_jouees:
            print(nom_joueur, ",vous avez dèja utilisé cette lettre, choisissez une lettre!")

        else:
            print(nom_joueur, ",votre choix est invalide, merci de saisir une lettre!")

    if essai == 0:
        print(nom_joueur, ", vous avez perdu, il ne vous reste aucun essai!")
        jouer_de_nouveau()
    else:
        print(nom_joueur, ",le mot à deviner est", mot, "vous avez gangné!")
        score += 10
        print(nom_joueur, ", votre score est:", score)
        jouer_de_nouveau()




hangman()