# Day 3 of 30 days of Python
"""
So it seems I missed his exercises and read the code instead. I've learnt my lesson now
I'll be going through thr .md files and do the exercises rather
"""
age = 25 # Declare 'age' as an integer variable
my_height = 182.4 # Declare 'my_height' as a float variable
complex_number = 1+2j # Declare 'complex_number' as a complex number

# First script
# I'm including my code asking user to enter height and base of a triangle and it'll calculate the area
base = int(input('Enter base: '))
height = int(input('Enter height: '))

area_of_triangle = 0.5 * height * base
print(f'The area of triangle is: {area_of_triangle}')


# Second Script
# This calculates the perimeter of the triangle
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

perimeter = a + b + c
print(f'The perimeter of triangle is: {perimeter}')


# Third Script. Calculating the area of a circle
radius = int(input('Enter radius: '))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print(f'The area of triangle is: {area}')
print(f'The circumference of triangle is: {circumference}')


# Printing the length of a string
print(len('python'))
print(len('dragon'))
print('on is in dragon', 'on' in 'dragon')

# I'll edit and add more