
def comparision (a, b ,c):
    """The function takes in three
    numbers in any form integer, float or
    string:
        a , b , c
    converts them into float and compares
    them, if two or more numbers are equal
    the function returns boolean True else
    False.
    """
    a = float (a)
    b = float (b)
    c = float (c)
    
    #Displaying the converted input arguments to the function
    
    print("\n The input values to the function are {} , {} and {}".format(a,b,c))
    
    if a != b != c:
        return False
    else:
        return True

#Calling function coparision with different inputs to verify the output 
a = comparision(1 ,"2" ,2)
print("if two or more numbers are equal? " ,a)


a = comparision(5 ,"5" ,5.0)
print("if two or more numbers are equal? " ,a)

a = comparision(1 ,-2 ,2)
print("if two or more numbers are equal? " ,a)

a = comparision(-2.1 ,"2.1" ,2.1)
print("if two or more numbers are equal? " ,a)

a = comparision(15 ,17 ,18)
print("if two or more numbers are equal? " ,a)