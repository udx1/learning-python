#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
number_of_letters = len(letters)
number_of_numbers = len(numbers)
number_of_symbols = len(symbols)
password = ""
for i in range(0,nr_letters):
  password += random.choice(letters)

for i in range(0,nr_symbols):
  password += random.choice(symbols)

for i in range(0,nr_numbers):
  password += random.choice(numbers)

print(f"Simple password= {password}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

desired_password_length = nr_letters + nr_numbers + nr_symbols
#print(f"Desired Password length = {desired_password_length}")

password2 = ""
while len(password2) != desired_password_length:
  random_pick = random.randint(1,3)
  #print(f"Password2 length={len(password2)} and random_pick = {random_pick}")
  if random_pick == 1:
    # choose a letter
    if nr_letters > 0:
      password2 += random.choice(letters)
      nr_letters -= 1
  elif random_pick == 2:
    # choose a number
    if nr_numbers > 0:
      password2 += random.choice(numbers)
      nr_numbers -= 1
  else:
    # choose a symbol
      if nr_symbols > 0:
        password2 += random.choice(symbols)
        nr_symbols -= 1

print(f"Hardpassword = {password2}")
#print(f"Length of Hardpassword = {len(password2)}")
