
class player(object):
    def __init__(self,name):
        raise NotImplementedError()
        
    def setRole(self,role):
        raise NotImplementedError()
        
    def getName(self):
        raise NotImplementedError()

    def proposeTeam(self,mission):
        raise NotImplementedError()

    def vote(self):
        raise NotImplementedError()

    def throwCard(self):
        raise NotImplementedError()

        
class dullMuteDeaf(player):
    
    def __init__(self,name):
        self.name = name
        
    def setRole(self,role):
        self.role = role
        
    def getName(self):
        return self.name

    def proposeTeam(self,mission):
        return range(mission[0])

    def vote(self):
        print self.name + ": Aye!"
        return True

    def throwCard(self):
        if self.role=="spy":
            return False
        if self.role=="resistance":
            return True
        else:
            return True
    
        
        
