# Ask user for their name
name = input("What is your name? ")

# Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.capitalize()
#Make all the letters of the words in the sentence capital
name = name.title()

# Say hello to user
print(f"Hello, {name}")