def algae(S):
	"""The function algae(S) takes as its argument a string and returns
	the string rewritten according to A -> AB and B -> A"""
	l = list(S)
	for y,x in enumerate(l):
		if x=='A':
			l[y]='AB' # 'A' is replaced by 'AB'
		if x == 'B':
			l[y]='A' # 'B' is replaced by 'A'
	return ''.join(l)



def find(rewrite, r, length, l):
	""" For argument 'rewrite', the function will print the string rewritten 'rewrite'
	number of times from the starting string 'r', according to the algae sequence.
	For argument 'length', the function will print the length of a string rewritten
	'length' number of times from the starting string 'l', according to the algae sequence.
	In both cases, in this example, the starting string will be the axiom 'E'."""

	 # I arranged the code so the function prints 'n', the number of times the string was rewritten, next to its respective string value
	for i in range(rewrite):
		print("n =", i , r)
		r = algae(r)
	print("The first", rewrite, "rewritings of the algae sequence gives:",r) # the last rewrite (after 'rewrite' number of times) is printed

	for i in range(length): # find length of a string rewritten 'length' number of times from 'l' using the algae sequence
		l = algae(l)
	print("The length of the string corresponding to", length, "rewritings of the algae sequence is",str(len(l)) + ".")
	
if __name__ == "__main__":
	find(10,'A',30,'A')




