import os
import unittest

from LangueAnglaise import LangueAnglaise
from LangueFrancaise import LangueFrancaise
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

        cas = [[LangueFrancaise(), "Bien dit"], [LangueAnglaise(), "Well said"]]

        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).build()
                resultat = detecteur.detecter(palindrome)

                bienDit = param[1]

                attendu = palindrome + os.linesep + bienDit
                self.assertIn(attendu, resultat)

    def testBonjour(self):
        mot = 'truc'

        cas = [
            [LangueFrancaise(), 'Bonjour', MomentDeLaJournée.INCONNU],
            [LangueFrancaise(), 'Bonjour', MomentDeLaJournée.MATIN],
            [LangueFrancaise(), 'Bonjour', MomentDeLaJournée.APRES_MIDI],
            [LangueFrancaise(), 'Bonsoir', MomentDeLaJournée.SOIR],
            [LangueFrancaise(), 'Bonsoir', MomentDeLaJournée.NUIT],
            [LangueAnglaise(), 'Hello', MomentDeLaJournée.INCONNU],
            [LangueAnglaise(), 'Good Morning', MomentDeLaJournée.MATIN],
            [LangueAnglaise(), 'Good Afternoon', MomentDeLaJournée.APRES_MIDI],
            [LangueAnglaise(), 'Good Evening', MomentDeLaJournée.SOIR],
            [LangueAnglaise(), 'Good Night', MomentDeLaJournée.NUIT],
        ]
        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                moment = param[2]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).ayantPourMoment(moment).build()
                resultat = detecteur.detecter(palindrome)

                premiereLigne = resultat.split(os.linesep)[0]
                self.assertEqual(param[1], premiereLigne)

    def testAuRevoir(self):
        mot = 'truc'

        cas = [[LangueFrancaise(), "Au revoir"], [LangueAnglaise(), "Good bye"]]
        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).build()
                resultat = detecteur.detecter(palindrome)

                derniereLigne = resultat.split(os.linesep)[-1]
                self.assertEqual(param[1], derniereLigne)
