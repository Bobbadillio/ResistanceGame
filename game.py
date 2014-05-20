from random import sample, random #used to select spies
from mission import Mission
from GameState import GameState
#from KellyAIs import dullMuteDeaf as playerBot # dullMuteDeaf is a bad AI

class ResistanceGame():

    def setPlanList(self):
        # missionList returns the default list of missions for the game 
        # resistance. missions are represented as:
        # (number of players,number of fails required for sabotage)
        n = len(self.players)
        if n in [5,6,7,8,9,10]:
            planList = {
                5 :[(2,1),(3,1),(2,1),(3,1),(3,1)],
                6 :[(2,1),(3,1),(4,1),(3,1),(4,1)],
                7 :[(2,1),(3,1),(3,1),(4,2),(4,1)],
                8 :[(3,1),(4,1),(4,1),(5,2),(5,1)],
                9 :[(3,1),(4,1),(4,1),(5,2),(5,1)],
                10:[(3,1),(4,1),(4,1),(5,2),(5,1)]
                }[n]
        else:
            plan = []
            print "Error: Expected a value in [5,10]. for n in missionList function of Class ResistanceGame Given: {}".format(n)
        self.plans = planList
        
    def getPlan(self,n):
        return self.plans[n]

    def getRandomPlayer(self):
        # getRandomPlayer generates a random number then uses that random 
        # number to select and return a player from the playerList. This can be
        # used to, for example, set the initial mission leader.
        nPlayers = len(self.players)
        return self.players[int(random()*nPlayers)]

    def getRandomPlayerIndex(self):
        nPlayers = len(self.players)
        return int(random()*nPlayers)

    def getLeader(self):
        return self.players[self.leaderIndex]

    def incrementLeaderCounter(self):
        nPlayers = len(self.players)
        self.leaderIndex = (self.leaderIndex+1)%nPlayers

    def setTeams(self):
        #setSpies sets the spies by randomly choosing from the players in 
        # PlayerList
        nPlayers = len(self.players)
        nSpies   = (nPlayers-1)/3+1 # equivalent to ceil((n+2)/3)
        spyIndices = sample(range(nPlayers),nSpies) 
        

        self.spies = [self.players[i] for i in spyIndices]
        for spy in self.spies: spy.setRole("spy")

        self.resistance = [self.players[i] for i in range(nPlayers) if not(i in spyIndices)]
        for resister in self.resistance: resister.setRole("resistance")
        
    def getSpies(self):
        return self.spies
    
    def getResistance(self):
        return self.resistance



    def __init__(self,playerList):
        self.players = playerList
        self.setPlanList()
        self.setTeams()
        #game is started by random player
        self.leaderIndex = self.getRandomPlayerIndex()
        self.nSuccess =0
        self.nFail = 0
        self.missionCounter=0
        self.gameState = GameState(playerList)
        
        




    def getResult(self):
        nSuccess = self.nSuccess
        nFail = self.nFail
        if (nSuccess==3):
            resistance = self.getResistance()
            names = [player.getName() for player in resistance]
            print "Resistance wins!\nCongratulations to: ",
            return names
        if (nFail==3):
            spies = self.getSpies()
            names = [player.getName() for player in spies]
            print "Spies win!\nCongratulations to: ",
            return names
        else:
            return "Game does not appear to be over. Current state is:\n Resistance:{} \tSpies:{}".format(nSuccess,nFail)


        

    def round(self):
        nPlayers = len(self.players)
        voteCounter = 0
        #set up the mission
        plan=self.getPlan(self.missionCounter)
        for player in self.players:
            player.setState(self.gameState)
        while voteCounter<5:
            #maybe players communicate somehow 
            #leader proposes a mission
           
            leader = self.getLeader()
            team = leader.proposeTeam(plan,self.players)
            #Display option:
            #print "proposal #{}:".format(voteCounter+1), " ".join([player.name for player in team])

            #every player votes
            votes = [player.vote(team) for player in self.players]
            nApprove = sum(1 for vote in votes if vote)
            nReject = sum(1 for vote in votes if not(vote))
            #leader counter increments
            self.incrementLeaderCounter()
        
            #if mission is approved
            if nApprove>nReject:
                # make a mission for the proposed team
                thisMission = Mission(team,plan)
                # run the mission
                thisMission.run()
                # add it to the game state's mission list
                
                self.gameState.addMission(thisMission)
                self.missionCounter+=1
                return
            else:
            #  increment voteCounter
                voteCounter+=1
            if voteCounter>=5:
                # Missions fail after 5 tries
                thisMission = Mission([],plan)
                this.Mission.result='fail'
                self.gameState.addMission(thisMission)
                return

    def play(self):
        for i in range(5):
#            print "\n=========================="
#            print "beginning round {}".format(i+1)
            self.round()     
#            print "\n=========================="
            if self.gameState.isOver():
                return self.gameState
            
            
        

