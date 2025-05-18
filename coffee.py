class Coffee:
    def __init__(self,name):
        self.name=name

    @property
    def name (self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name)>=3:
            self._name=name
        else:
            print("Name must be  3 characters or more")