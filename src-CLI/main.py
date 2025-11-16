# Module Imports
import asyncio as aio
import sympy as smp
import scipy as scp
import numpy as np

# File imports
import funcs as cmd
from funcs import l
from funcs import App



def main() -> None:
    running = True
    while running:
        l("-----------Mathnasium Calculae v1.0.0-----------")
        l("[1] Addition Solver (2 Inputs)")
        l("[2] Subtraction Solver (2 Inputs)") # So on, and so forth...
        l("[3] Division Solver (2 Inputs)")
        l("[4] Multiplication Solver (2 Inputs)")
        l("[5] WIP")
        l("[6] Expression Solver (2 Inputs)")
        l("[7] Exit")
        mmc = int(input("Choice: "))
        match mmc:
            case 1:
                x = input("X? ")
                y = input("Y? ")
                l(f"Value {x} + Value {y} Returns: {x + y}")
                break
            case 2:
                x = input("X? ")
                y = input("Y? ")
                l(f"Value {x} - Value {y} Returns: {x - y}")
                break
            case 3:
                x =  input("X? ")
                y = input("Y? ")
                l(f"Value {x} / Value {y} Returns: {x / y}")
                break
            case 4:
                cmd.multiply_prompt()
                break
            case 5:
                print("Work In Progress")
                input()
                break
            case 6: 
                cmd.exp()
                break
            case 7:
                running = False
            case 8:
                App.Info()
            case _:
                l("Invalid Option Selected, Please Try Again.")
        input()

aio.run(main())
