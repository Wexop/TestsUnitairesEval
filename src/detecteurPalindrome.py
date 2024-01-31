import os


class DetecteurPalindromme:
    def detecter(self, mot):
        mirroir = mot[::-1]

        debut = "Bonjour" + os.linesep + mirroir + os.linesep
        aurevoir = os.linesep + "Au revoir"

        if (mirroir == mot):
            return debut + mirroir + os.linesep + "Bien dit" + aurevoir

        return debut + mirroir + aurevoir
