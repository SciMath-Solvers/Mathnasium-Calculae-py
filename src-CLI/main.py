import commands
import asyncio as aio
async def prompt()->void:
    choice=int(input("1.Add \n2.Divide \n3.Subtract \n4.Multiply \n5.Linear Equations \n6. All-in-One (Includes CAS)"))
    match choice:
        case 1:
            commands.addition_prompt()
        case 2:
            commands.division_prompt()
        case 3:
            commands.subtraction_prompt()
        case 4:
            commands.multiply_prompt()
        case 5:
            commands.lineareq()
        case 6: 
            exp = Input("Your Expression: ")
            res = eval(exp)
            print(f'Your All-in-One Expression has Simplified into: {res}')


