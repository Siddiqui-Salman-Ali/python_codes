
def drawBoard(rows , columns):
    """The function takes in two input arguments
    rows (Odd Integer)
    columns (Odd Integer) 
    within certain range which specifies the number of elements that can fix into
    conosles at once. if the arguments passed are within the cosole limit
    then game board fields are formed, else the fucntion returns false"""
    if rows <22 and columns <86:
        for row in range(rows):
            if row%2 ==0:
                for col in range (1,columns+1):
                    if row %2 == 0 :
                        if col%2 ==0:
                            print("|" ,end= "")
                        elif col==columns:
                            print(" ")
                        else:    
                            print(" " ,end="")
            else:
                print("-"*columns)
    else:
        print("The value excedes the console size limit")
        return False


drawBoard(21,85)