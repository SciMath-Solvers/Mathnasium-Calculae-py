import commands as cmd
import asyncio as aio
from deco import aio
import app as _

@aio
async def main()->int:
    choice = int(input("1.Add \n2.Divide \n3.Subtract \n4.Multiply \n5.Linear Equations \n6. All-in-One (Includes CAS) \n7. Exit \n8. About"))
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
            cmd.lineareq()
        case 6: 
            cmd.exp()
        case 7:
            return
        case 8:
            _.App.Info()
    return await print(f"Proccess Completed with Return Code: {cmd.pcode()}")


