#The function takes only string arguments, e.g "Durrant", then outputs the string Hello Durrant!
#The function will also ask you to try again if the argument is not a string

def hello(name):
    
    if type(name)!=str:
        return "The argument must be a string,try again"
    else:
        return "Hello %s!"%name
print(hello("Durrant"))
