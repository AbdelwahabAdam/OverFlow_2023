
x = input("Name: ")
database = {'a':[[0,1,0],[0,1,0],[1,0,1]],
            'n':[[1,1,1],[1,0,1],[1,0,1]],
            's':[[1,1,1],[1,1,1],[1,1,1]]
            }
for i in x:
    #print(database[i])
    if database[i][0] == [0,1,0]:
        print("   " + " * " + "   ")
    elif database[i][0] == [1,0,1]:
        print(" * " + "   " + " * ")
    elif database[i][0] == [1,1,1]:
        print(" * " + " * " + " * ")
    
    if database[i][1] == [0,1,0]:
        print("   " + " * " + "   ")
    elif database[i][1] == [1,0,1]:
        print(" * " + "   " + " * ")
    elif database[i][1] == [1,1,1]:
        print(" * " + " * " + " * ")
    
    if database[i][2] == [0,1,0]:
        print("   " + " * " + "   ")
    elif database[i][2] == [1,0,1]:
        print(" * " + "   " + " * ")
    elif database[i][2] == [1,1,1]:
        print(" * " + " * " + " * ")




    
