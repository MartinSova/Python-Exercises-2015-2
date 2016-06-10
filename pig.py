import string
import sys

letters = string.ascii_letters

consonants = set(letters).difference(set(('a','e','i','o','u','y')))
vowels = set(('a','e','i','o','u'))

y = ['y', 'Y']

def find_vowel(wordlist):
	""" I've created a find_vowel(wordlist) function, which iterates over a list of letters
	and finds the index of the first vowel. This helps me to make the pig(word) 'prettier'."""
	for indx, letter in enumerate(wordlist):
		if [x for x in letter if x in vowels]:
			return indx

def pig(word):
	"""pig(word) takes a single word as a string and returns the Pig Latin for the word,
	assuming the rules provided by the ca2.pdf"""
	
	if not word.isalpha():
		print("You have not entered a valid string of letters.")
		sys.exit()
		# I have chosen to exit the program if the input contains any other characters than letters

	word = word.lower() # transalted word to lowercase for nicer code

	wordlist = list(word)

	if any(x in word for x in y): # this 'if' statement accounts for all possibilities of words with 'y' in them
		if any(x in wordlist[0:wordlist.index('y')] for x in vowels) or any(x in wordlist[0] for x in y):
		# if there is a vowel before 'y', or 'y' is the first letter (hence there is a vowel)
			indices = wordlist[0:find_vowel(wordlist)]
			a = ''.join(indices) # this will join the letters that are moved to end of the word for simplicity
			del wordlist[0:find_vowel(wordlist)]
			f = ''.join(wordlist),a,'ay' # I prefer to translate the word to lowercase Pig Latin
			return ''.join(f)
		# otherwise, if 'y' is not first letter or there is not a vowel before 'y' this will execute
		indices = wordlist[0:wordlist.index('y')] 
		a = ''.join(indices) # join all letters before 'y'
		del wordlist[0:wordlist.index('y')]
		f = ''.join(wordlist),a,'ay'
		return ''.join(f)

	elif any(x in wordlist[0] for x in consonants): # if word starts with consonants
		if any(x in wordlist for x in vowels):  # if there are vowels in the word following code executes
			find_vowel(wordlist)
			indices = wordlist[0:find_vowel(wordlist)]
			a = ''.join(indices)
			del wordlist[0:find_vowel(wordlist)]
			f = ''.join(wordlist),a,'ay'
			return ''.join(f)
		# if there are no vowels or 'y' in the word, and it starts with a consonant, this code will execute
		a = wordlist[0]
		wordlist.pop(0)
		f = ''.join(wordlist),a,'ay'
		return ''.join(f)

	elif wordlist[0] in vowels: # if the word starts with a vowel, this code will execute
		return word + "way"

def test_pig():
	"""The test_pig() function tests each of the examples given in ca2.pdf and uses assert to raise an
	exception if the result is incorrect. If no exception is raised, then a string saying that pig(word)
	correctly translates words to Pig Latin is printed."""
	assert pig('happy') == 'appyhay'

	assert pig('duck') == 'uckday'

	assert pig('glove') == 'oveglay'

	assert pig('evil') == 'evilway'

	assert pig('eight') == 'eightway'

	assert pig('yowler') == 'owleryay'

	assert pig('crystal') == 'ystalcray'

	print('The function pig(word) correctly translates the example words to Pig Latin.')


def line():
	"""This function repeatedly asks the user for a line of English and prints
	the corresponding Pig Latin translation. The program stops when the user inputs
	an empty line."""

	line = input("Write a line of English that you want to translate to Pig Latin: ")
	# by using 'input' the input returns the verbatim string entered by the user (don't need quotations when typing in terminal)
	while line.strip() != '': # while loop ends on an empty line
		words = line.split() # each word in 'line' is put into a list 'words' 
		list_words = []
		for i in words:
			new_word = pig(i)
			list_words.append(new_word) # every word that is translated is appended to a list
		print(' '.join(list_words)) # final list of translated words is joined
		line = input("If you want, write another line of English that you want to translate to Pig Latin, else leave an empty line: ")

if __name__ == "__main__":
	line()




