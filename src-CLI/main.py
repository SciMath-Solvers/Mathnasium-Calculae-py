# Module Imports
import asyncio as aio
import sympy as smp
import scipy as scp
import numpy as np
import matplotlib as mpl

# File imports
import funcs as cmd
from funcs import l
from funcs import App

running = True

async def main() -> None:
    while running:
        l("-----------Mathnasium Calculae v1.0.0-----------")
        l("[1] Addition Solver")
        l("[2] Subtraction Solver") # So on, and so forth...
        l("[3] Division Solver")
        l("[4] Multiplication Solver")
        l("[5] WIP")
        l("[6] Expression Solver")
        l("[7] Exit")
        mmc = input("Choice: ")
        match mmc:
            case 1:
                x = input("X? ")
                y = input("Y? ")
                l(f"Value {x} + Value {y} Returns: {x + y}")
            case 2:
                x = input("X? ")
                y = input("Y? ")
                l(f"Value {x} - Value {y} Returns: {x - y}")
            case 3:
                cmd.division_prompt()
            case 4:
                cmd.multiply_prompt()
            case 5:
                print("Work In Progress")
            case 6: 
                cmd.exp()
            case 7:
                running = False
            case 8:
                App.Info()
        input()
    return await l(f"Proccess Completed with Return Code: {cmd.pcode()}")






