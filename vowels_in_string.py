def vowels_in_string(string):

    all_vowels = "AaEeIiOoUu"
    list_vowels = [vowel.lower() for vowel in string if vowel in all_vowels]
    vowels = ",".join(dict.fromkeys(list_vowels))
    print(f"Vowels: {vowels}")
