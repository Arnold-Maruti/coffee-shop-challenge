


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
    
    def create_order(self,coffee,price):
        from Mymodules import order as requests
        return requests.Order(self.name,coffee,price)
        
        


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
        listings=[request.price for request in requests.Order.all_orders if request.coffee.name==coffee]
        if listings==[]:
            max_name="None"
        else:
            max_value=max(listings)
            max_name=[ request.customer.name for request in requests.Order.all_orders if request.price==max_value]

        return max_name
    




# pablo=Customer("diallo")
# print(Customer.most_aficionado("double"))




            


