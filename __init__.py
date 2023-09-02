from sade__list  import *
from faktorial import *
from termcolor import colored
from pyfiglet import figlet_format


def print_logo():
    print("\n",(colored(figlet_format("Hello"), color="light_magenta")),(colored(figlet_format("To"), color="red")),(colored(figlet_format("M@th S0lver"), color="blue")))
def initilation():
    print_logo()
    while True:
        print("Select: (0 to exit)")
        print("\n\t1.Sadə ədədlərin tapılması proqramı(list)\n\t2.Sadə ədədlərin tapılması proqramı(boolean)\n\t3.Faktorial\n\t4.Say Sistemləri\n")
        chose = int(input("Chose one: "))
        if chose == 0:
            print(colored(figlet_format("Bye : ) \n\tSee ya soon"), color="red"))
            break
        if chose == 1:
            sade_list()
        elif chose == 2:
            print("Working on it")
        elif chose == 3:
            faktorial()
        elif chose == 4:
            print("Soon...")
        else:
            print("emm ?")