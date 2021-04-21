def common_letters(string1, string2):

    common_letters = ",".join(set(string1).intersection(string2))
    return "Common letters:%s" % common_letters
