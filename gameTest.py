#!/usr/bin/env python
from game import ResistanceGame
from KellyAIs import dullMuteDeaf


nSpies =0
nRes = 0
nGames = 10000
nPlayers = 8
players = [dullMuteDeaf("bot"+str(i)) for i in range(nPlayers)]

winCount = {player.getName():[0,0] for player in players}
for i in xrange(nGames):
    
    game = ResistanceGame(players)
    finalState = game.play()
    winners = finalState.getWinners()
    winnerNames = [winner.getName() for winner in winners]
    #print " ".join(winnerNames)
    if winners[0].getRole()=="spy":
        nSpies+=1
        for winnerName in winnerNames:
            winCount[winnerName][1]+=1
    else:
        nRes +=1
        for winnerName in winnerNames:
            winCount[winnerName][0]+=1

print "spy wins: ",nSpies
print "resistance wins:",nRes

print "\n\n"
for player in players:
    print "player: {}\twins:{}\n".format(player.getName(),winCount[player.getName()])

