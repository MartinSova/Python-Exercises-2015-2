from follow import follow
from exturtle import*

def gosper(S):
	
	"""The gosper(S) function rewrites the string S according to
	the Gosper curve SRS, where 'E' is the axiom, and E -> ELFLLFRERREERFL,
	F -> RELFFLLFLERRERF, L->L, and R->R."""
	
	l = list(S)
	for y,x in enumerate(l):
		if x=='E':
			l[y]='ELFLLFRERREERFL' # 'E' replaced by 'ELFLLFRERREERFL'
		if x == 'F':
			l[y]='RELFFLLFLERRERF' # 'F' replaced by 'RELFFLLFLERRERF'
	return ''.join(l) # L and R do not have to be addressed because they are not altered in the Gosper curve SRS

def rewrite(num, S):
	
	"""The rewrite function takes a 'num' argument, which takes an integer
	value for how many times you want to rewrite the Gosper curve SRS,
	and then prints the rewritten string (rewritten 'num' number of times).
	The starting string is argument S (in most cases, the axiom 'E')."""

	for i in range(num): # S will be rewritten 'num' number of times
		print("n =", i , S) # n represents how many times S was rewritten
		S = gosper(S)
	print("n =", num , S) # final S value is printed

def draw(S, step, angle, number):

	"""The draw function takes a 'number' argument, which takes an integer
	value for how many times you want to rewrite the Gosper curve SRS
	the starting string, argument S, before using the function 'follow' to print the
	turtle graphics using the letters of the rewritten string, 'number' times.
	The step and angle arguments correspond to the steps and angles you want the
	turtle to execute for each defined letter in the follow function."""

	for i in range(number): # S string is rewritten 'number' number of times according to gosper curve SRS
		S = gosper(S)

	fred = Turtle()

	follow(fred, S, step, angle) # rewritten string S is used by follow function to draw using turtle graphics


if __name__ == "__main__":
	draw('E', 4, 60, 5)


