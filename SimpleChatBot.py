# There are a few bug that I can see, but this is just a simple chatBot
Stored_Values = {}


# Checks the UserInput if its a question or should it store values
def CheckWords(UserInput, Stored_Values):
    # These are words that need to be ingnored and go to the next word
    Not_needed_words = ['what', 'is', 'the', 'my']
    i = 0  # This is the index that will be incremented in the first for loop and will help me get the index of the previous word of the current word
    for Word in UserInput:
        if (Word in Not_needed_words):  # If the word is in the list of not needed to be check words, ignore
            i += 1
            continue
        else:
            # If it is my then it will help me indetify that Word is going to be a variable name
            if (UserInput[i-1] == 'my'):
                if ('what' in UserInput and UserInput.index('what') < UserInput.index('my')):
                    try:
                        print('your ' + Word+' is ' + Stored_Values[Word])
                    except:
                        print(f"Didn't give input for {str(Word)}")
                else:  # This is for storing values in the dictonary
                    n = 0
                    for y in UserInput:

                        # After 'is' there will be data that will be the data of the Variable name we got before, Word
                        if (y == 'is'):
                            # Storing the Data
                            Stored_Values[Word] = UserInput[n+1]
                            break
                        n += 1
                    break

    return Stored_Values  # Updating Stored_Values everytime it is being called


while (True):
    UserInp = input()
    if (UserInp == 'quit'):
        print('this is the end')
        break
    UserInput = UserInp.split(' ')
    Stored_Values = CheckWords(UserInput, Stored_Values)
