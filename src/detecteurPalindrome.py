import os


class DetecteurPalindromme:
    def detecter(self, mot):
        mirroir = mot[::-1]

        if (mirroir == mot):
            return mirroir + os.linesep + "Bien dit"

        return mirroir
