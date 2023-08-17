# METHOD 1
# This method doesn't work properly

    name = input("enter your name: ")  # >> i as the character
database = {'m': [[1, 1, 1], [1, 1, 1], [1, 0, 1]],
            'o': [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            'h': [[1, 0, 0], [1, 1, 1], [1, 0, 1]]
            }

for i in name:
    if database[i][0] == [1, 1, 1]:
        print("* " + " * " + " * ")
    elif database[i][0] == [1, 0, 1]:
        print("* " + "  " + "  * ")
    elif database[i][0] == [1, 0, 1]:
        print("* " + "  " + "  * ")

    if database[i][1] == [1, 1, 1]:
        print("* " + " * " + " * ")
    elif database[i][1] == [1, 0, 1]:
        print("* " + "  " + "  * ")
    elif database[i][1] == [1, 1, 1]:
        print("* " + " * " + "  * ")

    if database[i][2] == [1, 0, 0]:
        print("* " + "  " + "  ")
    elif database[i][2] == [1, 0, 1]:
        print("* " + " * " + "  * ")
    elif database[i][2] == [1, 0, 1]:
        print("* " + "  " + "  * ")

#  METHOD 2 :
# Although this method is not professional, I tried it.
x = input("name :")
M = (" * " + " * " + " * ""\n") + (" * " + " * " + " * ""\n") + (" * " + "  " + "  * ""\n")
O = ("* " + " * " + " * ""\n") + (" * " + "   " + " * ""\n") + (" * " + " * " + " * ""\n")
H = ("* " + "   " + " * ""\n") + (" * " + " * " + " * ""\n") + (" * " + "  " + "  * ""\n")
# print(M, O, H)

if x == 'M':
    print(M)
if x == 'M''O':
    print(M, O)
if x == 'M''O''H':
    print(M, O, H)
elif x == 'O':
    print(O)
elif x == 'H':
    print(H)
else:
    print("ERROR!!")
