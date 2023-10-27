import random

class PassphraseGenerator:          # Définition de la classe PassphraseGenerator
    def __init__(self, wordlist_path):

        self.wordlist = self.load_wordlist(wordlist_path) # Chargement du fichier fourni et stockage dans l'attribut wordlist

    def load_wordlist(self, file_path):                                 # Méthode pour charger la liste de mots à partir d'un fichier
        words = {}                                                      # Création d'un dictionnaire vide pour stocker les mots
        with open(file_path, 'r') as f:                                 # Ouverture du fichier en mode lecture
            for line in f:                                              # Parcours de chaque ligne du fichier
                number, word = line.strip().split('\t')                 # Séparation du numéro et du mot, suppression des espaces blancs
                words[number] = word                                    # ajout au dictionnaire
        return words

    def roll_dice(self):                                        # Méthode pour lancer un dé et retourner le résultat
        return str(random.randint(1, 6))                  # Retourne un nombre aléatoire entre 1 et 6 sous forme de chaîne de caractères

    def generate_passphrase(self,num_words=6):      # Méthode generate_passphrase avec un paramètre notre nombres de mot
        passphrase = []                             # Initialisation d'une liste vide

        for _ in range(num_words):                                      
            dice_rolls = ''.join(self.roll_dice() for _ in range(5))     # Lancement de cinq dés et concaténation des résultats pour créer un nombre à cinq chiffres
            word = self.wordlist.get(dice_rolls, "word_not_found")       # recherche du mot correspondant dans la liste de mots
            passphrase.append(word)                                      # ajout du mot à la passphrase

        return ' '.join(passphrase)

