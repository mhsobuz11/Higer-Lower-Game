from fans import data
import random

def final_game():
    def formate_data(account):
        """take the account data and return the printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def chack_answer(user_guess, a_followers, b_followers):
        """take the user's guess and the followers counts and return if they got it right"""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    print("Welcome to Higher lower game. ")

    score = 0

    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {formate_data(account_a)}. ")
        print("VS")
        print(f"Against B: {formate_data(account_b)}. ")

        guess = input("Who has more followers? Type 'A' or 'B': \n").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = chack_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You are correct! Current score:{score}")
        else:
            print(f"Sorry, that's wrong. Final Score:{score}")
            game_should_continue = False
            print("\n"*20)
            final_game()
final_game()