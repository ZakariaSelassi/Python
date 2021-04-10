import copy
def insertList(list):    
    listcpy = []
    for x in range(len(list)):
        if x < 5:
        #Insert permet d'insert des valeurs dans un tableau à partir d'un index donnée 
            listcpy.insert(x, list[x])
    return print(listcpy)

def addArray(list):     
    num = int(input("entrer un nombre : "));
    arr = []
    for x in list:  
        if x < num:
            # Append ajoute element dans un tableau
            arr.append(x)
    return print(arr)

list = [1,2,3,4,5,6,7,8,9,10]
insertList(list)
addArray(list)