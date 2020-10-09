# program to find whether a number is odd or even using a function

def oddEven(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

n = input("Enter a number:")
number = int(n)
oddEven(number)