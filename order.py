class Order:
    def __init__(self,customer,coffee,price):
        self.customer=Customer(customer)
        self.coffee=Coffee(coffee)
        self.price=price


    @property
    def price (self):
        return self._price
    
    @price.setter
    def price (self,price):
        if isinstance(price,float) and 1.0<=price>=10.0:
            self._price=price
        
   