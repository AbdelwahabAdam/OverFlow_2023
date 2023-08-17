x=input("enter your name: ")
y={'m':[[1,0,1],[1,1,1],[1,0,1]],'o':[[1,1,1],[1,0,1],[1,1,1]],'h':[[1,0,0],[1,1,1],[1,0,1]]}


try:
    for i in x:
#letter 1:
        if y[i][0] == [1,0,1]:
            print(" * " + "  " + "  * ")
        elif y[i][0] == [1,1,1]:
            print(" * " + " * " + " * ")
        elif y[i][0] == [1,0,0]:
            print(" * " + "  " + "  ")
#letter 2:
        if y[i][1] == [1,1,1]:
            print(" * " + " * " + " *  ")
        elif y[i][1] == [1,0,1]:
            print(" * " + "   " + " * ")
#letter 3:
        if y[i][2] == [1,0,1]:
            print(" * " + "   " + " * ")
            print("                   ")
        elif y[i][2] == [1,1,1]:
            print(" * " + " * " + " * ")
            print("                   ")

except:
    print("name is soon to be added to database")