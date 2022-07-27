#game to guess the number

import random
import os
def clues(trying: int, number: int, user: int):
  if (trying == 5):
    if (0 <= number and number <= 50):
      print("Another Clue: the number is between 0 and 50")
    elif (50 <= number and number <= 100):
      print("Another Clue: the number is between 50 and 100")
  if (user == (number - 1) or user == (number + 1)):
    print("Wow! That's really close")
  elif ((number - 10) < user < (number + 10)):
    print("That's close!")

tries = 0
correct = random.randrange(0,100)

print("First Clue: is a number between 0 and 100")
while(True):
  answer = int(input("Your guess: "))
  if answer == correct:
    print("\nYou win!!! The number was {}" .format(correct))
    print("You tried {} times\n" .format(tries+1))
    break
  elif (answer > 100 or answer < 0):
    print("The number is between 0 and 100")
  else:
    tries = tries + 1
    clues(tries, correct, answer)
    continue

