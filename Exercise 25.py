def minion_game(string):
    # your code goes here
    # l = len(string)
    # kevin = []
    # stuart = []

    # for i in range(l):
    #     kevin += [string[i:l-j] for j in range(l-i) if string[i] in ['A', 'E', 'I', 'O', 'U']]
    #     stuart += [string[i:l-j] for j in range(l-i) if string[i] not in ['A', 'E', 'I', 'O', 'U']]

    # if len(stuart) > len(kevin):
    #     print('Stuart ' + str(len(stuart)))
    # elif len(stuart) < len(kevin):
    #     print('Kevin ' + str(len(kevin)))
    # else:
    #     print('Draw')
    # Solution below is much better than above which gives runtime error for long strings
    # Just check the full list of possible substrings. Kevin scores for those starting with vowel, Stuart o/w
    s = input()

    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

# The Minion Game
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as . In this problem,  is not considered a vowel.