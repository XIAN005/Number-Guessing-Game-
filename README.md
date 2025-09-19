Number Guessing Game using  Python.

Ce code Python implémente un jeu de devinettes de nombres interactif, avec des niveaux de difficulté et un classement. Voici une explication détaillée de ses fonctionnalités :
1. Gestion du temps et salutations
get_time_greetings() : Cette fonction utilise le module datetime pour obtenir l'heure actuelle. Elle renvoie "Bonjour" si l'heure est avant 18h, et "Bonsoir" sinon.
salutations(name, sexe) : Prend en argument le nom et le sexe du joueur. Elle détermine le titre ("Madame" ou "Monsieur") en fonction du sexe et retourne une salutation personnalisée combinant le message de l'heure et le titre/nom du joueur.

2. Système de score
calculate_score(difficulty, attempts_taken, max_attempts) : Calcule le score du joueur en fonction de la difficulté du jeu et du nombre d'essais utilisés.
Un score de base est attribué selon la difficulté ("facile": 1000, "moyen": 2000, "difficile": 3000).
Le score diminue à mesure que le nombre d'essais augmente, encourageant les joueurs à deviner en moins de tentatives.
Si le joueur n'a fait aucune tentative (ce cas ne devrait pas arriver dans le jeu), le score est 0.

3. Le jeu de devinettes (play_guess_game)
Configuration des difficultés : Un dictionnaire settings définit les paramètres pour chaque niveau de difficulté :
min et max : la plage de nombres à deviner.
attempts : le nombre maximal d'essais autorisés.
Initialisation du jeu :
Vérifie si la difficulté choisie est valide.
Génère un nombre target aléatoire dans la plage définie.
Initialise le compteur d'essais attempts à 0.
Affiche un message de bienvenue personnalisé, la difficulté et les règles du jeu.
Boucle de jeu :
Le jeu continue tant que le joueur a des essais restants.
Demande au joueur d'entrer sa devinette.
Gestion des entrées : Utilise un bloc try-except pour gérer les ValueError si l'entrée n'est pas un nombre entier.
Vérification de la devinette :
Si la devinette est en dehors de la plage autorisée, un message d'erreur est affiché, et l'essai est décompté, mais la boucle continue sans comparer la devinette au nombre cible.
Si la devinette est correcte (guess == target) :
Le score est calculé et affiché.
Les détails de la partie (nom, difficulté, essais, score) sont ajoutés à la liste globale leaderboard.
Le jeu se termine avec succès.
Si la devinette est trop basse ou trop haute, un indice est donné.
Affiche le nombre d'essais restants.
Fin de partie : Si le joueur épuise tous ses essais, le jeu se termine et révèle le nombre cible.

4. Classement (display_leaderboard)
Affiche le classement des joueurs.
Si le classement est vide, un message correspondant est affiché.
Trie le classement par score décroissant (reverse=True).
Affiche le rang, le nom du joueur, la difficulté, le nombre d'essais et le score pour chaque entrée.

5. Boucle principale du programme (if __name__ == "__main__":)
Saisie des informations du joueur : Demande le nom et le sexe du joueur. Une boucle while assure que le sexe est "F" ou "H".
Menu principal : Présente un menu au joueur avec les options : "Jouer une partie", "Voir le classement", "Quitter".
Gestion du choix de l'utilisateur :
Choix 1 (Jouer une partie) : Demande la difficulté du jeu et lance play_guess_game(). Une boucle while assure que la difficulté choisie est valide.
Choix 2 (Voir le classement) : Appelle display_leaderboard().
Choix 3 (Quitter) : Affiche un message d'adieu et termine le programme (break).
Choix invalide : Informe l'utilisateur d'un choix incorrect.
