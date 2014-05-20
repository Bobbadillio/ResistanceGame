
class GameState():
    def __init__(self,playerList):
        # game state holds player information
        # and completed mission information
        self.playerList = playerList
        self.missions = []
        
        
    def getMissionStatus(self):
        # mission status is a list [nSuccess,nFail]
        nSuccess = sum(1 for mission in self.missions if mission.result =='success')
        nFail = sum(1 for mission in self.missions if mission.result =='fail')
        return [nSuccess,nFail]

    def isOver(self):
        status = self.getMissionStatus()
        nSuccess= status[0]
        nFail = status[1]
        #print "after the round, state is resistance: {}\t spies: {}\n".format(nSuccess,nFail)
        if (nSuccess==3) or (nFail==3):
            return True

    def addMission(self,mission):
        self.missions.append(mission)

    def getWinners(self):
        status = self.getMissionStatus()
        nSuccess= status[0]
        nFail = status[1]
        print "final score:\n resistance: {}\t spies:{}\n".format(nSuccess,nFail)
#        for player in self.playerList:
#            print "player {} was {}".format(player.getName(),player.getRole())
        resistanceTeam = [player for player in self.playerList if player.getRole()=='resistance']
        spyTeam =  [player for player in self.playerList if player.getRole()=='spy']
        if nSuccess == 3:
            print "resistance won"
            return resistanceTeam
        if nFail == 3:
            print "spies won"
            return spyTeam
            

        
