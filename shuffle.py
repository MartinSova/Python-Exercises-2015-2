from random import randint

def shuffle(L):
	"""The shuffle(L) function uses the Durstenfeld algorithm to shuffle the list L"""
	for i in range(len(L)-1,0,-1): # range from end of list (len(L)-1) to the first item (downto index 0)
		j = randint(0,i)
		temporary = L[i]
		L[i] = L[j]
		L[j] = temporary
		# replaces position so that L[i] = L[j]
	return L

def check_shuffle(L):
	"""The check_shuffle(L) function checks that the shuffle(L) function respects
	the conditions of a valid shuffle of list L, using assert to raise and exception
	if not."""
	assert len(L) == len(shuffle(L))
	assert L == shuffle(L)
	print("The conditions that the length of the shuffled and original list is the same and that all the elements in the original list are in the shuffled list are true.")

def quality(L):
	"""The function quality(L) evaluates how well the list L is shuffled, which is defined
	as the fraction of times the second element of two adjacent elements is larger than the first."""
	pairs = zip(shuffle(L)[1:],shuffle(L))
	# decided to define a list 'pairs' of tuple pairs of neighboring items in the shuffled list L
	counter = 0
	numb_pairs = 0
	for t in pairs:
		if t[0]>t[1]: # t[0] is the item that precedes its neigboring item t[1] in the shuffled list L
			counter += 1  # if neighboring items agree with quality shuffling, a counter adds 1
		numb_pairs += 1
	quality = counter/numb_pairs # quality then equals total matches of t[0]>t[1] by number of neighboring pairs in the list
	return quality

def average_quality(L, trials):
	"""Since the shuffling is random, the average quality over several shuffles of the original list
	L is taken. The function average quality(L, trials) finds the average quality of 'trials' shuffle of 
	list L. """
	sum_quality = 0
	for i in range(trials): # performs 'trials' quality tests, and adds all qualities of the shuffling to sum_quality
		sum_quality += quality(L)
	avg_quality = sum_quality/trials # sum_quality is divided by the total trials to get average quality
	print("The average quality of", trials, "shuffles of the list", L, "is", avg_quality)

L1 = list(range(100))

if __name__ == "__main__":
	average_quality(L1,1000)
