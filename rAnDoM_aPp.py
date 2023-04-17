# Dolan, Austin
# ICS 110P Assignment 09
# October 19 2022
# Program uses functions to take input from user and display alternating letters in capital and lowercase letters, arrange 3 words in alphabetical order, and display the users initials.


def phrase_format_tool(user_phrase):
	# Use input from user and dispay alternating letters in capital and lowercase letters
	phrase = ""
	# Loop through each letter in user_phrase and if index is even make uppercase, if odd make lowercase
	for letter in range(len(user_phrase)):
		if not letter % 2:
			phrase = phrase + user_phrase[letter].upper()
		else:
			phrase = phrase + user_phrase[letter].lower()
	# Output new funky phrase
	print("Your new funny formatted phrase is: {}".format(str(phrase)))

def alph_order(word_one, word_two, word_three):
	# Compare given words and display in alphabetical order
	if word_one < word_two < word_three:
		print("Your three words in alphabetical order read: %s, %s, %s" % (word_one, word_two, word_three))
	elif word_one < word_three < word_two:
		print("Your three words in alphabetical order read: {}, {}, {}".format(word_one, word_three, word_two))
	elif word_two < word_one < word_three:
		print(f"Your three words in alphabetical order read: {word_two}, {word_one}, {word_three}")
	elif word_two < word_three < word_one:
		print(f"Your three words in alphabetical order read: {word_two}, {word_three}, {word_one}")
	elif word_three < word_one < word_two:
		print(f"Your three words in alphabetical order read: {word_three}, {word_one}, {word_two}")
	else:
		print(f"Your three words in alphabetical order read: {word_three}, {word_two}, {word_one}")

def initial_generator(first_name, last_name):
	# Take index[0] of first and last name and output inbetween "."
	initials = f"\nYour initials are: {first_name[0]}.{last_name[0]}."
	return initials


def main():
		try:
			# Welcome user and ask their name
			user_name = input("Hello and welcome to my program.\n What is your name? ")
			play = input(f"\n{user_name}, My program has 3 operations.\n Would you like to try one? (yes or no) ")
			prompt1 = "\nWant to play again? (yes or no) "
			prompt2 = "\nDo you want to try the program again? (yes or no) "
			# Loop while user doesn't enter no
			while play != 'no':
				if play == 'yes':
					# Take input from user to perform function 1, 2, or 3
					choice = int(input("\nOkay! I can perform 3 different opperations! The things I can do are:\n  1. FoRmAt yOuR TeXt sO It lOoKs lIkE ThIs\n  2. Put any three words you give me in alphabetical order\n  3. Print out your initials\n\nWhich operation would you like to perform? (1, 2, or 3) "))
					if choice == 1:
						user_phrase = input("\nOkay! You choose my text format function. I can take any text input and FoRmAt It To LoOk LiKe ThIs.\n  What phrase/text would you like to format? ")
						phrase_format_tool(user_phrase)
						play = input(prompt1)
					elif choice == 2:
						# Use method .lower to change all strings to lowercase to compare in alphabetical order
						print("\nOkay! You choose to compare 3 words and I will show you how they would display in alphabetical order.  This program works best if you input 3 words that start with different letters!")
						word_one = input("First word: ").lower()
						word_two = input("Second word: ").lower()
						word_three = input("Third word: ").lower()
						alph_order(word_one, word_two, word_three)
						play = input(prompt1)
					elif choice == 3:
						print("\nOkay! This program can take your full name(first and last) and output your initials!")
						first_name = input("What is your first name? ")
						last_name = input("What is your last name? ")
						print(initial_generator(first_name, last_name))
						play = input(prompt1)
					else:
						# If user doesn't enter 1, 2, or 3 tell them their response is invalid
						print("\nThat is not one of my choices!")
						play = input(prompt2)
				else:
					# If user doesn't enter yes or no tell them their response is invalid
					print(f"\n{play} is not a valid response.")
					play = input(prompt2)
		except ValueError as e:
			print("\nThat is not a valid number. Please try again.")
			print("Error:", end = " ")
			print(e)

		# After loop breaks say Goodbye
		print("\nThank's for playing! Goodbye")

main()
