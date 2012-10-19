from time import *

x = int
return x

##def timer():
##    #x = eval(input("how many seconds is the countdown? "))
##    for i in range(x, -1, -1):
##        print(i)
##        sleep(1)
##    print("The clock has gone off")
    
def main(x):
    for i in range(x, -1, -1):
        print(i)
        sleep(1)
    print("The clock has gone off")

main()
    
