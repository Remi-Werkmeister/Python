import random
import string
from Password_testing import password_testing

class mdpGenerator:
    def generate_mdp(self, num_lowercase, num_uppercase, num_digits, num_special_chars):


                                                                                                # Définition des ensembles de caractères pour chaque catégorie
        lowercase_letters = string.ascii_lowercase                                              # Lettres minuscules
        uppercase_letters = string.ascii_uppercase                                              # Lettres majuscules
        digits = string.digits                                                                  # Chiffres
        special_chars = string.punctuation                                                      # Caractères spéciaux

        mdp = []                                                                                # Liste vide pour stocker les caractères du mot de passe
        mdp.extend(random.choice(lowercase_letters) for _ in range(num_lowercase))              # Ajout de lettres minuscules
        mdp.extend(random.choice(uppercase_letters) for _ in range(num_uppercase))              # Ajout de lettres majuscules
        mdp.extend(random.choice(digits) for _ in range(num_digits))                            # Ajout de chiffres
        mdp.extend(random.choice(special_chars) for _ in range(num_special_chars))              # Ajout de caractères spéciaux

        random.shuffle(mdp)                                                 # Mélange aléatoire des caractères

        generated_mdp = ''.join(mdp)                                        # Conversion de la liste de caractères en une chaîne de caractères

        testeur = password_testing()                                        # Création d'une instance de la classe password_testing pour évaluer la force du mot de passe


        force, entropie = testeur.calcul_strength(generated_mdp)         # Calcul de la force et de l'entropie du mot de passe généré


        return generated_mdp, force, entropie
