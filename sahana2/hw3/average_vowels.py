# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(words):
    num_vowels = 0
    num_consonants = 0
    for i in range(len(words)): 
        if words[i] == 'a' or words[i] == 'e' or words[i] == 'i' or words[i] == 'o' or words[i] == 'u': 
            num_vowels+=1 
        else:
            num_consonants+=1
    return(num_vowels,num_consonants)

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(paragraph): 
    paragraph_list = paragraph.replace("!",".").split(".")
    listing = list()
    for sentances in paragraph_list:
        listing.append(list(counting_vowels_and_consonants(sentances)))
    avg_consonants = 0
    for x in listing:
        avg_consonants = avg_consonants + x[1]
    avg_vowels = 0 
    for x in listing:
        avg_vowels = avg_vowels + x[0]
    return(len(paragraph_list), avg_vowels, avg_consonants)

        


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
print(average_vowels_and_consonants(paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)))

list_result = list(average_vowels_and_consonants(paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)))
# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
print(f'The number of sentances is {list_result[0]}, the output of average vowels is {list_result[1]}, and the consonants per sentance is {list_result[2]}.')