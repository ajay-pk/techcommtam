# #Anagram Solver is a tool used to help players
# rearrange letters to generate all the possible
# words from them. You input the letters, and Anagram
# Maker gives you the edge to win Scrabble, Words With
# Friends, or any other word game. No matter the
# length or difficulty of the word, Anagram Solver
# provides all available word options.


from collections import Counter

# Counter is an unordered collection where elements
# are stored as Dict keys and their count as dict value.
#  Counter elements count can be positive, zero or
#  negative integers. However there is no restriction
#  on it's keys and values. Although values are intended
#  to be numbers but we can store other objects too.


def anagram(first, second):

    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb")
