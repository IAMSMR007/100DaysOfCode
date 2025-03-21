import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

let=""
for i in range(0,nr_letters):
    x=random.randint(0,len(letters)-1)
    y=letters[x]
    let+=y

sym=""
for i in range(0,nr_symbols):
    x=random.randint(0,len(symbols)-1)
    y=symbols[x]
    sym+=y

num=""
for i in range(0,nr_numbers):
    x=random.randint(0,len(numbers)-1)
    y=numbers[x]
    num+=y
print("Your Easy password")
easy=(let+sym+num)
print(easy)
print("Your Hard password")
hard=""
for k in range(0,len(easy)):
    a=random.randint(0,len(easy)-1)
    b=easy[a]
    hard+=b

print(hard)
