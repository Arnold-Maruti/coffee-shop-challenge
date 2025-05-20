


class Customer:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
         return f"{self.name}"


    def orders(self):
        from Mymodules import order as requests
        return [request for request in requests.Order.all_orders if request._customer==self]
    
    def coffees (self):
        from Mymodules import order as requests
        return [coff._coffee for coff in requests.Order.all_orders if coff._customer==self]
    
    def create_order(self,coffee,price):
        from Mymodules import order as requests
        return requests.Order(self,coffee,price)
        
        


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1<=len(name)<=15:
            self._name=name
        else:
            raise ValueError("Name must be between 1-15 characters")
        

    @classmethod
    def most_aficionado(cls,coffee):
        from Mymodules import order as requests
        listings=[request._price for request in requests.Order.all_orders if request._coffee==coffee]
        if listings==[]:
            max_name="None"
        else:
            max_value=max(listings)
            max_name=[ request._customer for request in requests.Order.all_orders if request._price==max_value and request._coffee==coffee]

        return max_name
    









            


