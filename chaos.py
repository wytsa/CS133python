dimpoef main():
    print("This pogram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))
    for i in range(n):
        x = 2 * x * (1 - x)
        print(x)

main()



        
