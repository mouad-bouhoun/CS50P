def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
#    return n ** 3
    return pow(n, 4)

main()