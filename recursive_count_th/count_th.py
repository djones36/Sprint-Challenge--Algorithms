'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# input 1 word =string
# total count of th
# case - th only matters if lowercase
# use recursion
'''
Plan
1. find all the lower case th
2. check every 2 letters in the string, isolate every 2 letters to run a check if it is "th".
'''


def count_th(word):
    if len(word) == 0 or len(word) < 2:
        return 0
    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

    # print(len(word))
    # print(word[0:2])  # isolate 2 letters


# print(count_th("Breathe"))
