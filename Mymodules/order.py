class Order:
    all_orders=[]
    all_coffees=[]


    def __init__(self,customer,coffee,price):
        if not isinstance(customer,client.Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, drink.Coffee):
            raise TypeError("coffee must be a Coffee instance")
 
        
        if isinstance(price,float) and 1.0<=price<=10.0:
            self._price=price
        else:
            raise ValueError("price is not within range")
        
        self._customer = customer
        self._coffee = coffee


        
        Order.all_orders.append(self)
        Order.all_coffees.append(self._coffee)



    # def __repr__(self):
        # return f"{self._coffee} for {self._customer} "
    
    def customer(self):
        return self._customer
    
    def coffee(self):
        return self._coffee


    @property
    def price (self):
        return self._price
    
    @price.setter
    def price (self,_):
        raise AttributeError("Coffee name is immutable and cannot be changed.")

        




