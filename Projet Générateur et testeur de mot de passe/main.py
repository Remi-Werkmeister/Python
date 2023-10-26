from Password_testing import password_testing
from mdp_generator import mdpGenerator
from passphrase_generator import PassphraseGenerator

def main():
    while True:
        print("="*40)
        print("Outils de Sécurité pour les Mots de Passe".center(40))
        print("="*40)
        print("\nVeuillez choisir une option :")
        print("[1] Tester la force d'un mot de passe")
        print("[2] Générer un mot de passe aléatoire")
        print("[3] Générer une passphrase")
        print("[Q] Quitter")

        choice = input("\nVotre choix : ").upper()

        if choice == "1":
            password = input("\nEntrez le mot de passe à tester : ")
            testeur = password_testing()
            force, entropie = testeur.calculate_strength(password)
            print(force)
            print("Entropie :" + str(int(entropie)) + " bits")

        elif choice == "2":
            num_lowercase = int(input("Nombre de minuscules : "))
            num_uppercase = int(input("Nombre de majuscules : "))
            num_digits = int(input("Nombre de chiffres : "))
            num_special_chars = int(input("Nombre de caractères spéciaux : "))

            generateur = mdpGenerator()
            mot_de_passe, force, entropie = generateur.generate_mdp(num_lowercase, num_uppercase, num_digits,num_special_chars)
            print("Votre mot de passe : "+mot_de_passe)
            print(force)
            print("Entropie :" + str(int(entropie)) + " bits")

        elif choice == "3":
            generator = PassphraseGenerator("eff_large_wordlist.txt")
            passphrase = generator.generate_passphrase()
            print("Votre passphrase est:", passphrase)

        elif choice == "Q":
            print("\nAu revoir")
            break
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
