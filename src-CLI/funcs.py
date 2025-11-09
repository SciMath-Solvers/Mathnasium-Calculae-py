
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
    eq = input("enter equation,format in x + b = c\nex x + 1 = 9\n")
    print(eq)
    length = -1
    for letter in eq:
        length+=1
        match letter:
            case "x":
                eq.replace(" ","")
                coeff=eq.split("x")[0]
                print(f"COEF {coeff}")
                after_x=eq.split("x")[1]
                after = after_x.split("=")[1]
                
                      
def exp():
    """doesnt work"""
    exp = None
    while exp == None:
        exp = input("Enter All-in-One Expression: ") | ""
    res = eval(exp)
    return res

async def pcode():
    return await 0

def Text(ctx)->None:
    print(ctx)

def Choice()->int:
    opt = input("1.Add \n2.Divide \n3.Subtract \n4.Multiply \n5.Discontunied \n6. All-in-One (Includes CAS) \n7. Exit \n8. About")

    return int(opt)

