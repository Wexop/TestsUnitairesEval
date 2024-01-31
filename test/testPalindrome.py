import os
import unittest

from src.detecteurPalindrome import DetecteurPalindromme

testNonPalindrome = ["maison", "truc", "ceiling-shot", "flip-rest"]


class TestPalindrome(unittest.TestCase):
    def testMirroir(self):
        for mot in testNonPalindrome:
            with(self.subTest(mot)):
                detecteur = DetecteurPalindromme()
                resultat = detecteur.detecter(mot)

                attendu = mot[::-1]
                self.assertEquals(attendu, resultat)

    def testBienDit(self):
        palindrome = 'kayak'

        detecteur = DetecteurPalindromme()
        resultat = detecteur.detecter(palindrome)

        attendu = palindrome + os.linesep + "Bien dit"
        self.assertIn(attendu, resultat)
