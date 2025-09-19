import random

choices = ["heads", 'tails']
rounds = 5
player1_score = 0
player2_score = 0
player1 = input("Enter player1 name : ")
player2 = input("Enter player2 name : ")
print("\n")


def coin_toss(player1_score, player2_score):
    print("Coin Toss Game")

    player_call = player1
    for round in range(1, rounds+1):
        print(f"\nThis is round {round}")

        if round % 2 == 0:
            player_call = player1
        else:
            player_call = player2

        print(f"\n{player_call}, will call heads or tails")

        player_input = input(f"\n{player_call} choose heads or tails : ")
        print(f"{player_call} has chose {player_input}")

        toss_result = random.choices

        if toss_result == player_input:
            player1_score += 1
            print(f"\nThis round winner is {player1}")
        else:
            player2_score += 1
            print(f"\nThis round winner is {player2}")


coin_toss(player1_score, player2_score)

if player1_score == player2:
    print("\nMatch is draw!")
elif player1_score > player2_score:
    print(f"\n{player1} is overall winner!!!")
else:
    print(f"\n{player2} is overall winner!!")
