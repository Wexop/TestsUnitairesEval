import os


class DetecteurPalindromme:

    def __init__(self, langue, moment):
        self.__langue = langue
        self.__moment = moment

    def detecter(self, mot):
        mirroir = mot[::-1]

        debut = self.__langue.bonjour(self.__moment) + os.linesep + mirroir
        aurevoir = os.linesep + self.__langue.auRevoir()

        if (mirroir == mot):
            return debut + os.linesep + self.__langue.bienDit() + aurevoir

        return debut + aurevoir
