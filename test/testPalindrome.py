import os
import unittest

from LangueAnglaise import LangueAnglaise
from LangueFrancaise import LangueFrancaise
from momentJournee import MomentJournee
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

        cas = [
            [LangueFrancaise(), 'Bonjour', MomentJournee.INCONNU],
            [LangueFrancaise(), 'Bonjour', MomentJournee.MATIN],
            [LangueFrancaise(), 'Bonjour', MomentJournee.APRES_MIDI],
            [LangueFrancaise(), 'Bonsoir', MomentJournee.SOIR],
            [LangueFrancaise(), 'Bonsoir', MomentJournee.NUIT],
            [LangueAnglaise(), 'Hello', MomentJournee.INCONNU],
            [LangueAnglaise(), 'Good Morning', MomentJournee.MATIN],
            [LangueAnglaise(), 'Good Afternoon', MomentJournee.APRES_MIDI],
            [LangueAnglaise(), 'Good Evening', MomentJournee.SOIR],
            [LangueAnglaise(), 'Good Night', MomentJournee.NUIT],
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

        cas = [
            [LangueFrancaise(), 'Au revoir', MomentJournee.INCONNU],
            [LangueFrancaise(), 'Bonne journée', MomentJournee.MATIN],
            [LangueFrancaise(), 'Bon après midi', MomentJournee.APRES_MIDI],
            [LangueFrancaise(), 'Bonne soirée', MomentJournee.SOIR],
            [LangueFrancaise(), 'Bonne nuit', MomentJournee.NUIT],
            [LangueAnglaise(), 'Good bye', MomentJournee.INCONNU],
            [LangueAnglaise(), 'Good bye am', MomentJournee.MATIN],
            [LangueAnglaise(), 'Good bye pm', MomentJournee.APRES_MIDI],
            [LangueAnglaise(), 'Good bye soir', MomentJournee.SOIR],
            [LangueAnglaise(), 'Good bye nuit', MomentJournee.NUIT],
        ]

        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                moment = param[2]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).ayantPourMoment(moment).build()
                resultat = detecteur.detecter(palindrome)

                derniereLigne = resultat.split(os.linesep)[-1]
                self.assertEqual(param[1], derniereLigne)
