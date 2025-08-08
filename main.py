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

                                               # ->>>First and Second steps.
                                                # ->>>Ending the game and the score counter.


count = 0
while 1:# starting the game and make it continuous until the user cutoff the infinite loop or exit the game.
 Random_word = random.choice(file_words2) # random.choice() is a built_in function that choose a random item from a list ,dict and tuple. I put it here to generate a new Random_word every time the game starts.
 i = 0
 Guesses = [] # A list to store all user guessed words.
 Status = False # a boolean to inform the user that he has lost if he did not guess random_word correctly in his 6 tries.
 # print("Random word from Dataset is :",Random_word) # for Debbuging
 while i < 6: # outer while loop is number of rows(number of guessed words) and inner loop(y) is number of columns (number of letters of the word).

    guesses = input(f"Enter your {i+1} guess :") # Takes user input.

    if guesses in file_words2: # Validity of the word
        Guesses.append(guesses) # Append every user input guessed word to our list
        for x in Guesses:
            print(f"       {x.upper()}       ") # printing output as [6][5] grid on the terminal.
        # print("WORD VALID") # for Debbuging

        if guesses == Random_word: # User has guessed the word correctly
            print("YOU WIN!")
            print(f"The secret word is {Random_word}")
            count += 1
            print(f"Your score is {count}") # Counter that indicates the score
            Status = True
            break

        elif guesses != Random_word: # Word is valid but not the Random_word
            for y in range (5):
                if guesses[y] in Random_word and y == Random_word.index(guesses[y]): # index() is a built-in function to get our letter index in Random_word, we used it to compare letter index in user guessed word and in Random_word.
                        print(f"{guesses[y]} is a valid letter in the Random_word with the same index") # first possible hint to the user
                elif guesses[y] in Random_word:
                        print(f"{guesses[y]} is a valid letter in the Random_word") # second possible hint to the user
                else:
                        print(f"{guesses[y]} is not a valid letter in the Random_word") # third possible hint to the user











