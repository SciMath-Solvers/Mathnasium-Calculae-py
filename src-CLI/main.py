# Module Imports
import asyncio as aio
import sympy as smp
import scipy as scp
import numpy as np

# File imports
import funcs as cmd
from funcs import l
from funcs import App


async def main()->int:
    l("-----------Mathnasium Calculae v1.0.0-----------")
    l("[1] Addition Solver")
    l("[2] Subtraction Solver") # So on, and so forth...
    match choice:
        case 1:
            cmd.addition_prompt()
        case 2:
            cmd.division_prompt()
        case 3:
            cmd.subtraction_prompt()
        case 4:
            cmd.multiply_prompt()
        case 5:
            print("not fucntional anymore")
        case 6: 
            cmd.exp()
        case 7:
            return await print(f"Proccess Completed with Return Code: {cmd.pcode()}")
            goto .end
        case 8:
            _.App.Info()
    print(f"Proccess Completed with Return Code: {cmd.pcode()}")
    input()
    

    





