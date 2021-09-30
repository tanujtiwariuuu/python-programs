'''program to get class name of a instance '''

class flower:
    def __init__(self,name ):
        self.name=name

myflower=flower("marri")
print(myflower.__class__.__name__)