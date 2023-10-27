import unittest
import string
from Password_testing import password_testing
from mdp_generator import mdpGenerator

class TestPasswordStrength(unittest.TestCase):

    def setUp(self):
        self.tester = password_testing()

    def test_weak_password(self):
        force, _ = self.tester.calcul_strength("password")
        self.assertEqual(force, "La force du mot de passe est très faible")

    def test_medium_password(self):
        force, _ = self.tester.calcul_strength("Passord1995%")
        self.assertEqual(force, "La force du mot de passe est moyenne")

    def test_strong_password(self):
        force, _ = self.tester.calcul_strength("P@19995ss%ord")
        self.assertEqual(force, "La force du mot de passe est forte")

class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = mdpGenerator()

    def test_password_length(self):
        password, _, _ = self.generator.generate_mdp(4, 4, 4, 4)
        self.assertEqual(len(password), 16)

    def test_no_special_chars(self):
        password, _, _ = self.generator.generate_mdp(4, 4, 4, 0)
        self.assertFalse(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()
