def hello(name):

    if type(name) != str:
        return "The argument must be a string,try again"
    else:
        return "Hello %s!" % name
