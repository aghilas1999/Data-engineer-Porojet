import os

# Param Api

Path = "./data/last_processed.json"
Limit = 100
offsetlimit = 10000 


# 3 Parametres to put in the URL of the API: Max_limit, date and offset/

URL_API = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso0/records?limit={}&where=date_de_publication%20%3E%20'{}'&order_by=date_de_publication%20ASC&offset={}"
URL_API = URL_API.format(Limit, "{}","{}")


# PostrSQL Paramet 

user_name = os.getenv("Postgres_user", "localhost")
Postgres_URL = f"jdbc:postgresql://{user_name}:5432/postgres"
Postgres_Properties = {
    "user": "postrges",
    "password": "Aghilas1999.",
    "driver": "org.postgresql.Driver",
}



DB_FIELDS = [
    "reference_fiche",
    "ndeg_de_version",
    "nature_juridique_du_rappel",
    "categorie_de_produit",
    "sous_categorie_de_produit",
    "nom_de_la_marque_du_produit",
    "noms_des_modeles_ou_references",
    "identification_des_produits",
    "conditionnements",
    "date_debut_fin_de_commercialisation",
    "temperature_de_conservation",
    "marque_de_salubrite",
    "informations_complementaires",
    "zone_geographique_de_vente",
    "distributeurs",
    "motif_du_rappel",
    "risques_encourus_par_le_consommateur",
    "preconisations_sanitaires",
    "description_complementaire_du_risque",
    "conduites_a_tenir_par_le_consommateur",
    "numero_de_contact",
    "modalites_de_compensation",
    "date_de_fin_de_la_procedure_de_rappel",
    "informations_complementaires_publiques",
    "liens_vers_les_images",
    "lien_vers_la_liste_des_produits",
    "lien_vers_la_liste_des_distributeurs",
    "lien_vers_affichette_pdf",
    "lien_vers_la_fiche_rappel",
    "rappelguid",
    "date_de_publication",
]

NEW_COLUMNS = [
    "risques_pour_le_consommateur",
    "recommandations_sante",
    "date_debut_commercialisation",
    "date_fin_commercialisation",
    "informations_complementaires",
]

COLUMNS_TO_NORMALIZE = [
    "categorie_de_produit",
    "sous_categorie_de_produit",
    "nom_de_la_marque_du_produit",
    "noms_des_modeles_ou_references",
    "identification_des_produits",
    "conditionnements",
    "temperature_de_conservation",
    "zone_geographique_de_vente",
    "distributeurs",
    "motif_du_rappel",
    "numero_de_contact",
    "modalites_de_compensation",
]

COLUMNS_TO_KEEP = [
    "reference_fiche",
    "liens_vers_les_images",
    "lien_vers_la_liste_des_produits",
    "lien_vers_la_liste_des_distributeurs",
    "lien_vers_affichette_pdf",
    "lien_vers_la_fiche_rappel",
    "date_de_publication",
    "date_de_fin_de_la_procedure_de_rappel",
]
DB_FIELDS = COLUMNS_TO_KEEP + COLUMNS_TO_NORMALIZE + NEW_COLUMNS