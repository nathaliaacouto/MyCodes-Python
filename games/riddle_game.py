#when you choose a number, it will print a riddle and you can answer it
questions = {1: "What has to be broken before you can use it?",
    2: "I’m tall when I’m young, and I’m short when I’m old. What am I?",
    3: "What month of the year has 28 days?",
    4: "What is full of holes but still holds water?",
    5: "What is always in front of you but can’t be seen?",
    6: "What goes up but never comes down?",
    7: " What gets wet while drying?",
    8: "I shave every day, but my beard stays the same. What am I?",
    9: "What can’t talk but will reply when spoken to?",
    10: "The more of this there is, the less you see. What is it?"
    }
  
answers = {1: "egg",
    2: "candle",
    3: "all",
    4: "sponge",
    5: "future",
    6: "age",
    7: "towel",
    8: "barber",
    9: "echo",
    10: "darkness"
    }

def answerTheRiddle():
  answer = input("What's the answer? ")

  if answer.lower() in answers[choice]:
    print("Correct!")
  else:
    print("Oh no, the answer was {}" .format(answers[choice]))

def rules():
  print("The rules are simple: choose a number and one riddle will be shown, answer it and see if it is correct! For most riddles you will just need to use a word, such as 'dog' or 'fruit'")

while(True):
  choice = int(input("\nChoose a number from 1-10 to get a riddle (0 to exit, -1 to rules): "))
  if choice == 0:
    print("See you later!")
    break
  if choice == -1:
    rules()

  if choice in questions:
    print(questions[choice])
    answerTheRiddle()
  elif choice != -1:
    print("Sorry, that number cannot be chosen")
