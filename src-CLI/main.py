# Module Imports
import asyncio as aio
from goto import with_goto

# File imports
from deco import aio
import app as _
import funcs as cmd



@with_goto
@aio
async def main()->int:

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
    
    goto .start
    label .end
    




