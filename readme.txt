                                   ************  YOUTUBE DEV *************


               

            I- Installation de l'environnement
 
* VueJS
    - Installer node.js 
    - Executer dans le terminal les commandes
        > npm install -g @vue/cli
        > npm update -g @vue/cli

* FastApi
    - Installer une version de python supérieure à 3.0
    - Lancer le terminal 
    - Se placer dans le dossier /backend/
    - Executer la commande
        > pip install -r requirements.txt


 
            II- Lancement

* VueJs

L'excecution de notre code VueJs se fait comme suit:
    - Lancer le terminal 
    - Se placer dans le dossier /frontend/
    - Executer la commande
        > npm run serve
    - Coller l'url http://localhost:8080/ dans votre navigateur web, puis appuyer sur entrée pour ouvrir votre site

* FastApi
    - Lancer le terminal 
    - Se placer dans le dossier /backend/
    - Executer la commande
        > uvicorn main:app --reload          


            III- Test
                1- Inscription  
                    - Dans la barre de navigation, taper sur le lien s'inscrire
                    - Choisir dans la barre des onglets en haut à gauche le type de compte souhaité
                    - Remplir les champs de formulaire puis taper sur Valider

                2- Connexion
                    - Cliquer dans la barre de navigation sur le lien Se connecter
                    - Entrer les informations de connexion
                    - La redirection vers une page est effectuée en fonction du type de compte correspondant
                    (Les pages expert et admin sont actuellement non abouties)

                3- Insertion d'un syllabus
                    (Fonctionnalité non aboutie)

                4- Consultation d'une formation
                    (Fonctionnalité non aboutie)
