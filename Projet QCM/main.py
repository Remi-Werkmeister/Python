from qcm import Questionnaire

if __name__ == "__main__":
    questionnaire = Questionnaire('Questions.json')  # Crée une instance de la classe Questionnaire avec le fichier JSON
    questionnaire.poser_questions()                  # Pose les questions à l'utilisateur
    questionnaire.afficher_correction()              # Affiche les corrections

