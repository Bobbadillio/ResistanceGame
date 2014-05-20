from player import player
from random import sample

        
class dullMuteDeaf(player):
    # dullMuteDeaf is an AI that can't:
    # think intelligently
    # speak to other players
    # hear what other players say
    def __init__(self,name):
        self.name = name
        
    def setRole(self,role):
        self.role = role
        
    def getRole(self):
        return self.role
        
    def getName(self):
        return self.name

    def setState(self):
        return

    def proposeTeam(self,plan,players):
        nMembers = plan[0]
        #return players[1:nMembers]
        return sample(players,nMembers)

    def vote(self,team):
        #print self.name + ": Aye!"
        return True

    def throwCard(self):
        if self.role=="spy":
            #print "failed the mission!"
            return False
        if self.role=="resistance":
            #print "a good resistance member"
            return True
        else:
            #print "got confused, threw success"
            return True

class dullMuteDeaf(player):
    # dullMuteDeaf is an AI that can't:
    # speak to other players
    # hear what other players say
    # possibleBot CAN however, identify if a proposed team is possible
    # based on previous game state
    def __init__(self,name):
        self.name = name
        
    def setRole(self,role):
        self.role = role
        
    def getRole(self):
        return self.role
        
    def getName(self):
        return self.name

    def setState(self,gameState):
        self.gameState = gameState

    def proposeTeam(self,plan,players):
        nMembers = plan[0]
        #return players[1:nMembers]
        return sample(players,nMembers)

    def vote(self,team):
        #print self.name + ": Aye!"
        return True

    def throwCard(self):
        if self.role=="spy":
            #print "failed the mission!"
            return False
        if self.role=="resistance":
            #print "a good resistance member"
            return True
        else:
            #print "got confused, threw success"
            return True


    
        
        
