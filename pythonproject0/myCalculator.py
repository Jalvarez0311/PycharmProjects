
def MathGetter():
    while True:        
        try:
            calc = str(input("Insert what you want to do in this calculator: "))
        except ValueError:
            print("That is not an accepted value")
            continue
        else:
            break
    return calc


while True:
    try:
        var1 = int(input("Input your first variable: "))
    except ValueError:
        print("That is not an accepted value")
        continue
    else:
        break

while True:        
    try:
        var2 = int(input("Input your second variable: "))
    except ValueError:
        print("That is not an accepted value")
        continue
    else:
        break

while True:
    calc = MathGetter()

    if calc == '+':
        answer = var1 + var2
        
    if calc == '-':
        answer = var1 - var2
        
    if calc == '*':
        answer = var1 * var2
        
    if calc == '/':
        answer = var1 / var2

    try:
        print(answer)
    except NameError:
        print("That is not an accepted value")
    else: 
        break


