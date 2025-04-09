#input a string and count the vowel

user_input = input("enter a word: ")
vowel_count = 0
vowel = "aeiouAEIOU"

for letter in user_input:     #get a letter from the input string
    if letter in vowel:        
        vowel_count += 1

print("The count of vowel is: ", vowel_count)
