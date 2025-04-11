import random


def RPS_game():
    comp_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Choose rock, paper, or scissors: ")
    if not (is_legal(player_choice)):
        print("You must select from rock, paper, or scissors")
    else:
        print("The computer chose", comp_choice)
        if beats(player_choice, comp_choice):
            print("You win!")
        elif beats(comp_choice, player_choice):
            print("You lost. :(")
        else:
            print("It's a tie.")


def is_legal(choice: str) -> bool:
    """
    Checks if a player's weapon choice is legal

    Args:
        choice (str): The weapon chosen by a player (rock, paper, or scissors).

    Returns:
        bool: True if the choice is legal; False otherwise.
    """
    return choice in ["rock", "paper", "scissors"]


def beats(weapon_one: str, weapon_two: str) -> bool:
    """
    Determine if the first player's weapon beats the second player's weapon in Rock, Paper, Scissors.

    Args:
        weapon_one (str): The weapon chosen by the first player.
        weapon_two (str): The weapon chosen by the second player.

    Returns:
        bool: True if the first player's weapon beats the second player's weapon; False otherwise.
    """
    # Rock beats scissors, scissors beat paper, paper beats rock
    return (
            (weapon_one == "rock" and weapon_two == "scissors") or
            (weapon_one == "scissors" and weapon_two == "paper") or
            (weapon_one == "paper" and weapon_two == "rock")
    )


# Usage:
if __name__ == "__main__":
    RPS_game()
