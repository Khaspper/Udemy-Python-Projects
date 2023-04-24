import game_data
import art
import random

#TODO: Check update score

def choose_person():
    person = random.randint(0, len(game_data.data) - 1)
    return person

def update_score(choice):
    if choice == 'A':
        if game_data.data[person_A]["follower_count"] > game_data.data[person_B]["follower_count"]:
            return True
        else:
            return False
    elif choice == 'B':
        if game_data.data[person_A]["follower_count"] < game_data.data[person_B]["follower_count"]:
            return True
        else:
            return False

def run_game():
    global players_score, person_A, person_B
    print(f'Compare A: {game_data.data[person_A]["name"]}, a {game_data.data[person_A]["description"]}, from {game_data.data[person_A]["country"]}.')

    print(art.vs)

    print(f'Against B: {game_data.data[person_B]["name"]}, a {game_data.data[person_B]["description"]}from {game_data.data[person_B]["country"]}.')
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if update_score(choice.upper()) == True:
        players_score += 1
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(art.logo)
        print(f"You're right! Current score: {players_score}.")
        person_A = person_B
        person_B = choose_person()
        run_game()
    else:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {players_score}")


players_score = 0
person_A = choose_person()
person_B = choose_person()

while person_B == person_A:
    person_B = choose_person()

print(art.logo)
run_game()
