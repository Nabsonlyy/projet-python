from bipede import Bipede


class Humain(Bipede):
    nom = ""
    prenom = ""
    taille = 0
    sexe = ""
    couleur_de_peau = ""
    nationalite = ""

    def __init__(self, nom, prenom, taille, sexe, couleur_de_peau, nationalite):
        self.nom = nom
        self.prenom = prenom
        self.taille = taille
        self.sexe = sexe
        self.couleur_de_peau = couleur_de_peau
        self.nationalite = nationalite

    # <editor-fold desc="Getters">

    def get_nom(self):
        pass

    def get_prenom(self):
        pass

    def get_taille(self):
        pass

    def get_sexe(self):
        pass

    def get_couleur_de_peau(self):
        pass

    def get_nationalite(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Setters">

    def set_nom(self, nom):
        pass

    def set_prenom(self, prenom):
        pass

    def set_taille(self, taille):
        pass

    def set_sexe(self, sexe):
        pass

    def set_couleur_de_peau(self, couleur_de_peau):
        pass

    def set_nationalite(self, nationalite):
        pass

    # </editor-fold>

    def communiquer(self):
        print("Je communique dans la langue: " + self.nationalite)

    def marcher(self):
        print("Je marche tel l'humain que je suis")
