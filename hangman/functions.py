# this files contains utility functions for the pendu.py file

import data
import random
import pickle


def game():
    scores = load_scores(data.SCORES_FILE_NAME)
    player_name = get_player_name()
    print("Bonjour {}.".format(player_name))
    player_score = get_player_score(scores, player_name)
    print("Votre score actuel est de {}.".format(player_score))
    scores[player_name] = main_loop(player_score)
    save_scores(data.SCORES_FILE_NAME, scores)


def load_scores(filename):
    try:
        with open(filename, 'rb') as scores_file:
            return pickle.Unpickler(scores_file).load()
    except OSError:
        print("Le fichier \"{}\" n'existe pas.".format(filename))
        return dict()


def get_player_name():
    return input("Veuillez saisir votre nom s'il vous plait : ")


def get_player_score(scores, name):
    try:
        return scores[name]
    except:
        return 0


def main_loop(player_score):
    continue_game = True
    while continue_game:
        tries_left, word_to_find = initialize_game()
        print("L'ordinateur a choisi le mot \"{}\".".format(word_to_find)) # disable this before release
        print("Vous avez droit à {} essais.".format(tries_left))
        masked_word = "*" * len(word_to_find)
        player_score = guess_word_loop(masked_word, word_to_find, tries_left, player_score)
        if not player_wants_to_continue():
            continue_game = False
    return player_score


def save_scores(filename, scores):
    with open(filename, 'wb') as scores_file:
        pickle.Pickler(scores_file).dump(scores)


def initialize_game():
        return data.MAX_TRIES, random.choice(data.word_list)


def guess_word_loop(masked_word, word_to_find, tries_left, player_score):
    while "*" in masked_word and tries_left > 0:
        print("Mot à deviner : {}".format(masked_word))
        letter = get_player_letter()
        print("Vous avez saisi la lettre \"{}\"".format(letter))

        if letter in word_to_find:
            print("La lettre \"{}\" se trouve dans le mot à deviner.".format(letter))
            masked_word = update_masked_word(letter, masked_word, word_to_find)
        else:
            print("La lettre \"{}\" ne se trouve pas dans le mot à deviner.".format(letter))
            tries_left -= 1
            print("Le nombre d'essais diminue.")
            
        print("Il vous reste {} essais.".format(tries_left))
        
    if tries_left > 0:
        assert masked_word == word_to_find, "Le mot découvert est censé être identique à celui à trouver."
        print("Bravo ! Vous avez trouvé le mot \"{}\".".format(word_to_find))
    else:
        print("Perdu ! Le mot à trouver était \"{}\".".format(word_to_find))
    
    return player_score + tries_left


def player_wants_to_continue():
    answer = input("Voulez vous continuer à jouer ? (oui / non) ")
    return answer == "oui"


def get_player_letter():
    letter = input("Saisissez une lettre (une seule, sans accent) : ")
    assert len(letter) == 1, "Vous avez saisi plus d'un caractère."
    assert letter.isalpha(), "Vous n'avez pas saisi une lettre."
    return letter.lower()


def update_masked_word(player_letter, masked_word, word_to_find):
    letter_list = list(masked_word)
    for index, current_letter in enumerate(word_to_find):
        if player_letter == current_letter:
            letter_list[index] = player_letter
    return ''.join(letter_list)
