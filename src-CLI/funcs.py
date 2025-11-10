
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
    for letter in eq:
        match letter:
            case "x":
                eq.replace(" ","")
                coeff=eq.split("x")[0]
                print(f"COEF {coeff}")
                after_x=eq.split("x")[1]
                after_equal = after_x.split("=")[1]
                after_x= after_x.split("=")[0]
                print(after_x)
                print(after_equal)
                for letter in after_x:
                    match letter: 
                        case "+":
                            
                            after_x=int(after_x.split("+")[1])
                            print(int(after_equal)-after_x)
                        case "-":
                    
                            after_x=int(after_x.split("-")[1])
                            print(int(after_equal)+after_x)
                      
def exp():
    #eval does not work
    exp = None
    while exp == None:
        exp = input("Enter All-in-One Expression: ") | ""
    res = eval(exp)
    return res

async def pcode():
    return await 0

def l(ctx) -> None:
    print(ctx)
    return None

class App:
    def __init__(self,Info):
        self.Info = Info
        Info = f'{Desc()}\n{Version()}\n{Lang()\n{Type()}'
        l( Info )
    def Desc()->str:
        return "Description:\n\tMathnasium Calculae is a Mathematics Solver for anything with Python Terminal"
    def Version() -> str:
        return "Version:\n\tv1.0.0"
    def Lang() -> str:
        return "Language:\n\tPython\n\tENGLISH (US)"
    def Type() -> str:
        return "Type:\n\tCLI (Command-Line Interface)"






