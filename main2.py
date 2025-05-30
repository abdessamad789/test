import re

def valider_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valider_mot_de_passe(mot_de_passe):
    return len(mot_de_passe) >= 6

def inscription():
    print("=== Formulaire d'inscription ===")
    nom = input("Nom : ")
    email = input("Email : ")
    mot_de_passe = input("Mot de passe : ")

    if not valider_email(email):
        print("❌ Email invalide.")
        return

    if not valider_mot_de_passe(mot_de_passe):
        print("❌ Mot de passe trop court (min 6 caractères).")
        return

    with open("utilisateurs.txt", "a") as f:
        f.write(f"{nom},{email},{mot_de_passe}\n")

    print(f"✅ Inscription réussie pour {nom}.")
    print(f"📧 Email de confirmation envoyé à {email} (simulé).")

def calculatrice():
    print("=== Calculatrice ===")
    while True:
        try:
            a = float(input("Entrez le premier nombre : "))
            op = input("Opération (+, -, *, / ou q pour quitter) : ")
            if op == "q":
                break
            b = float(input("Entrez le deuxième nombre : "))

            if op == "+":
                print(f"Résultat : {a + b}")
            elif op == "-":
                print(f"Résultat : {a - b}")
            elif op == "*":
                print(f"Résultat : {a * b}")
            elif op == "/":
                if b != 0:
                    print(f"Résultat : {a / b}")
                else:
                    print("❌ Division par zéro interdite.")
            else:
                print("❌ Opération inconnue.")
        except ValueError:
            print("❌ Veuillez entrer des nombres valides.")

def connexion():
    print("=== Connexion ===")
    email = input("Email : ")
    mot_de_passe = input("Mot de passe : ")

    try:
        with open("utilisateurs.txt", "r") as f:
            for ligne in f:
                nom_enregistre, email_enregistre, mdp_enregistre = ligne.strip().split(",")
                if email == email_enregistre and mot_de_passe == mdp_enregistre:
                    print(f"✅ Connexion réussie. Bienvenue, {nom_enregistre} !")
                    calculatrice()
                    return
    except FileNotFoundError:
        print("❌ Aucun utilisateur inscrit pour le moment.")
        return

    print("❌ Échec de la connexion. Email ou mot de passe incorrect.")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Inscription")
        print("2. Connexion")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            inscription()
        elif choix == "2":
            connexion()
        elif choix == "3":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    menu()
