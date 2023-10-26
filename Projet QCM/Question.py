import random
class Question:                                     # Définition de la classe Question
    def __init__(self, data):
        self.enonce = data['question']             # Initialisation de l'énoncé de la question avec les données fournies
        self.options = {                           # Initialisation des options de réponse sous forme de dictionnaire
            'a': data['options']['a'],
            'b': data['options']['b'],
            'c': data['options']['c']
        }
        self.reponse_correcte = data['reponse']    # Initialisation de la réponse correcte avec les données fournies

        self.reponse_utilisateur = None             # Initialisation de la réponse de l'utilisateur à None



    def poser(self):                                    # Méthode pour poser la question à l'utilisateur

        options_melangees = list(self.options.items()) # Convertit les options en liste de tuples et les mélange pour les afficher dans un ordre aléatoire
        random.shuffle(options_melangees)

        while True:                                     # Boucle qui continue jusqu'à ce que l'utilisateur entre une réponse valide
            print("Question : " + self.enonce)          # Affiche l'énoncé de la question
            for lettre, choix in options_melangees:     # Affiche les options de réponse
                print(f"Réponse {lettre}: {choix}")

            reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()  # Demande la réponse à l'utilisateur et la convertit en minuscule

            if reponse_utilisateur in self.options:                              # Vérifie si la réponse de l'utilisateur est l'une des options possibles

                self.reponse_utilisateur = reponse_utilisateur
                break
            else:
                print("Merci d'entrer une réponse valide (a, b ou c).\n")

        print("\n")

    def est_correcte(self):                                             # Méthode pour vérifier si la réponse de l'utilisateur est correcte
        return self.reponse_utilisateur == self.reponse_correcte

    def afficher_correction(self):                                      # Méthode pour afficher la correction de la question
        print("Question : " + self.enonce)                              # Affiche l'énoncé de la question
        for lettre, choix in self.options.items():                      # Affiche les options de réponse
            print(f"Réponse {lettre}: {choix}")

        print(f"Réponse correcte : {self.reponse_correcte}")                    # Affiche la réponse correcte

        if self.reponse_utilisateur:                                            # Vérifie si l'utilisateur a répondu à la question

            print(f"Votre réponse : {self.reponse_utilisateur} ({'Correcte' if self.est_correcte() else 'Incorrecte'})\n")

