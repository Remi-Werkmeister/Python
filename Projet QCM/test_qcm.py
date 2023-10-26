import unittest
from Question import Question
from qcm import Questionnaire

class TestQuestion(unittest.TestCase):
    def test_est_correcte(self):                 # Teste la méthode est_correcte de la classe Question

        question_correcte = Question({           # Teste le cas où la réponse utilisateur est correcte

            'question': "Combien vaudra la variable x a la fin de ce programme utilisant un test if ?\nx=10\nif x>=9:\n   x=x+5\n   if x<15:\n      x=x+3",
            'options': {"a": "10", 'b': "9", "c": "15"},
            'reponse': 'c'
        })
        question_correcte.reponse_utilisateur = 'c'
        self.assertTrue(question_correcte.est_correcte())   # Vérifie que la réponse est correcte

        question_incorrecte = Question({                    # Teste le cas où la réponse utilisateur est incorrecte
            'question': "Combien vaudra la variable x a la fin de ce programme utilisant un test if ?\nx=10\nif x>=9:\n   x=x+5\n   if x<15:\n      x=x+3",
            'options': {"a": "10", 'b': "9", "c": "15"},
            'reponse': 'c'
        })
        question_incorrecte.reponse_utilisateur = 'a'
        self.assertFalse(question_incorrecte.est_correcte()) # Vérifie que la réponse est incorrecte

    def test_lecture_fichier(self):                      #Teste la méthode lire_fichier de la classe QCM

        fichier_test = 'questions_test.json'             # Fichier de test contenant une question

        qcm = Questionnaire(fichier_test)

        questions = qcm.questions                       # Récupère les questions du Questionnaire

        self.assertEqual(len(questions), 1)     # Vérifie qu'une seule question est présente dans le fichier de test

        self.assertEqual(questions[0].enonce,           # Vérifie le contenu de la première question
                         "Combien vaut l'ensemble e3 a la fin de ce programme ?\ne1={2, 4}\ne2={0, 8, 7}\ne3=e1&e2")
        self.assertEqual(questions[0].options,
                         {"a": "{8, 2}", "b": "{1, 4}","c": "set()"})
        self.assertEqual(questions[0].reponse_correcte, "c")

if __name__ == '__main__':
    unittest.main()
