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
        random_card = random.choice(deck)
        cards_dealt = [[random_card] * num_cards] * num_players
        return cards_dealt

    def value(self, cards):
        """
        Purpose:
            Return the average of all the values seen so far.
        Pre-Conditions:
            :param cards: The value to be added.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return cards

    def highest(self, list_of_card):
        """
        Purpose:
            Return the average of all the values seen so far.
        Pre-Conditions:
            :param list_of_card: The value to be added.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__highest

    def lowest(self, list_of_card):
        """
        Purpose:
            Return the average of all the values seen so far.
        Pre-Conditions:
            :param list_of_card: The value to be added.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__lowest

    def average(self, list_of_card):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__average

