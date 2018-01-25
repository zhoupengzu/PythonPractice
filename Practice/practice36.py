from functools import reduce
def sum_of_middle_three(*scores):
    print(max(scores))
    print(min(scores))
    # sorted(scores)
    print(scores)
    print(reduce(lambda score, sum:sum + score, scores))

sum_of_middle_three(1,2,3,4,5,6)

print(len("hahh"))

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(sorted(days_in_month))
    days_in_month.sort()
    print(days_in_month)
    #todo: return the correct value
    max_index = len(days_in_month)
    temp_index = month_number - 1
    if temp_index >= max_index:
        return 0
    else:
        return days_in_month[(month_number - 1)]


# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))

dic1 = {}
dic1[0] = 1
print(dic1)

str = "I am a student"
str_sep = str.split(sep=" ")
print(str_sep)

import math
print(math.exp(3))

import random

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password():
    word_file = "words.txt"
    word_list = []
    #fill up the word_list
    with open(word_file, 'r') as words:
	    for line in words:
		    # remove white space and make everything lowercase
		    word = line.strip().lower()
		    # don't include words that are too long or too short
		    if 3 < len(word) < 8:
		        word_list.append(word)

    result = ""
    for _ in range(3):
        index = random.randrange(0, len(word_list))
        result +=  word_list[index]
    return result

	
# print(generate_password())
a1 = [1,2,3,4,5]
print(sum(a1))

def tag_count(tag_list):
    sum = 0
    for ele in tag_list:
        if ele[0] == '<' and ele[-1] == '>':
            sum += 1
    return sum
