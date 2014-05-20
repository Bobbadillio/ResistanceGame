
class Mission():
    def __init__(self,players,plan):
        self.players = players
        self.plan = plan
        self.result = ''
        self.thrownCards = []
    def run(self):
        
        
        requiredFails = self.plan[1]
        
        self.thrownCards = [player.throwCard() for player in self.players]
        nFails = sum(1 for card in self.thrownCards if not(card))
        
        #print "required Fails: {}\tobserved fails: {}".format(requiredFails,nFails)
        if nFails>=requiredFails:
            #print "Mission Failed"
            self.result = 'fail'
        else:
            #print "Mission Succeeded"
            self.result = 'success'
        return

    def __bool__(self):
        myBool = False
        if self.result == 'fail':
            myBool = False
        elif self.result == 'successs':
            myBool = True
        else:
            print "Mission is confused about its state:{}".format(myBool)
        return myBool
        
  

        

