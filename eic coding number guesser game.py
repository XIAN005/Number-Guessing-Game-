import random
from datetime import datetime  

leaderboard = []

def get_time_greetings ():
    current_hour = datetime.now().hour
    if datetime.now().hour < 18 :
        return "Bonjour"
    else :
        return "Bonsoir"
    
def salutations ( name , sexe ) :
    if sexe.lower() == "f" :
         title = "Madame"
    else :
         title = "Monsieur"
        
    return f"{get_time_greetings()}{title}{name}"
      
def calculate_score(difficulty, attempts_taken, max_attempts):
    base_score = {"facile": 1000, "moyen": 2000, "difficile": 3000}
    if attempts_taken == 0:
        return 0
    return int(base_score[difficulty] * (1 - (attempts_taken - 1) / max_attempts))

def play_guess_game( name , sexe , difficulty ):
   settings = {
      "facile": { "min":1 , "max":100 ,"attempts" : 10} ,
      "moyen":{"min": 1 ,"max": 100 , "attempts":7} ,
      "difficile":{"min":1 , "max": 200 , "attempts": 5},
      
    }

   if difficulty not in settings:
        print("Difficulté non valide. Veuillez choisir 'facile', 'moyen' ou 'difficile'.")
        return False

   min_num = settings[difficulty]["min"]
   max_num = settings[difficulty]["max"]
   max_attempts = settings[difficulty]["attempts"]

   target = random.randint(min_num, max_num)
   attempts = 0
   print(f"\n{salutations(name, sexe)}, bienvenue au jeu de devinettes !")
   print(f"Niveau : {difficulty.capitalize()}")
   print(f"Devinez un nombre entre {min_num} et {max_num}. Vous avez {max_attempts} essais.")

   while attempts < max_attempts:
     try:
            guess = int(input("Entrez votre devinette : "))
            attempts += 1 

            if guess < min_num or guess > max_num:
                print(f"Veuillez entrer un nombre entre {min_num} et {max_num}.")
                print(f"Essais restants : {max_attempts - attempts}")

                continue

               
            if guess == target:
                score = calculate_score(difficulty, attempts, max_attempts)
                print(f"Félicitations ! Vous avez deviné en {attempts} essais. Votre score : {score}")

                leaderboard.append({"name": name, "difficulty": difficulty, "attempts": attempts, "score": score})
                return True
            
            elif guess < target:
                print("Trop bas ! Essayez un nombre plus grand.")

            else:
                 print("Trop haut ! Essayez un nombre plus petit.")

            
            if attempts < max_attempts:
                 print(f"Essais restants : {max_attempts - attempts}")

     except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

   print(f"\nDésolé, vous n'avez plus d'essais. Le nombre était {target}.")
   return False 

def display_leaderboard ():
    if not leaderboard :
        print("\nLe classement est vide pour le moment.")
        return
    
    print("\n----- CLASSEMENT -----")
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)

    for i, entry in enumerate(sorted_leaderboard):
        print(f"{i+1}. Joueur: {entry['name']} | Difficulté: {entry['difficulty'].capitalize()} | Essais: {entry['attempts']} | Score: {entry['score']}")
    print("----------------------")




if __name__ == "__main__":
    player_name = input("Entrez votre nom : ")
    player_sexe = ""
    while player_sexe.lower() not in ["f", "h"]:
        player_sexe = input("Entrez votre sexe (F pour féminin, H pour masculin) : ")
        if player_sexe.lower() not in ["f", "h"]:
            print("Sexe invalide. Veuillez entrer 'F' ou 'H'.")

while True:
     print("\n--- Menu ---")
     print("1. Jouer une partie")
     print("2. Voir le classement")
     print("3. Quitter")
        

     choice = input("Votre choix : ")

     if choice == '1':
            chosen_difficulty = ""
            while chosen_difficulty.lower() not in ["facile", "moyen", "difficile"]:
                chosen_difficulty = input("Choisissez la difficulté (facile, moyen, difficile) : ")
                if chosen_difficulty.lower() not in ["facile", "moyen", "difficile"]:
                    print("Difficulté invalide. Veuillez choisir 'facile', 'moyen' ou 'difficile'.")
            
            play_guess_game(player_name, player_sexe, chosen_difficulty.lower())
     elif choice == '2':
            display_leaderboard()
     elif choice == '3':
            print(f"Au revoir {player_name} ! Merci d'avoir joué.")
            break
     else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")



