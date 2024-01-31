import os
import unittest

from src.detecteurPalindrome import DetecteurPalindromme
from utilities.detecteurPalindrommeBuilder import DetecteurPalindrommeBuilder

testNonPalindrome = ["maison", "truc", "ceiling-shot", "flip-rest"]


class TestPalindrome(unittest.TestCase):
    def testMirroir(self):
        for mot in testNonPalindrome:
            with(self.subTest(mot)):
                detecteur = DetecteurPalindrommeBuilder().build()
                resultat = detecteur.detecter(mot)

                attendu = mot[::-1]
                self.assertIn(attendu, resultat)

    def testBienDit(self):
        palindrome = 'kayak'

        detecteur = DetecteurPalindromme()
        resultat = detecteur.detecter(palindrome)

        attendu = palindrome + os.linesep + "Bien dit"
        self.assertIn(attendu, resultat)

    def testBonjour(self):
        mot = 'truc'

        detecteur = DetecteurPalindromme()
        resultat = detecteur.detecter(mot)

        premiereLigne = resultat.split(os.linesep)[0]
        self.assertEqual("Bonjour", premiereLigne)

    def testAuRevoir(self):
        mot = 'truc'

        detecteur = DetecteurPalindromme()
        resultat = detecteur.detecter(mot)

        premiereLigne = resultat.split(os.linesep)[-1]
        self.assertEqual("Au revoir", premiereLigne)
