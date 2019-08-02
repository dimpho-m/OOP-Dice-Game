#class definition for an n-sided die

#import packages
import random

class MultiSidedDie:

#constructor here
  def __init__(self, number_of_sides, current_value):
      '''A die is initialized with the number of sides known as well the 
      current player-facing value'''
      self.number_of_sides = number_of_sides
      self.current_value = current_value

#define method 'roll' to roll the MultiSidedDie
  def roll():
      '''Rolls the die and returns a random value between 1 and the known number
      of sides'''
      die_roll = random.randint(1, self.number_of_sides)

#define method 'set_value' to set the die to a particular value
  def set_value(chosen_value):
      '''The player is allowed to 'cheat' and set the die roll value to their liking'''
      chosen_value = self.current_value

#define method 'get_value' to return the current value of the MultiSidedDie
  def get_value():
      '''Returns the newly rolled value of the die'''
      die_roll = self.current_value
      return die_roll




  

  
