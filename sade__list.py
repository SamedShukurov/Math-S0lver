#Programda   meqsed sade ededleri bir massive yigib ekrana çıxartmaq
import math
sade=[2] #sade ededleri yığmaq ucun massiv
def f(n):
    while n>0:
        for i in range (2,int(math.sqrt(n))+1):
            if n%i == 0:
                break
            else:
                if i== int(math.sqrt(n)) :
                    sade.append(n)
                else:
                    continue
        n-=1
    sade.sort()  
def sade_list():
    n = int(input("Natural ədəd daxil edin: "))
    if n==0:
        print("0 natural ədəd deyil.\n")
    elif n==1:
        print("1 nə sadə nədə mürəkkəb ədəddir.\n")
    elif n==2:
        print("Bu ədəd default olaraq proqramı icra etmək üçün qeyde alinib ve bu eded sadedir. \n")
    elif n < 0:
        print("Zehmet olmasa natural eded daxil edin.\n")
    else:
        f(n)
        cont = input("Continue? ")
        if cont.lower() == "yes" or "y":
            for num in sade:
                print(num)
            print("See ya ;)")
        elif cont.lower() == "no" or "n":
            print(sade)
        else:
            print("wrong chose between y and n (yes and n)!")