import re
import time 
lives = 5

guessWord = ""
while guessWord.isnumeric() == True or guessWord == "":
  guessWord = input("What word would you like your opponent to guess?\n")
  guessWord = guessWord.replace(' ', '')
  guessWord = guessWord.upper()

wordLength = len(guessWord) - 1

blank = []
for x in range(wordLength + 1):
  blank.append("*")
print("\033c", end='')

realResult = blank[0] * (wordLength + 1)
print ("Your word to guess is:",blank[0] * (wordLength + 1))

while True:
  
  if lives == 0:
    time.sleep(1)
    print("You ran out of lives, you died")
    print("The word was", guessWord)
    exit()
    
  choice = input("Would you like to guess the word or guess a letter? W or L\n").upper()
  if choice == "W":
    result = input("What do you think the word is\n")
    result = result.upper()
    if result != guessWord:
      lives = lives - 1
      print("That was not the word, you have", lives, "lives left\n")
      print("The word to guess is:", realResult,"\n")
      continue
    elif result == guessWord:
      print("You guessed the word")
      exit()
      
    break
  elif choice == "L":
    
    userInput = input("What letter would you like to guess\n")
    userInput = userInput.upper()

    if userInput not in guessWord:
      lives = lives - 1
      print("That letter was not in the word, you have", lives,"lives left")
      time.sleep(2)
      continue

    loopTimes= guessWord.count(userInput)

    for x in range (loopTimes):
      letterPosition = [_.start() for _ in re.finditer(userInput, guessWord)] 
  
  
      blank[letterPosition[x]] = userInput
  

    for x in range(wordLength + 1):
      realResult = "".join(blank)

    print(userInput, "was a letter in the word\n" "Your word to guess is:",realResult,"\n")
    time.sleep(2)
    if realResult == guessWord:
      print("You guessed the word, good job!")
  
      break
    continue

 
  
