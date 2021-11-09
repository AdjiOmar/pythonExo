"""
Class Personne
"""


class Personne:
    """Les informations d'une personne"""
    def __init__(self, prenom, nom, adresse, telephone, date_naissance,
                 lieu_naissance, nationalite, pays, email, genre ):
        self.prenom = prenom
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.date_naissance = date_naissance
        self.lieu_naissance = lieu_naissance
        self.nationalite = nationalite
        self.pays = pays
        self.email = email
        self.genre = genre

    def __str__(self):
        return f"Prenom: {self.prenom}\nNom: {self.nom}\nAdresse: {self.adresse}\nTelephone: {self.telephone}\n"\
               f"Date de naissance: {self.date_naissance}\nLieu de naissance: {self.lieu_naissance}\n" \
               f"nationalite: {self.nationalite}\nPays: {self.pays}\nEmail: {self.email}\nGenre: {self.genre}"



if __name__ == "__main__":
        personne = Personne("Adji ngone","Ndiaye", "Gueule tappe", "77 825 36 18", "27 janvier 1997", "Dakar", "Senegalaise", "Senegal", "ngone227@gmail.com", "Feminin" )
        print(personne)


