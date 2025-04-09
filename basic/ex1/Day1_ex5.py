# user_input = input("Enter a 3 digit number: ")

# user_input= int(user_input)

# print(user_input)
# print("This is an even number")


number = input( "enter a number: ")

# number = int(number)

even_number_count = 0

for digit in number:
  if int(digit) % 2 == 0:
        even_number_count += 1

print("Even numbers are", even_number_count)




    

