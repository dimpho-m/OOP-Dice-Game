#import packages needed
import random

class Die: 
    """ This is a class that initializes the 5 die used to play the game"""
# We assume that the game is being played with a regular 6-sided dice. We initialize each dice to start at 0
    def __init__(self, die):
        self.die = [0] * 5

# define a method that rolls all or a subset of the die
    def roll():
    """ This method can roll a subset of the die or all of them depending on the subset given as a parameter. 
    For example, should you want to roll dice 1, 2 and 5 pass [1, 2, 5] else pass the set list(range(5)) to roll 
    all die. It returns the current """
        for i in self.die:
        self.die[i] = random.randint(1, 7)

    def value():
        return self.die    

class DicePoker:
    """ This class will keep track of the amount of money the player gains and uses throughout the game as well automatically terminate 
    when the player has run out of funds. It also gives the player the option of exiting the game.""" 
# constructor
    def __init__(self, start_score, current_score, round_cost, hand_score):
        self.start_score = 100
        self.current_score = current_score
        self.round_cost = 10
        self.hand_score = hand_score

    def hand(die):
# create instances of the methods in the Die class 
        self.die = Die()
        die.roll()
        self.die_list = die.value()

        for i in self.die_list:
# create a list in which to store the counts from the subset list
            counts = [0, 0, 0, 0, 0]
            counts[i] = counts[i] + 1
# the hand rolled at random is scored 
            if 5 in counts:
                return 'Five of a kind' , 30

            elif 4 in counts:
                return 'Four of a kind' , 15

            elif 3 in counts:
                return 'Three of a kind', 8

            elif (3 in counts ) and (2 in counts):
                return 'Full house', 12

            elif (1 and 2 and 3 and 4 and 5) in counts:
                return 'Straight', 20

            elif counts.count(2) == 2:
                return 'Two Pairs' , 5

            else :
                return 'Bad hand' , 0 

    def score_calculator():
        start_amount = self.start_score - self.round_cost
        hand_fare = self.hand_score
        hand_fare.hand()
        present_amount = self.current_score
        present_amount = start_amount + hand_fare

        return present_amount            
