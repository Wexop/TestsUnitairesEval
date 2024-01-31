from momentJournee import MomentJournee


class LangueFrancaise:
    def bienDit(self):
        return "Bien dit"

    def bonjour(self, moment):
        if moment == MomentJournee.SOIR or moment == MomentJournee.NUIT:
            return "Bonsoir"
        return "Bonjour"

    def auRevoir(self):
        return "Au revoir"

    def __str__(self):
        return "Langue Francaise"
