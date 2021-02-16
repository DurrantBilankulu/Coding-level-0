#This function takes in 3 numbers/side, then use them to calculate area of triangle

def area_of_triangle(a,b,c):     #a,b,c are sides of the triangle
    s=0.5*(a+b+c)   #semiperimeter
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area

print(area_of_triangle(3,4,5))