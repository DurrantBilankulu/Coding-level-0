def triangle_area(side1, side2, side3):

    semiperimeter = 0.5 * (side1 + side2 + side3)
    area = (
        semiperimeter
        * (semiperimeter - side1)
        * (semiperimeter - side2)
        * (semiperimeter - side3)
    ) ** 0.5
    return area
