import math

class password_testing:
    def calcul_strength(self, password):
        password_length = len(password)                             # Calcul de la longueur du mot de passe
        alphabet_size = self.determine_alphabet_size(password)      # Détermination de la taille de l'alphabet utilisé dans le mot de passe
        strength = password_length * math.log2(alphabet_size)       # Calcul de la force du mot de passe en utilisant la formule : longueur * log2(taille de l'alphabet)


        entropie = strength
                                                                    # Évaluation de la force du mot de passe en fonction de sa force calculée
        if strength <= 64:
            force = "La force du mot de passe est très faible"
        elif 64 < strength < 80:
            force = "La force du mot de passe est faible"
        elif 80 <= strength < 100:
            force = "La force du mot de passe est moyenne"
        else:
            force = "La force du mot de passe est forte"

        return force, entropie

    def determine_alphabet_size(self, password):
        char_types = set()                                          # Ensemble pour stocker les types de caractères présents dans le mot de passe
                                                                    # Vérification de la présence de différents types de caractères et ajout à l'ensemble
        if any(char in "&[|]@^µ§:/ ;.,<>°²³" for char in password):
            char_types.add('extended_special_chars')
        if any(char in "!#$*%?" for char in password):
            char_types.add('standard_special_chars')
        if any(char.islower() for char in password):
            char_types.add('lowercase')
        if any(char.isupper() for char in password):
            char_types.add('uppercase')
        if any(char.isdigit() for char in password):
            char_types.add('digits')
        if all(char in '01' for char in password):
            char_types.add('binary')

        alphabet_sizes = {                                  # Dictionnaire définissant la taille de l'alphabet pour chaque type de caractère
            'extended_special_chars': 90,
            'standard_special_chars': 70,
            'lowercase': 26,
            'uppercase': 26,
            'digits': 10,
            'binary': 2
        }

        total_alphabet_size = sum(alphabet_sizes[char_type] for char_type in char_types)        # Calcul de la taille totale de l'alphabet en fonction des types de caractères présents
        return total_alphabet_size if total_alphabet_size > 0 else 70                            # Si aucun type de caractère n'est détecté, on retourne une taille d'alphabet par défaut de 70

