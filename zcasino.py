# This project is a small gambling game in french.

import math
import random

STARTING_MONEY = 50 # the money the player is starting with


def game():
    print("Bienvenue dans le ZCasino !\n")

    player_money = STARTING_MONEY

    want_to_play = want_to_play_question(player_money)

    while want_to_play and player_money > 0:
        gain = gamble(player_money)
        player_money += gain

        if player_money > 0:
            want_to_play = want_to_play_question(player_money)
        else:
            print("Vous n'avez plus d'argent.")    
    
    end_of_game(player_money)


def gamble(player_money):
    bet = get_player_bet(player_money)
    player_number = get_player_number()

    print("Les jeux sont faits. La roue tourne.")
    bank_number = roll()
    print("La bille tombe sur le numéro", bank_number, ".")

    if player_number == bank_number:
        print("Vous avez trouvé le bon numéro ! Vous avez gagné trois fois votre mise !")
        gain = get_full_prize(player_money)
    elif player_number % 2 == bank_number % 2:
        print("Votre numéro a la même parité que celui de la banque. Vous gagnez la moitié de votre mise.")
        gain = get_half_prize(player_money)
    else:
        print("Vous avez perdu votre mise.")
        gain = -bet

    return gain


def get_player_bet(player_money):
    input_ok = False
    while not input_ok:
        bet_text = input("Combien voulez-vous miser ? ")

        try:
            bet = int(bet_text)
        except:
            print("Vous devez saisir un nombre.")
        else:
            if bet < 0:
                print("Vous ne pouvez pas miser un montant négatif.")
            elif bet > player_money:
                print("Vous ne pouvez miser que l'argent que vous possédez.")
            else:
                print("Vous misez", bet, "$.")
                input_ok = True

    return bet


def get_player_number():
    input_ok = False
    while not input_ok:
        number_text = input("Sur quel nombre voulez-vous miser ? ")

        try:
            number = int(number_text)
        except:
            print("Vous devez saisir un nombre.")
        else:
            if number < 0:
                print("Vous ne pouvez pas miser sur un nombre négatif.")
            elif number > 49:
                print("Vous ne pouvez pas miser sur un nombre supérieur à 49.")
            else:
                print("Vous misez sur le numéro", number, ".")
                input_ok = True

    return number


def want_to_play_question(player_money):
    print("Vous avez", player_money, "$ en poche.")
    answer_ok = False
    while not answer_ok:
        answer = input("Voulez-vous jouer ? (oui/non) ")
        if answer == "oui":
            return True
        elif answer == "non":
            return False
        else:
            print("Votre réponse", answer, """n'est pas correcte. Saisissez "oui" ou "non".""")


def roll():
    return random.randrange(50)


def get_half_prize(bet):
    return math.ceil(bet / 2)


def get_full_prize(bet):
    return 3 * bet


def end_of_game(player_money):
    if player_money > STARTING_MONEY:
        print("Vous avez gagné", player_money - STARTING_MONEY, "$.")
    elif player_money == STARTING_MONEY:
        print("Vous n'avez rien gagné.")
    elif player_money > 0:
        print("Vous avez perdu", STARTING_MONEY - player_money, "$.")
    else:
        print("Vous avez tout perdu.")


if __name__ == "__main__":
    game()
