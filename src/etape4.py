import locale
import time

from momentJournee import MomentJournee
from LangueAnglaise import LangueAnglaise
from LangueFrancaise import LangueFrancaise
from detecteurPalindrome import DetecteurPalindromme


class Etape4:

    def __init__(self):
        self.__lang = LangueAnglaise()
        if locale.getdefaultlocale()[0] == 'fr_FR':
            self.__lang = LangueFrancaise()

        hour = time.localtime().tm_hour
        self.__moment = MomentJournee.INCONNU
        if 6 <= hour <= 12:
            self.__moment = MomentJournee.MATIN
        elif 13 <= hour <= 17:
            self.__moment = MomentJournee.APRES_MIDI
        elif 18 <= hour <= 23:
            self.__moment = MomentJournee.SOIR
        else:
            self.__moment = MomentJournee.NUIT


        print(self.__lang, self.__moment)

    def detecter(self):
        mot = input("Choisir un mot : ")
        detecteur = DetecteurPalindromme(self.__lang, self.__moment)
        return detecteur.detecter(mot)


etap4 = Etape4()
print(etap4.detecter())