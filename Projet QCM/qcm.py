import json
from Question import Question

class Questionnaire:        # Définition de la classe Questionnaire
    def __init__(self, fichier):
        self.questions = self.lire_fichier(fichier)         # Méthode lire_fichier pour lire les questions et reponse depuis le fichier JSON
                                                            # Stocke la liste des objets Question dans l'attribut questions

    def lire_fichier(self, fichier):        # Méthode pour lire les questions depuis un fichier JSON

        with open(fichier, 'r') as file:            # Ouvre le fichier en mode lecture
            data = json.load(file)                  # Charge les données JSON depuis le fichier et les stocke dans la variable data
        questions = []                              # Initialise une liste vide pour stocker les objets Question

        for q in data:                              # Boucle à travers chaque élément dans data (chaque question)
            question = Question(q)                  # Crée un objet Question avec les données de la question actuelle
            questions.append(question)              # Ajoute l'objet Question à la liste des questions
        return questions


    def poser_questions(self):                      # Méthode pour poser toutes les questions du questionnaire
        score = 0

        for question in self.questions:              # Boucle à travers la liste des questions

            question.poser()                         # Appelle la méthode poser() pour chaque objet Question
            if question.est_correcte():              # Vérifie si la réponse donnée par l'utilisateur est correcte
                score += 1

        print("\nVotre score final est de " +str(int(score))+ "/10")         # Affiche le score final de l'utilisateur


    def afficher_correction(self):                      # Méthode pour afficher les corrections du questionnaire

        print("\nCorrigé complet :")
        for question in self.questions:                     # Boucle à travers la liste des questions
            question.afficher_correction()
