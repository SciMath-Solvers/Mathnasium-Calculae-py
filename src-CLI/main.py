import commands
import sys
def prompt():
    choice=int(input("1.add 2.divide 3.subtract 4.multiply 5.linear equations"))
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
while True:
    prompt()            



