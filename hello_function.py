def hello(name):

    if type(name) != str:
        result = "The argument must be a string,try again."
    else:
        result = f"Hello {name}!"
    print(result)
    
