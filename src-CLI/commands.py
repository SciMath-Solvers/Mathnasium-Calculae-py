
#basic math


def addition_prompt():
    """Addition.
    """
    a = int(input(">_< +_?\n"))
    b = int(input(f"{a} + >_<?\n"))
    print(f"= {a + b}")
def subtraction_prompt():
    """Subtraction.
    """
    a = int(input(">_< -_?\n"))
    b = int(input(f"{a} - >_<?\n"))
    print(f"= {a - b}")
def division_prompt():
    """Division.
    """
    a = int(input(">_< /_?\n"))
    b = int(input(f"{a} / >_<?\n"))
    print(f"= {a / b}")
def multiply_prompt():
    """Multiplication.
    """
    a = int(input(">_< *_?\n"))
    b = int(input(f"{a} * >_<?\n"))
    print(f"= {a / b}")
def lineareq():
    """solves basic linears
    """
    eq = input("enter equation,format in x + b = c\nex x + 1 = 9\n leave a space before please")
    length = -1
    for letter in eq:
        length+=1
        match letter:
            case "x":
                if eq[-(length-1)] != "":
                    coeff=eq[-(length-1)]
                    print(f"{coeff}")
                else:
                    print("no coeff")
            case "=":
                after = eq[length+1]
                print(f"{after}")
                
