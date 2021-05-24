# 1. Write a Python program which accepts the radius of a circle from the user and
#    compute the area.

'''
This program will take the radius of a circle as input from user and
display the area of circle accordingly
'''

def calculateArea (rad):
    import math
    area = math.pi * math.pow(int(rad), 2) #Calculating area of circle
    print(f'The area of a circle with {rad} radius is {area:.3f}')

def main():
    print("Welcome to circle area calculator")
    radius = input("Please enter the radius of circle : ")  #Taking input from user
    calculateArea(radius)

main()
