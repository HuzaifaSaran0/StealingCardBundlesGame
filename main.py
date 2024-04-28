import random
import time


class CardsGame:
    def __init__(self):
        # Initialize the game with a deck of cards, player hands, screen cards, and other players' matched cards
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []
        self.cards_on_the_screen = []
        self.distributions = 0
        self.other_players_card = [[], [], [], []]  # Only those which were matched
        self.players = [self.player1, self.player2, self.player3, self.player4]
        self.winner = 0
        self.game_started = False
        self.count = 0

        # Start the game by distributing cards and displaying the initial screen
        self.screen_card()
        while self.cards or self.cards_on_the_screen:
            if self.game_started:
                for player_hand in self.players:
                    if len(player_hand) == 0 and not self.cards_on_the_screen:
                        # print(player_hand)
                        self.count += 1
                    else:
                        self.winner = self.players.index(player_hand)
                        # print(f"not {player_hand}")

                if self.count < 2:
                    if self.distributions < 3:
                        time.sleep(1)
                        print(f"\n\n----------Distribution # {self.distributions + 1}----------\n\n")
                        self.dealer_Card_distribution()
                        self.distributions += 1

                    # Allow each player to take their turn
                    for player_input in range(4):
                        print(f"\n\n-----Player {player_input + 1} Turn-----")
                        if self.players[player_input]:
                            print(f"Your Cards: \n\t\t\t\t{self.players[player_input]}")
                            print(f"Screen Cards: \n\t\t\t\t{self.cards_on_the_screen}")
                            print(f"Other Players Cards:", end="")
                            [print(f"\n\t\t\t\tPlayer{index + 1} Cards are :{card}", end="")
                             if index != player_input
                             else print(f"\n\t\t\t\tPlayer{index + 1} Cards are: []", end="")
                             for index, card in enumerate(self.other_players_card)]

                            # Prompt the player to match a card from their hand with a card on the screen

                            thrown_number = self.getting_card()
                            self.Type(thrown_number, player_input + 1)
                            time.sleep(1)
                        else:
                            print("You have no more cards to play")
                    self.count = 0
                else:
                    print("------Game Over------")
                    scores = []
                    self.players[self.winner].extend(self.cards_on_the_screen)
                    for player in self.players:
                        scores.append(len(player))
                    print(f"Player 1 Score: {scores[0]}\nPlayer 2 Score: {scores[1]}\nPlayer 3 Score:"
                          f" {scores[2]}\nPlayer 4 Score: {scores[3]}")
                    print(f"-----Winner is Player {scores.index(max(scores)) + 1}------")
                    break
            else:
                # self.dealer_Card_distribution()
                self.game_started = True

    def getting_card(self):
        card = input("\nWrite Card Number to match:")
        return card

    def screen_card(self):
        for k in range(4):
            index = random.randint(0, len(self.cards) - 1)
            s_card = self.cards.pop(index)
            self.cards_on_the_screen.append(s_card)

    # Method to distribute cards to players
    def dealer_Card_distribution(self):
        for i in range(4):
            for j in range(4):
                index = random.randint(0, len(self.cards) - 1)
                card = self.cards.pop(index)
                self.players[i].append(card)

    # Method to determine the type of input (number or string) and call the matching method accordingly
    def Type(self, value_to_check_type, value_index):
        try:
            int_value = int(value_to_check_type)
            self.Match(str(int_value), value_index)
        except ValueError:
            self.Match(value_to_check_type.capitalize(), value_index)

    def other_players_match(self, the_index):
        other_list = []
        for i in self.other_players_card:  # I want to make that when the person whose turn is to match then his
            if self.other_players_card.index(i) == the_index:  # Changed This line
                other_list.append("")
            elif i:  # matched cards should not be shown
                for j in i:
                    other_list.append(j)
            else:
                other_list.append("")
        return other_list

    # Method to match the thrown card with cards on the screen or other players' matched cards
    def Match(self, thrown, index):
        # card_thrown = False

        if thrown in self.players[index - 1]:
            # card_thrown = True
            other_player_list = self.other_players_match(index - 1)
            if thrown in other_player_list:
                self.other_players_card[index - 1] = []
                self.other_players_card[index - 1].append(thrown)
                self.other_players_card[other_player_list.index(thrown)] = []
                self.players[index - 1].extend(self.players[other_player_list.index(thrown)])
                self.players[other_player_list.index(thrown)] = []

            elif thrown in self.cards_on_the_screen:
                removed_card = thrown
                self.cards_on_the_screen.remove(thrown)
                self.players[index - 1].append(removed_card)
                self.other_players_card[index - 1].clear()
                self.other_players_card[index - 1].append(removed_card)

            else:
                self.cards_on_the_screen.append(thrown)
        else:
            print("Invalid Card Number, You lost your turn")
        # other_player_list = self.other_players_match(index - 1)
        # print(other_player_list)


startGame = CardsGame()
