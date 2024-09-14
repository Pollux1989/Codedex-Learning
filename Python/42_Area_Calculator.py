# Write code below 💖
### Area Calculator
print('==================')
print('42.Area Calculator 📐 - ⏹️ - ⭕')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

shape = float (input('Which Shape: '))

if shape == 1:
    base = float(input('Base: '))
    height = float(input('Height: '))
    triangle_area = (base * height / 2)
    print('The Triangle area is: ', triangle_area)
elif shape == 2:
    length = float(input('Length: '))
    width = float(input('width: '))
    rectangle_area = (length * width)
    print ('The Rectangle area is: ', rectangle_area)
elif shape ==3:
    side = float(input('Side: '))    
    square_area = (side **2)
    print('The square area is: ', square_area)
elif shape == 4:
    radius = float(input('Radius: '))    
    import math
    circle_area = (math.pi *(radius ** 2))
    print('The Circle Area is: ', circle_area)
elif shape == 5    :
    print("Thanks for use the Area Calculator")
else:
    print(shape)




