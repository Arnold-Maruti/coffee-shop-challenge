


class Order:
    all_orders=[]
    all_coffees=[]


    def __init__(self,customer,coffee,price):
        from Mymodules import coffee as drink
        from Mymodules import customer as client


        self.customer=client.Customer(customer)
        self.coffee=drink.Coffee(coffee)
        self.price=price
        
        Order.all_orders.append(self)
        Order.all_coffees.append(self.coffee)



    def __repr__(self):
        return f"{self.coffee} for {self.customer} "


    @property
    def price (self):
        return self._price
    
    @price.setter
    def price (self,price):
        if isinstance(price,float) and 1.0<=price<=10.0:
            self._price=price
        else:
            raise ValueError("price is not within range")
        
   

left=Order("pablo","double",3.2)
right=Order("pablo","double",5.2)
center=Order("alice","double",5.4)



