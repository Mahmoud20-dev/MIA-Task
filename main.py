                                   # ->>> Steps we have to pass through it to achieve our goal.

#as an initialization we have to read words.txt file to make it as our dataset and determine a random word from it. //ok
#first step, we need to implement [6][5] grid to make the user interface with it and guesses 6 words from Dataset every word contains 5 letters. //ok
#The second step the user has 6 tries to guess a word that will be randomly selected from the game (code). //ok
#We have 2 options first one that the user guessed a word not included in Dataset,so we have to set an error message that WORD NOT FOUND. //ok
#second one that the user guessed the correct word from dataset so we have to determine letters that included in random word chose by game by its index. ->> {Bonus according to color (Green ->> correct index,Yellow ->> close index,Gray ->> letter no included)}. //ok
#Game ends when user has guessed the word correctly before 6 tries or the user has finished his 6 tries or (additional property) ->> (user input is giveup). //ok
#Score increase by 1 if user guessed the word correctly and vice versa it decreased by 1 if user failed to guess the word. //ok

 #بسم الله
import random
                                                             # ->>>Initialization.


Initialization = open('words.txt','r')
file_words1 = Initialization.readlines() # return a list, every item on it is line from the file. But we have a problem here, list is created by \n which is an indication to a new line in the end of every item in the list. we have many techniques to solve this problem.
file_words2 = [x[:-1] for x in file_words1] # we have a built-in functions to solve this problem but i prefer SLICING to solve it, this technique loops inside every item in the list and kills the last character on it which is \n character.
# print(file_words2) # for Debbuging










