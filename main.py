import re

def valider_email(email):
    # Validation simple d'email avec regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valider_mot_de_passe(mot_de_passe):
    # Mot de passe >= 6 caractères
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

    # Enregistrer dans un fichier (simule une base de données)
    with open("utilisateurs.txt", "a") as f:
        f.write(f"{nom},{email},{mot_de_passe}\n")

    # Simuler l'envoi d'un email
    print(f"✅ Inscription réussie pour {nom}.")
    print(f"📧 Email de confirmation envoyé à {email} (simulé).")

if __name__ == "__main__":
    inscription()
