


class Customer:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"{self.name}"


    def orders(self):
        from Mymodules import order as requests
        return [request for request in requests.Order.all_orders if request.customer.name==self.name]
    
    def coffees (self):
        from Mymodules import order as requests
        return [coff.coffee.name for coff in requests.Order.all_orders if self.name==coff.customer.name]
        
        


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1<=len(name)<=15:
            self._name=name
        else:
            raise ValueError("Name must be between 1-15 characters")
        

pablo=Customer("pablo")



            


