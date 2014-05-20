#generic player object
class player(object):
    def __init__(self,name):
        raise NotImplementedError()
        
    def setRole(self,role):
        raise NotImplementedError()

    def getRole(self,role):
        raise NotImplementedError()
        
    def getName(self):
        raise NotImplementedError()

    def proposeTeam(self,plan):
        raise NotImplementedError()

    def vote(self):
        raise NotImplementedError()

    def throwCard(self):
        raise NotImplementedError()
