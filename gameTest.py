from game import ResistanceGame
from players import dullMuteDeaf


nSpies =0
nRes = 0
nGames = 10000
nPlayers = 10
players = [dullMuteDeaf("bot"+str(i)) for i in range(10)]

winCount = {player.getName():[0,0] for player in players}
for i in xrange(nGames):
    
    game = ResistanceGame(players)
    winnerNames = game.play()
    print " ".join(winnerNames)
    if len(winnerNames)==4:
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

