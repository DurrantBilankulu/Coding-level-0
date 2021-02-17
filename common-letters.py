#a function that takes two strings as input, and outputs the common characters/letters that they share

def common_letters(string1,string2):
    
    common_letters= ','.join(set(string1).intersection(string2))
    return "Common letters:%s"%common_letters
   

