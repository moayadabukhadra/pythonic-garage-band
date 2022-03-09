from abc import abstractmethod


class Musician:
    """
    Musician base class to handle common functionality which particular kinds of musicians will inherit.
    """
    def __init__(self,name): 
        self.name=name
    @abstractmethod
    def __str__(self):
        pass
    
    def __repr__(self) :

        return f'{self.name}'

    @abstractmethod
    def get_instrument(self):
        "get instrument returns a string for each musician"
        pass
    @abstractmethod
    def play_solo(self):
        "get instrument returns a string for each musician"
        pass

        

class Guitarist(Musician):

    """
    Guitarist class which inherts from Musician class
    """
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
   def __str__(self):
        return f'My name is {self.name} and I play bass'

   def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
   def get_instrument(self):
        return 'bass'
   def play_solo(self):
        return "bom bom buh bom"
    

class Drummer(Musician):
   def __str__(self):
        return f'My name is {self.name} and I play drums'

   def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
   def get_instrument(self):

        return 'drums'
   def play_solo(self):
        return "rattle boom crash"

    

class Band:
    instances=[]
    def __init__(self,name,members=[]):
        self.name=name
        self.members=members
        self.__class__.instances.append(self)
        
        

    def __str__(self):
        "returns a string with  band name"
        return f'This is the {self.name} band'
    
    def __repr__(self):
        "returns a string for the name of the band name"
        return f'{self.name}'

    
        

    def play_solos(self):
        """
         method that asks each member musician to play a solo, in the order they were added to band.
        """

        solos = []
        for el in self.members:
            solos=solos+ [f'{el.play_solo()}']
        return solos

    @classmethod
    def to_list(cls):
        "returns a list of previously created Band instances"
        return cls.instances
        


