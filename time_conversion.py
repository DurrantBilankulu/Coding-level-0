def time_conversion(number):

    hours = number // 60
    minutes = number % 60
    if hours >= 2 or hours == 0:
        if minutes >= 2 or minutes == 0:
            time = f"{hours} hours, {minutes} minutes"
        else:
            time = f"{hours} hours, {minutes} minute"
    else:
        if hours < 2 and (minutes < 2 and minutes != 0):
            time = f"{hours} hour, {minutes} minute"
        else:
            time = f"{hours} hour, {minutes} minutes"
    return time
