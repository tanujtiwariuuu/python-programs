'''Use of isinstance in python '''

class flower:
    def __init__(self,name ):
        self.name=name

myflower=flower("marri")

print(isinstance(myflower,flower))