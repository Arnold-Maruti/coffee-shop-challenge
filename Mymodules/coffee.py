class Coffee:
    def __init__(self,name):
        self.name=name


    def __repr__(self):
        return f"{self.name}"
    
    def orders(self):
         from Mymodules import order as requests
         return [request for request in requests.Order.all_orders if request.coffee.name==self.name ]
    
    def customers(self):
        from Mymodules import order as requests
        return [coff.customer.name for coff in requests.Order.all_orders if self.name==coff.coffee.name]
    
    def average_price(self):
        from Mymodules import order as requests
        new_list=[coff.price for coff in requests.Order.all_orders if self.name==coff.coffee.name]
        if sum(new_list)==0:
            mean=0
        else:
            mean=sum(new_list)/len(new_list)

        return mean
    


    def num_orders(self):
        from Mymodules import order as requests
        new_lists=[coff for coff in requests.Order.all_orders if self.name==coff.coffee.name]
        return len(new_lists)
    
  



    @property
    def name (self):
        return self._name
    

    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name)>=3:
            self._name=name
        else:
            print("Name must be  3 characters or more")

doubles=Coffee("double")