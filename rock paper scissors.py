# Write your code here :-)
import random, sys
print('ROCK, PAPER, SCISSORS!')
wins = 0
losses = 0
ties = 0
while True:
    print("%s wins, %s losses, %s ties" % (wins, losses, ties))
    while True: # the players loop
        print('you must enter a move, (r)ock (p)apper (s)issors or q to exit the game')
        playermove = input()
        if playermove == "q":
            sys.exit
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break#this break the player out of input loop
        print('please select one of the following r, s, p, q')

        ##players choices
    if playermove == 'r':
        print('ROCK VERSUS')
    elif playermove == 'p':
        print('PAPPER VERSUS')
    elif playermove == 's':
        print('SCISSORS VERSUS')

    ##computer moves
    computermove = ''
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computermove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computermove = 'p'
        print('PAPPER')
    elif randomNumber == 3:
        computermove = 's'
        print('SCISSORS')

    ##display the wins/losses/ties
    if playermove == computermove:
        print('its a tie')
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('aye thats a win')
        wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
        print('aye thats a win')
        wins = wins + 1
    elif playermove == 's' and computermove == 'p':
        print('aye thats a win')
        wins = wins + 1
    elif playermove == 's' and computermove == 'r':
        print('thats a loss')
        losses = losses + 1
    elif playermove == "r" and computermove == 'p':
        print('thats a loss')
        losses = losses + 1
    elif playermove == 'p' and computermove == 's':
        print('thats a loss')
        losses = losses + 1


