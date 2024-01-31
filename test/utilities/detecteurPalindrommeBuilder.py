from src.detecteurPalindrome import DetecteurPalindromme
from utilities.LangueStub import LangueStub


class DetecteurPalindrommeBuilder:
    __langue = LangueStub()

    def build(self):
        return DetecteurPalindromme(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self
