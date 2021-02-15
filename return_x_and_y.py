#A function that prints x and y values given some conditions

def print_x_and_y(x_value,y_value):
    print (x_value) 
    print (y_value)
    x_value = x_value+3
    y_value = y_value+x_value
    print(x_value)
    return y_value

print(print_x_and_y(0,1))