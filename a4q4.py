"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""
import random


class Card(object):
    def create(self):
        """
        Purpose:
            Creates and returns a list of all possible cards that can be drawn from the 52 card playing deck.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        list_of_cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AD', '2D',
                         '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AS', '2S', '3S', '4S',
                         '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C',
                         '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']
        return list_of_cards

    def deal(self, num_cards, num_players, deck):
        """
        Purpose:
            Randomly deals a number of cards to a number of players from the given deck.
        Pre-conditions:
            :param num_cards: The number of cards handed to the players.
            :param num_players: The number of players in a game.
            :param deck: The total number of cards in a deck.
        Post-conditions:
            When a card is drawn, it is removed from the deck.
        Return:
            A list of lists of cards to a number of players in a game.
        """
        cards_dealt = []
        player_list = []
        while len(deck) > 0:
            random_card = random.choice(deck)
            if random_card in deck:
                deck.remove(random_card)
                player_list.append(random_card)
            cards_dealt.append(player_list)
        return cards_dealt

    def value(self, card):
        """
        Purpose:
            Takes in the string of a card, and returns its integer value.
        Pre-Conditions:
            :param cards: The string of a card.
        Post-conditions:
            (none)
        Return:
            The card's integer value.
        """
        card_dict = {'AH': 1, '2H': 2, '3H': 3, '4H': 4, '5H': 5, '6H': 6, '7H': 7, '8H': 8, '9H': 9, '10H': 10,
                     'JH': 11, 'QH': 12, 'KH': 13, 'AD': 1, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7,
                     '8D': 8, '9D': 9, '10D': 10, 'JD': 11, 'QD': 12, 'KD': 13, 'AS': 1, '2S': 2, '3S': 3, '4S': 4,
                     '5S': 5, '6S': 6, '7S': 7, '8S': 8, '9S': 9, '10S': 10, 'JS': 11, 'QS': 12, 'KS': 13, 'AC': 1,
                     '2C': 2, '3C': 3, '4C': 4, '5C': 5, '6C': 6, '7C': 7, '8C': 8, '9C': 9, '10C': 10, 'JC': 11,
                     'QC': 12, 'KC': 13}
        card_value = card_dict[card]
        return card_value

    def highest(self, list_of_cards):
        """
        Purpose:
            Takes a list of cards, and returns the the card string with the highest value.
        Pre-Conditions:
            :param list_of_cards: A list of card strings.
        Post-conditions:
            (none)
        Return:
            The card string with the highest value.
        """
        dict_of_cards = {}
        for card in list_of_cards:
            dict_of_cards[card] = self.value(card)
        largest_card = max(dict_of_cards)
        return largest_card

    def lowest(self, list_of_cards):
        """
        Purpose:
            Takes a list of cards, and returns the card string with the lowest value.
        Pre-Conditions:
            :param list_of_cards: A list of card strings.
        Post-conditions:
            (none)
        Return:
            The card string with the lowest value.
        """
        dict_of_cards = {}
        for card in list_of_cards:
            dict_of_cards[card] = self.value(card)
        smallest_card = min(dict_of_cards)
        return smallest_card

    def average(self, list_of_cards):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return list_of_cards
