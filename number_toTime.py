def number_to_time(number):
    hours = number // 60
    minutes = number % 60
    if hours >= 2:
        if minutes >= 2:
            return "%d hours, %d minutes" % (hours, minutes)
        else:
            return "%d hours, %d minute" % (hours, minutes)
    else:
        if hours < 2 and minutes < 2:
            return "%d hour, %d minute" % (hours, minutes)
        else:
            return "%d hour, %d minutes" % (hours, minutes)
