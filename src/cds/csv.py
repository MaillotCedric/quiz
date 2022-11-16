def get_secteur(elements, secteur):
    code_secteur = elements[0]
    nom_secteur = elements[1]
    secteur["details"] = {}
    secteur["details"]["code_secteur"] = code_secteur
    secteur["details"]["nom_secteur"] = nom_secteur

def get_infos_chef_secteur(elements, secteur):
    matricule_chef_secteur = elements[2]
    nom_chef_secteur = elements[3]
    prenom_chef_secteur = elements[4]
    secteur["chef"] = {}
    secteur["chef"]["matricule"] = matricule_chef_secteur
    secteur["chef"]["nom"] = nom_chef_secteur
    secteur["chef"]["prenom"] = prenom_chef_secteur

def get_infos_collaborateur(elements, secteur):
    matricule_collaborateur = elements[5]
    nom_collaborateur = elements[6]
    prenom_collaborateur = elements[7]
    secteur["collaborateurs"].append({
        "matricule": matricule_collaborateur,
        "nom": nom_collaborateur,
        "prenom": prenom_collaborateur
    })

def get_infos_csv(reader, secteur):
    for index, row in enumerate(reader):
        elements = row[0].split(";")
        if index == 1:
            secteur["nb_secteurs"] = 1
            get_secteur(elements, secteur)
            get_infos_chef_secteur(elements, secteur)
            get_infos_collaborateur(elements, secteur)
        elif index > 1:
            code_secteur_enregistre = secteur["details"]["code_secteur"]
            code_secteur_en_cours = elements[0]

            if code_secteur_enregistre != code_secteur_en_cours and secteur["nb_secteurs"] < 2:
                secteur["nb_secteurs"] += 1

            get_infos_collaborateur(elements, secteur)

def csv_est_conforme(tableau_de_bord):
    chef_secteur_identique = tableau_de_bord[1,2,2]
    import_secteur_unique = tableau_de_bord[1,1,2]

    return import_secteur_unique and chef_secteur_identique
