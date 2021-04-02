def askNumber():
    num = int(input("number : "))
    print(f"Your num is : {num}")
    return num   
    
def verifyOddEven(num):       
    # verification si impaire
    if num % 2:
        print("This is an even number !")
    if num % 4 == 0:
        print("This a multiple of 4")
    else:
        print("this is an odd number !")
def checkNumber():
    num = int(input("number : "))
    check = int(input("number : "))
    print(f"Your nums are : {num} and {check}")
    if num % check == 0:
        print(f"number {num} is divisible by {check}")
    else:
        print(f"number {num} is not divisible by {check}")
## call function        
##num = askNumber()
#verifyOddEven(num)
checkNumber()
     