import os


class DetecteurPalindromme:

    def __init__(self, langue):
        self.__langue = langue

    def detecter(self, mot):
        mirroir = mot[::-1]

        debut = "Bonjour" + os.linesep + mirroir
        aurevoir = os.linesep + "Au revoir"

        print(debut + os.linesep + self.__langue.bienDit() + aurevoir)

        if (mirroir == mot):
            return debut + os.linesep + self.__langue.bienDit() + aurevoir

        return debut + aurevoir
