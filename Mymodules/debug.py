from Mymodules import coffee as drink
from Mymodules import customer as client
from Mymodules import order as orders


pablo=client.Customer("pablo")
pendo=client.Customer("pendo")
alice=client.Customer("alice")
donald=client.Customer("donald")


latte=drink.Coffee("latte")
blacktea=drink.Coffee("blacktea")
strongtea=drink.Coffee("strongtea")
cream=drink.Coffee("cream")


order1=orders.Order(pablo,latte,10.0)
order2=orders.Order(pendo,latte,2.0)
order3=orders.Order(alice,strongtea,10.0)


print(client.Customer.most_aficionado(latte))