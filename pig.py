import random
import time


class Player:
    player_score = 0
    turn_total = 0

    def __init__(self, pos, turn):
        self.pos = pos
        self.turn = turn

    def get_score(self):
        return player_score

    def switch_turn(self):
        if self.turn is True:
            self.turn = False
        else:
            self.turn = True

    def get_turn(self):
        return self.turn


class ComputerPlayer(Player):
    def __init__(self, pos, turn):
        super().__init__(pos, turn)
        turn = 0
        roll = 0

    def strategy(self):
        print("\n")
        print(f"Player {self.pos}'s turn")
        print(f"Score: {self.player_score}")
        print(f"Turn Total: {self.turn_total}")
        time.sleep(1)
        if 25 <= 100 - self.player_score:
            while self.turn_total < 25:
                roll = die_roll()
                print(f"You rolled: {roll}")
                time.sleep(0.5)
                if roll == 1:
                    self.turn_total = 0
                    break
                else:
                    self.turn_total += roll
                    print("\n")
                    print(f"Player {self.pos}'s turn")
                    print(f"Score: {self.player_score}")
                    print(f"Turn Total: {self.turn_total}")
                    time.sleep(1.5)

        elif 100 - self.player_score <= 25:
            while self.turn_total < 100 - self.player_score:
                roll = die_roll()
                print(f"You rolled: {roll}")
                time.sleep(0.5)
                if roll == 1:
                    self.turn_total = 0
                    break
                else:
                    self.turn_total += roll
                    print("\n")
                    print(f"Player {self.pos}'s turn")
                    print(f"Score: {self.player_score}")
                    print(f"Turn Total: {self.turn_total}")
                    time.sleep(2)
        self.player_score += self.turn_total
        self.turn_total = 0


def intro():
    print("Welcome")
    while True:
        p1 = input("Is Player 1 a human or a computer? ")
        if p1 == "human" or p1 == "computer":
            break
        else:
            print("Invalid input. Please try again")
    while True:
        p2 = input("Is Player 2 a human or a computer? ")
        if p2 == "human" or p2 == "computer":
            break
        else:
            print("Invalid input. Please try again")
    while True:
        time_toggle = input("Timed game (Y/N)? ")
        if time_toggle == "Y" or time_toggle.upper() == "Y":
            while True:
                sec = input("Enter time limit in seconds: ")
                if sec.isdigit() == True:
                    sec = int(sec)
                    print('\n')
                    timed_pig_game_proxy(p1, p2, sec)
                    break
            break
        elif time_toggle == "N" or time_toggle.upper() == "N":
            print('\n')
            pig_game(p1, p2)
            break
        else:
            print("Invalid input. Please try again")


def die_roll():
    die = random.randrange(1, 7)
    return die


def new_game():
    pig_run = 0
    while pig_run == 0:
        new_game = input("Would you like to play again (Y/N)? ")
        if new_game == 'Y' or new_game.upper() == 'Y':
            print("\n")
            intro()
        elif new_game == 'N' or new_game.upper() == 'N':
            pig_run = 1
        else:
            print("\nINVALID INPUT\n")


def timed_pig_game_proxy(player1, player2, timed):
    random.seed(0)
    new_line = '\n'
    roll = 0
    end = 0
    if player1 == "human" and player2 == "human":
        p1 = Player(1, False)
        p2 = Player(2, False)
        print('Welcome to The Game of Pig (TIMED).')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        end = int(time.time()) + timed
        while p1.player_score < 100 and p2.player_score < 100 and int(time.time()) < end:

            # p1 human turn
            while p1.get_turn() is True:
                print("\nPlayer 1's turn")
                print(f"Score: {p1.player_score}{new_line}Turn Total: {p1.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p1.turn_total = 0
                        p2.switch_turn()
                        p1.switch_turn()
                    else:
                        p1.turn_total += roll
                    if p1.turn_total + p1.player_score >= 100:
                        p1.player_score += p1.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p1.player_score += p1.turn_total
                    p1.turn_total = 0
                    p2.switch_turn()
                    p1.switch_turn()
                else:
                    print("\n---INVALID INPUT---")
            if p1.player_score >= 100:
                break

            # p2 human turn
            while p2.get_turn() is True:
                print("\nPlayer 2's turn")
                print(f"Score: {p2.player_score}{new_line}Turn Total: {p2.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p2.turn_total = 0
                        p1.switch_turn()
                        p2.switch_turn()
                    else:
                        p2.turn_total += roll
                    if p2.turn_total + p2.player_score >= 100:
                        p2.player_score += p2.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p2.player_score += p2.turn_total
                    p2.turn_total = 0
                    p1.switch_turn()
                    p2.switch_turn()
                else:
                    print("\nINVALID INPUT\n")

        # Winner confirmation
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    # comp vs human
    elif player1 == "computer" and player2 == "human":
        p1 = ComputerPlayer(1, False)
        p2 = Player(2, False)
        print('Welcome to The Game of Pig. (TIMED)')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        end = int(time.time()) + timed
        while p1.player_score < 100 and p2.player_score < 100 and int(time.time()) < end:
            # p1 computer turn
            while p1.get_turn() is True:
                p1.strategy()
                p2.switch_turn()
                p1.switch_turn()
            if p1.player_score >= 100:
                break

            # p2 human turn
            while p2.get_turn() is True:
                print("\nPlayer 2's turn")
                print(f"Score: {p2.player_score}{new_line}Turn Total: {p2.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p2.turn_total = 0
                        p1.switch_turn()
                        p2.switch_turn()
                    else:
                        p2.turn_total += roll
                    if p2.turn_total + p2.player_score >= 100:
                        p2.player_score += p2.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p2.player_score += p2.turn_total
                    p2.turn_total = 0
                    p1.switch_turn()
                    p2.switch_turn()
                else:
                    print("\nINVALID INPUT\n")

        # Winner confirmation
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    # human vs comp
    elif player1 == "human" and player2 == "computer":
        p1 = Player(1, False)
        p2 = ComputerPlayer(2, False)
        print('Welcome to The Game of Pig. (TIMED)')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        end = int(time.time()) + timed
        while p1.player_score < 100 and p2.player_score < 100 and int(time.time()) < end:

            # p1 human turn
            while p1.get_turn() is True:
                print("\nPlayer 1's turn")
                print(f"Score: {p1.player_score}{new_line}Turn Total: {p1.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p1.turn_total = 0
                        p2.switch_turn()
                        p1.switch_turn()
                    else:
                        p1.turn_total += roll
                    if p1.turn_total + p1.player_score >= 100:
                        p1.player_score += p1.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p1.player_score += p1.turn_total
                    p1.turn_total = 0
                    p2.switch_turn()
                    p1.switch_turn()
                else:
                    print("\n---INVALID INPUT---")
            if p1.player_score >= 100:
                break

            # p2 comp turn
            while p2.get_turn() is True:
                p2.strategy()
                p1.switch_turn()
                p2.switch_turn()

        # Winner confirmation
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    # comp vs comp
    elif player1 == "computer" and player2 == "computer":
        p1 = ComputerPlayer(1, False)
        p2 = ComputerPlayer(2, False)
        print('Welcome to The Game of Pig. (TIMED)')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        end = int(time.time()) + timed
        while p1.player_score < 100 and p2.player_score < 100 and int(time.time()) < end:
            # p1 computer turn
            while p1.get_turn() is True:
                p1.strategy()
                p2.switch_turn()
                p1.switch_turn()
            if p1.player_score >= 100:
                break
            # p2 computer turn
            while p2.get_turn() is True:
                p2.strategy()
                p1.switch_turn()
                p2.switch_turn()

        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0


def pig_game(player1, player2):
    random.seed(0)
    new_line = '\n'
    roll = 0
    if player1 == "human" and player2 == "human":
        p1 = Player(1, False)
        p2 = Player(2, False)
        print('Welcome to The Game of Pig.')
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()
        while p1.player_score < 100 and p2.player_score < 100:
            while p1.get_turn() is True:
                print("\nPlayer 1's turn")
                print(f"Score: {p1.player_score}{new_line}Turn Total: {p1.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p1.turn_total = 0
                        p2.switch_turn()
                        p1.switch_turn()
                    else:
                        p1.turn_total += roll
                    if p1.turn_total + p1.player_score >= 100:
                        p1.player_score += p1.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p1.player_score += p1.turn_total
                    p1.turn_total = 0
                    p2.switch_turn()
                    p1.switch_turn()
                else:
                    print("\n---INVALID INPUT---")
            if p1.player_score >= 100:
                break
            while p2.get_turn() is True:
                print("\nPlayer 2's turn")
                print(f"Score: {p2.player_score}{new_line}Turn Total: {p2.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p2.turn_total = 0
                        p1.switch_turn()
                        p2.switch_turn()
                    else:
                        p2.turn_total += roll
                    if p2.turn_total + p2.player_score >= 100:
                        p2.player_score += p2.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p2.player_score += p2.turn_total
                    p2.turn_total = 0
                    p1.switch_turn()
                    p2.switch_turn()
                else:
                    print("\nINVALID INPUT\n")
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    # comp vs human
    elif player1 == "computer" and player2 == "human":
        p1 = ComputerPlayer(1, False)
        p2 = Player(2, False)
        print('Welcome to The Game of Pig.')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        while p1.player_score < 100 and p2.player_score < 100:

            # p1 computer turn
            while p1.get_turn() is True:
                p1.strategy()
                p2.switch_turn()
                p1.switch_turn()
            if p1.player_score >= 100:
                break

            # p2 human turn
            while p2.get_turn() is True:
                print("\nPlayer 2's turn")
                print(f"Score: {p2.player_score}{new_line}Turn Total: {p2.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p2.turn_total = 0
                        p1.switch_turn()
                        p2.switch_turn()
                    else:
                        p2.turn_total += roll
                    if p2.turn_total + p2.player_score >= 100:
                        p2.player_score += p2.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p2.player_score += p2.turn_total
                    p2.turn_total = 0
                    p1.switch_turn()
                    p2.switch_turn()
                else:
                    print("\nINVALID INPUT\n")

        # Winner confirmation
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    # human vs comp
    elif player1 == "human" and player2 == "computer":
        p1 = Player(1, False)
        p2 = ComputerPlayer(2, False)
        print('Welcome to The Game of Pig.')

        # first turn decision
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()

        # p1 human turn
        while p1.player_score < 100 and p2.player_score < 100:
            while p1.get_turn() is True:
                print("\nPlayer 1's turn")
                print(f"Score: {p1.player_score}{new_line}Turn Total: {p1.turn_total}")
                choice = input("Enter 'r' to roll or 'h' to hold: ")
                if choice == 'r' or choice.lower() == 'r':
                    roll = die_roll()
                    print(f"You rolled: {roll}")
                    if roll == 1:
                        p1.turn_total = 0
                        p2.switch_turn()
                        p1.switch_turn()
                    else:
                        p1.turn_total += roll
                    if p1.turn_total + p1.player_score >= 100:
                        p1.player_score += p1.turn_total
                        break
                elif choice == 'h' or choice.lower() == 'h':
                    p1.player_score += p1.turn_total
                    p1.turn_total = 0
                    p2.switch_turn()
                    p1.switch_turn()
                else:
                    print("\n---INVALID INPUT---")
            if p1.player_score >= 100:
                break
            while p2.get_turn() is True:
                p2.strategy()
                p1.switch_turn()
                p2.switch_turn()

        # Winner confirmation
        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0

    elif player1 == "computer" and player2 == "computer":
        p1 = ComputerPlayer(1, False)
        p2 = ComputerPlayer(2, False)
        print('Welcome to The Game of Pig.')
        first_turn = random.randrange(1, 11)
        if first_turn >= 6:
            print("Player 1 goes first.")
            p1.switch_turn()
        else:
            print("Player 2 goes first.")
            p2.switch_turn()
        while p1.player_score < 100 and p2.player_score < 100:
            while p1.get_turn() is True:
                p1.strategy()
                p2.switch_turn()
                p1.switch_turn()
            if p1.player_score >= 100:
                break
            while p2.get_turn() is True:
                p2.strategy()
                p1.switch_turn()
                p2.switch_turn()

        p1.turn_total = 0
        p2.turn_total = 0
        if p1.player_score > p2.player_score:
            print("\nPlayer 1 Wins!")
            print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
        else:
            print("\nPlayer 2 Wins!")
            print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")
            p1.player_score = 0
            p2.player_score = 0


if __name__ == "__main__":
    intro()
    new_game()