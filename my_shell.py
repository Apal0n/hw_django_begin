from shop.models import *

item1 = Item(name='IPhone', price=50000)
item1.save()
item2 = Item(name='AirPods', price=12000)
item2.save()
item3 = Item(name='IPad', price=30000)
item3.save()
item4 = Item(name='AppleWatch', price=20000)
item4.save()
item5 = Item(name='MacBook', price=80000)
item5.save()

purchase1 = Purchase(name='Omurzakob Elnur', age=18, item=item1)
purchase1.save()
purchase2 = Purchase(name='Temirov Azamat', age=18, item=item2)
purchase2.save()
purchase3 = Purchase(name='Jarkulov Kubat', age=19, item=item3)
purchase3.save()
purchase4 = Purchase(name='Toktomuratov Kurmanbek', age=21, item=item4)
purchase4.save()
purchase5 = Purchase(name='Jumabekov Arsen', age=24, item=item5)
purchase5.save()
