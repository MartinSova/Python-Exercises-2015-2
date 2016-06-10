from follow import follow
from exturtle import*

def sierpinski(S):
	"""The sierpinski(S) function rewrites the string S according to
	the sierpinski curve SRS; E -> FLELF and F -> ERFRE."""
	l = list(S)
	for y,x in enumerate(l): # this for loop iterates over list l and replaces 'E' and 'F' according to sierpinski curve SRS
		if x=='E':
			l[y]='FLELF' # 'E' replaced by 'FLELF'
		if x == 'F':
			l[y]='ERFRE' # 'F' replaced by 'ERFRE'
	return ''.join(l) # 'L' and 'R' do not have to be addressed because they are not altered in the sierpinski curve SRS

def draw(S, step, angle, number):

	"""The draw function takes a 'number' argument, which takes an integer
	value for how many times you want to rewrite the sierpinski curve SRS
	the starting string, argument S, before using the function 'follow' to print the
	turtle graphics using the letters of the rewritten string, 'number' times.
	The step and angle arguments correspond to the steps and angles you want the
	turtle to execute for each defined letter in the follow function."""

	for i in range(number): # S string is rewritten 'number' number of times according to sierpinski curve SRS
		S = sierpinski(S)

	fred = Turtle()

	follow(fred, S, step, angle)

if __name__ == "__main__":
	draw('E', 2, 60, 8)

