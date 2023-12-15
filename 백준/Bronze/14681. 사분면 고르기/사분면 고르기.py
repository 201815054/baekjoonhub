integer_x = int(input())
integer_y = int(input())

if integer_x>0 and integer_y>0:
    print(1)
elif integer_x<0 and integer_y>0:
    print(2)
elif integer_x<0 and integer_y<0:
    print(3)
else:
    print(4)
