from momentJournee import MomentJournee


class LangueAnglaise:
    def bienDit(self):
        return "Well said"

    def bonjour(self, moment):
        if moment == MomentJournee.MATIN:
            return "Good Morning"
        if moment == MomentJournee.APRES_MIDI:
            return "Good Afternoon"
        if moment == MomentJournee.SOIR:
            return "Good Evening"
        if moment == MomentJournee.NUIT:
            return "Good Night"

        return "Hello"

    def auRevoir(self):
        return "Good bye"

    def __str__(self):
        return "Langue Anglaise"
