def maximum(number1, number2, number3):

    if number1 >= number2 and number1 >= number3:
        largest_number = number1

    elif number2 >= number1 and number2 >= number3:
        largest_number = number2
    else:
        largest_number = number3

    return largest_number
