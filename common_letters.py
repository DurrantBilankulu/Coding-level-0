def common_letters(string1, string2):

    common_letters = ",".join(set(string1).intersection(string2))
    return f"Common letters:{common_letters}"
