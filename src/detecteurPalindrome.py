import os


class DetecteurPalindromme:

    def __init__(self, langue):
        self.__langue = langue

    def detecter(self, mot):
        mirroir = mot[::-1]

        debut = self.__langue.bonjour() + os.linesep + mirroir
        aurevoir = os.linesep + self.__langue.auRevoir()

        if (mirroir == mot):
            return debut + os.linesep + self.__langue.bienDit() + aurevoir

        return debut + aurevoir
