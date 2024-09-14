print("#####--------34. Restaurants--------#####")

class Restaurant:
    name = ''
    category = 0
    rate = 0.0
    delivery = False

bobs_burger = Restaurant ()
bobs_burger.name = "Bob\'s Burger" 
bobs_burger.category = 'American Dinner'
bobs_burger.rate = 3.9
bobs_burger.delivery = True

gyg = Restaurant ()
gyg.name = 'Guzman y Gomez'
gyg.category = "TexMex"
gyg.rate = 4.5
gyg.delivery = True

burro_bar = Restaurant ()
burro_bar.name = 'Burrito Bar'
burro_bar.category = "Mexican"
burro_bar.rate = 2.8
burro_bar.delivery = False


print(vars(bobs_burger))
print(vars(gyg))
print(vars(burro_bar))