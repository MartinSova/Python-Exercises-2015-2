from beggar import*

def statistics(Nplayers, games):
	"""This function uses the 'beggar' function to find the shortest, average and
	the longest of games of beggar-your-neighbour with Nplayers."""
	all_games = [] 
	for i in range(games): # number of turns for all trials of games for Nplayers is appended to all_games
		deck = shufflepack()
		all_games.append(beggar(Nplayers, deck, False))
	shortest = min(all_games)
	average = sorted(all_games)[len(all_games) // 2] # find average from sorted list, or one below of middle index if 'games' is odd
	longest = max(all_games)
	return shortest, average, longest

def averages(lowest, highest, trials):
	"""This function finds statistics using the 'statistics' function over 'trials' trials,
	for the shortest, average, and longest games for a certain number of player;
	this is defined by the arguments 'lowest', and 'highest'. If you want to find
	statistics for beggar-your-neighbour over a range of players, such
	as 2-10, you call averages(2, 10)."""
	for digit in range(lowest, highest+1): # in range 1 is added to argument 'highest', range generates up to (not including) this number
		shortest, average, longest = statistics(digit, trials)
		print('Statistics for games of', digit,'players:') # statistics from 'statistics' function are printed for each number of Nplayers 
		print('Shortest game for', digit, 'players =', shortest)
		print('Average game for', digit, 'players =', average)
		print('Longest game for', digit, 'players =', longest)

averages(2, 10, 100)
