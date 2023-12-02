# Ex.4.14-4.17.py

"""Computer Assisted Instruction program"""

import random


def number_gen(difficulty):
    """This functions generates a number depending on what difficult
    level you've chosen"""

    if difficulty == 1:

        number1 = random.randrange(1, 9)
        number2 = random.randrange(1, 9)

        return (number1, number2)

    elif difficulty == 2:

        number1 = random.randrange(0, 99)
        number2 = random.randrange(0, 9)

        return (number1, number2)


def pos_response():
    """Makes a random positive response to your answer"""

    responses_pos = ["Very good!", "Keep up the good work!", "Nice work!"]

    print(random.choice(responses_pos))


def neg_response():
    """Makes a random negative response to your answer"""

    responses_neg = ["No. Please try again.", "Wrong. Try once more.", "No. Keep trying"]

    print(random.choice(responses_neg))


def math_op(x, number1, number2):
    """Calculates the results depending on what game mode is chosen
    and handles if division by 0 occurs"""

    result = 0

    if x == 1:

        result = number1 + number2

    if x == 2:

        result = number1 - number2

    if x == 3:

        result = number1 * number2

    if x == 4:

        if number2 == 0:

            number2 += 1
            result = round(number1 / number2, 2)

        else:

            result = round(number1 / number2, 2)

    return (result)


def text(x, number1, number2):
    """Asks a math question depending on what game mode
    the user has chosen"""

    answer = None

    if x == 1:

        answer = float(input(f'what is {number1} + {number2}?,'
                             f' 0.001 to go back to menu '))

    if x == 2:

        answer = float(input(f'what is {number1} - {number2}?,'
                             f' 0.001 to go back to menu '))

    if x == 3:

        answer = float(input(f'what is {number1} * {number2}?,'
                             f' 0.001 to go back to menu '))

    if x == 4:

        if number2 == 0:

            number2 += 1

            answer = float(input(f'what is {number1} / {number2}?,'
                                 f' 0.001 to go back to menu '))

        else:

            answer = float(input(f'what is {number1} / {number2}?,'
                                 f' 0.001 to go back to menu '))

    return (answer)


def question_dif():
    """Asks what difficulty you wanna play and returns that answer"""

    difficulty = int(input("What difficulty do you wanna play on?\n"
                           "1 for single digit integers and 2 for up to 2 digit integers "))

    return (difficulty)


def question_mode():
    """Asks what game mode you wanna play and returns that answer"""

    game_mode = float(input('What game mode do you want to play? 1 for addition,'
                            ' 2 for subtraction,\n3 for multiplication, 4 for division,'
                            ' 5 for random mixture or -1 to exit '))

    return (game_mode)


def main():
    """Creates a game loop that lets the user return to the menu
     when he wants"""

    while True:

        difficulty = question_dif()

        game_mode = question_mode()

        if game_mode == -1:
            print('You quit the game')

            break

        if game_mode == 0:
            continue

        if game_mode == 5:
            game_mode = random.randint(1, 4)

        number1, number2 = number_gen(difficulty)

        result = math_op(game_mode, number1, number2)

        answer = text(game_mode, number1, number2)

        if answer == 0.001:

            continue

        while True:

            if answer != result:

                neg_response()

                answer = text(game_mode, number1, number2)

                if answer == 0.001:

                    break

            elif answer == result:

                pos_response()

                break


if __name__ == "__main__":
    main()