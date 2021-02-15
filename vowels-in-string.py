
#the function that takes in a string and then prints out all the vowels in the string


def vowels_in_string(string):
    
    all_vowels = "AeEeIiOoUu"
    list_vowels=[vowel for vowel in string if vowel in all_vowels]
    return list_vowels
    
print(vowels_in_string("AWrite a functionU thatA takes"))

