from random import shuffle

def pack():
    """The 'pack' function creates a pack of 52
    players cards, numbered 2-14."""
    pack = 4*list(range(2,15)) # generates a list of a pack of (4 times) cards numbered 2-14
    return pack

def shufflepack():
    """This function shuffled the pack of 52
    playing cards numbered 2-14."""
    deck = pack()
    shuffle(deck)
    return deck

def splitdeck(Nplayers, deck):
    """The splitdeck(Nplayers, deck) function splits the
    shuffled 52 card deck between 'Nplayers' number of players
    evenly, and if Nplayers is odd, then the excess cards are further
    given out to the players until no cards are left in the deck."""

    players = [[] for i in range(Nplayers)] # a list to which cards will be appended is created for each player
    for i in range(52):
        players[(i%Nplayers)-1].append(deck.pop(0))  # cards are given consecutively to each player until no cards are left in shuffled deck (cards are popped off)     
    return players, deck # each player with their respective cards and an empty deck is returned to be used in 'beggar' function

def calc_penalty(num):
    """This function allows for a nice code later on, as
    it calculates the penalty associated with each of the penalty
    cards when called for that card."""
    penalty = (num - 10) # each penalty is equivalent to number of penalty card minus 10
    return penalty 

def finished(players):
    """This function checks whether the length of the list of players
    that still have cards is 1; hence, the game is over if only one player
    has cards left (players are removed from the game in the 'beggar' function
    when they no longer possess cards."""
    return len(players) == 1


def take_turn(player, pile):
    """The take_turn(player, pile) takes the cards held by the player whose turn it is
    and the current pile of cards. It returns the player’s cards after the turn (newplayer)
    the pile (newpile) after the turn and, reward, the cards that should be given to the
    previous player because this player didn’t lay another penalty card in response
    to the top card of the pile.  """
    penalty_cards = [11, 12,13,14]
    reward = []
    newpile = []
  
    
    if pile == [] or pile[-1] not in penalty_cards: # only one card laid by player for these conditions
        pile.append(player.pop(0))
        newpile = pile
    else: # if pile[-1] in penalty_cards
        penalty = calc_penalty(pile[-1]) # use calc_penalty function to calculate penalty of card
        for i in range(penalty):
            pile.append(player.pop(0)) # for value of penalty, player lays down cards into pile
            if pile[-1] in penalty_cards or player == []: # if player laid down another penalty card or he has no cards left his penalty ceases
                break
        if pile[-1] not in penalty_cards: # if the player does not lay down a penalty card during his payment, the pile becomes the reward for the previous player
            reward = pile
        else:
            newpile = pile # otherwise, if no reward given, newpile = pile
    newplayer = player
    return newplayer, newpile, reward

        
def beggar(Nplayers, deck, talkative):
    """The function beggar(Nplayers, deck, talkative) plays a single game
    of beggar-your-neighbour with Nplayers using the shuffled deck of cards,
    the 'deck' argument. If the argument talkative is True, the function
    prints details of the pile and the cards held by the players after each round,
    and the current round and whose turn it is. The function returns the number of
    turns that it takes for the game to finish (only one player left with cards)."""
    assert 2 <= Nplayers <= 52
    # I assert that Nplayers is at least 2, so a proper games is played out
    # I assert that Nplayers =< 52, because if Nplayers > 52, some players start with an empty hand as the deck only has 52 cards (not possible for a game)

    players, pile = splitdeck(Nplayers, deck)
    counter = 0
    while not finished(players): # while finished(players) not true (more than one player left), the game goes on
        for index, player in enumerate(players):

            counter += 1 # counts number of rounds

            if talkative: # prints out round details (turn, pile, and players) if talkative true
                print("Turn:",counter)
                print("Pile:",pile)
                print("Player", str(index) + ",", "your turn!")
                for i,x in enumerate(players):
                    print(i, x) # prints out cards held by each player

            player, newpile, reward = take_turn(player, pile)

            if reward != []: # if there is a reward, following code is executed
                for card in reward:
                    playerindex = index-1 # player with previous index to current player collects the reward
                    if playerindex == -1: # assuring to change playerindex to a valid index if it was the last player of the list to collect the reward
                        playerindex = (len(players)-1) 
                    players[playerindex].append(card) # all reward is appended to previous player's card if reward is to be given
                if player != []:
                    newpile = [player.pop(0)] # since current player just payed penalty and layed no penalty cards, he must lay the next card on the pile if he has cards left
            if player == []:
                players.remove(player) # remove players from game that have no cards left
            pile = newpile
    if talkative: # print number of rounds it took the game to finish if talkative true
        print("The game is finished. It took " + str(counter) + " rounds to finish this game.")
    return counter

deck = shufflepack()

def ask_input():
    """This function asks for input for how many player you want to play
    beggar-your-neighbour with, and then executes a game with the 'beggar' function
    for that many players."""
    num = input("How many players do you want to play 'beggar' with? ")
    beggar(int(num), deck, True)

if __name__ == "__main__":
    ask_input()