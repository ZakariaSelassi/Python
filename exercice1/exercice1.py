import datetime
def ask():
    name = input('Give your name :')
    # Attention si resulter entrer est un nombre le resultat obtenu sera un string !
    age = int(input('Give your age : '))
    now = datetime.datetime.now()
    calculate = str((now.year-age+100))
    msg = str((f"Your name is {name} and your age {age} you will have 100 years in {calculate} \n"))
    return msg


def askNumber(m):
    n = int(input('Give me a number :'))
    print((m) * n)

m = ask()
askNumber(m)