
#  Blackjack
#p1_random.py in the same folder.

import p1_random as p1


def print_menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print()  # blank line after the menu


def card_text(n):
    if n == 1:
        return "ACE!"
    elif n == 11:
        return "JACK!"
    elif n == 12:
        return "QUEEN!"
    elif n == 13:
        return "KING!"
    else:
        return str(n) + "!"


def card_value(n):
    if n == 1:
        return 1
    elif n >= 11:
        return 10
    else:
        return n


def main():
    rng = p1.P1Random()

    game_num = 1
    player_wins = 0
    dealer_wins = 0
    ties = 0
    games_done = 0  # only completed games count here

    while True:
        # Start new round
        print(f"START GAME #{game_num}\n")

        hand = 0

        # First card is dealt automatically
        c = rng.next_int(13) + 1
        hand += card_value(c)
        print(f"Your card is a {card_text(c)}")
        print(f"Your hand is: {hand}")
        print()

        # Round loop
        while True:
            print_menu()
            choice = input("Choose an option: ")

            # Invalid input
            if choice not in {"1", "2", "3", "4"}:
                print("Invalid input!")
                print()
                print("Please enter an integer value between 1 and 4.")
                # do NOT reprint the menu here; loop will do it once
                continue

            choice = int(choice)

            if choice == 1:
                # Hit: deal another card
                nxt = rng.next_int(13) + 1
                hand += card_value(nxt)
                print()
                print(f"Your card is a {card_text(nxt)}")
                print(f"Your hand is: {hand}")
                print()

                if hand == 21:
                    print("BLACKJACK! You win!")
                    print()
                    player_wins += 1
                    games_done += 1
                    game_num += 1
                    break
                elif hand > 21:
                    print("You exceeded 21! You lose.")
                    print()
                    dealer_wins += 1
                    games_done += 1
                    game_num += 1
                    break

            elif choice == 2:
                # Hold here
                dealer = rng.next_int(11) + 16
                print()
                print(f"Dealer's hand: {dealer}")
                print(f"Your hand is: {hand}")
                print()

                if dealer > 21:
                    print("You win!")
                    print()
                    player_wins += 1
                elif dealer == hand:
                    print("It's a tie! No one wins!")
                    print()
                    ties += 1
                elif dealer > hand:
                    print("Dealer wins!")
                    print()
                    dealer_wins += 1
                else:
                    print("You win!")
                    print()
                    player_wins += 1

                games_done += 1
                game_num += 1
                break

            elif choice == 3:
                # Statistics for completed games
                print()
                print(f"Number of Player wins: {player_wins}")
                print(f"Number of Dealer wins: {dealer_wins}")
                print(f"Number of tie games: {ties}")
                print(f"Total # of games played is: {games_done}")
                pct = 0.0 if games_done == 0 else (player_wins / games_done) * 100
                print(f"Percentage of Player wins: {pct:.1f}%")
                print()

            else:  # choice == 4
                return


if __name__ == "__main__":
    main()
