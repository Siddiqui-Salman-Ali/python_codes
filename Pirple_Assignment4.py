myUniqueList = []
myLeftovers = []

def addListItem(listValue):
    """The function takes in single argument ,listValue
    and appends it to the lists based on the following 
    conditions:
        if the argument passed is unique , it is added to:
    myUniqueList and the function returns true.
    else the value is added to a different list of Leftovers
    and the function returns false."""
   
    if listValue not in myUniqueList:
        myUniqueList.append(listValue)
        print("\n After adding ",listValue," the unique list is now ",myUniqueList)
        return True
    
    else:
        myLeftovers.append(listValue)
        print("\n\tSince ", listValue ," is already added its moved to Leftovers ",myLeftovers)
        return False
    
#Calling function with different values to test the output
    
addListItem(1)
addListItem(2)
addListItem(3)
addListItem(4)
addListItem("Hello")
addListItem("Sam")




#addListItem(2)
#addListItem(4)
addListItem(3)
addListItem(4)
addListItem([2,1])
addListItem([1, 2])
addListItem("Hello")
addListItem([2,1])
