# Circle
p = 3.14159265359

def areacircle(p, r):
    # Calculate the area
    areacircle = p * r * r
    return areacircle

def circumference(p, r):
    # Calculate the perimeter
    circumference = 2 * p * r
    return circumference

def maincircle():
    r = float(input('Enter radius of Circle: '))

    print("Area of Circle:", areacircle(p, r))
    print("Circumference of Circle:", circumference(p, r))

maincircle()