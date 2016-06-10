from exturtle import*

def follow(t, S, step, angle):
	"""The 'follow' function causes the turtle, t, to draw the path
	described by the string S. The argument 'step' specifies the number
	of steps that the turtle draws forward for an E or F symbol and the
	'angle' argument specifies the angle through which the turtle rotates
	left or right ('L' or 'R', respectively)."""
	t = Turtle()
	list(S)
	right(t, 180) # so the sierpinski prints upwards
	t.speed(100) # adjust speed so the turtle draws faster
	hideturtle(t) # hide turtle during drawing
	for i in S:
		if i == 'F' or i == 'E':
			t.forward(step) # turtle moves forward 'step' steps for and 'F' or an 'E' letter in S
		elif i == 'L': # turn left by 'angle' degrees for letter 'L'
			t.left(angle) 
		elif i == 'R': # turn right by 'angle' degrees for letter 'R'
		# I could use 'else', but than I assume that an axiom would only include one of 'E', 'F', 'L', or 'R' letters; if not, the "else" command would still execute, which would not agree with the 'follow' function rules
			t.right(angle)
	showturtle(t) # show turtle after it finished drawing
	mainloop()