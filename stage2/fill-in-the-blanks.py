# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# Quiz sentences
easy = '''The world wide [___1___] was developed in the early 1990's. 
It is a collection of [___2___] documents. [___2___] stands for [___3___] Markup Language which is the basis for almost any [___1___] page. 
You can find several types of documents on the [___1___] (images, videos, music,...). 
[___2___] allows to organize all those things together. The [___4___]s allow to link the pages to one another.'''

medium = ''' Python is a [___1___] typed language. This means that the type of the [___2___]s (string, integer, float, ..) is deduced at runtime by the [___3___].
This contrasts with a [___4___] typed language like Java where it is mandatory to declare the type of ANY [___2___]s.'''

hard = '''[___1___] [___2___]s get structured through [___3___], this means that [___4___] blocks are defined by their [___3___]. 
That's what we expect from any [___2___] [___4___], isn't it? Yes, but in the case of [___1___] it's a language requirement not a matter of style. 
This principle makes it easier to read and understand other people's [___1___] [___4___]. '''

# Quiz responses
easy_words = ["web", "html", "hypertext", "hyperlink"]
medium_words = ["dynamically", "variable", "interpreter", "statically"]
hard_words = ["Python", "program", "indentation", "code"]


def replaceWords(sentence, index, word):
    '''replace the indexed positions in the sentence by the word provided
       Sentence:    
            Initial text including the blanks. 
            Blanks should have the format : [___n___] (3 underscores before and after "n" between brackets) 
            with "n" being the index of the word to discover starting at 1
       index:   
            The index to be replaced within the sentence
            index starts at 1 
        word : 
            The word that will replace the blank positions
        the function return the sentence with the blank positions replaced by the word provided'''
        
    word_begin = "[___" 
    word_end = "___]"
    old = word_begin + str(index) + word_end
    result = sentence.replace(old, word)
    return result
	
def play_game(sentence, words, max_attempts): 
    '''Plays a full game of fill_in_the_blank.
	   Sentence: 
            Initial text including the blanks. 
            Blanks should have the format : ___n___ 
            with n being the index starting at 1
	   words : 
            list of replacement words in the order of the numbers blanks
	   max_attemps : 
            Maximum number of wrong attempts allowed per guess
	   The player is prompted to suggest a replacement word	starting at 1 until the test is complete
	   the function return True if the player won, false otherwise'''	   
    
    # initialize attempts and word_index
    attempts = word_index = 0
    while True: 
        guess  = raw_input("\n" + sentence + "\nNumber of guesses left: " + str(max_attempts - attempts) + "\n" + "Type your guess for position " + str(word_index + 1) + "\n")
        if guess == words[word_index]:
            print "Good guess !!!"
            sentence =  replaceWords(sentence, word_index + 1, words[word_index]) 
            word_index += 1
            attempts = 0
            if word_index == len(words):
                print "Completed Quiz:\n" + sentence + "\n"
                return True
        else:
            print "wrong guess !",
            attempts += 1
            if max_attempts != attempts:
                 print "Try again"
            else:
                return False

def init_level():
    """prompt the player for the desired level and number of tries
        Returns:
         - level : the level of difficulty choosen by the user
         - guess : Maximum number of guess allowed (from 1 up to 10)"""

    sharpMultiplicator = 35 #Number of '#' in a line
    MIN_LEVEL = 0
    MAX_LEVEL = 2 
    level = -1
    while level < MIN_LEVEL or level > MAX_LEVEL: 
        print "#" * sharpMultiplicator
        level = raw_input("Welcome to the start to program quiz!\nPlease choose your quiz level:\n0 - easy\n1 - medium\n2 - hard\n")
        if level.isdigit():
            level = int(level)
        else:
            level = -1
    return level

def init_guesses():
    """prompt the player for the desired level and number of tries
        Returns:
         - level : the level of difficulty choosen by the user
         - guess : Maximum number of guess allowed (from 1 up to 10)"""

    sharpMultiplicator = 35 #Number of '#' in a line
    MIN_GUESS = 1
    MAX_GUESS = 10
    guess = 0 
    while guess < MIN_GUESS or guess > MAX_GUESS:   
        print "#" * sharpMultiplicator
        guess = raw_input("Please input the number of guesses you'd like to have for each question (1-10)\n")
        if guess.isdigit():
            guess = int(guess)
        else:
            guess = 0
    return guess


##############################################################
# Main routine 
##############################################################

level = init_level()
max_guess = init_guesses()
samples = [easy, medium, hard]
words = [easy_words, medium_words, hard_words]

if play_game(samples[level], words[level], max_guess):
    print "YOU WON CONGRATS!!!!"
else:
    print "You have no more guesses left.\nGAME OVER"

