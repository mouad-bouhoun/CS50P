# Ask user for their name
#name = input("What is your name? ")

# Say hello to user
#print("Hello,", name , end="")
#print(name)
#print("Welcome,", name , sep="???")
#print("Hello, \"friend\"")

#print(F"Hello, {name}")
#print("Hello,", name)
#print("Hello, "+ name)
def hello(to="friend"):
    print("Hello,", to)

hello()
name = input("What is your name? ")
hello(name)