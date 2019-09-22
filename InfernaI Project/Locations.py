
class Location:
    def __init__(self,name,x,y):
       self.name = name
       self.x = x
       self.y = y 

CoffeShop = Location('Coffe Shop',200,200)
Club = Location('Club',300,300)
Bar = Location('Bar',400,400)
Gym = Location('Gym',200,400)
Onsen = Location('Onsen', 600,600)
Katarina_Appartment = Location('Katarina Appartment',1000,100)
Vi_Appartment = Location('Vi Appartment',1100,100)
Ashe_Appartment = Location('Ashe Appartment',1200,100)
Akali_Appartment = Location('Akali Appartment',1300,100)

Locations = (CoffeShop,Club,Bar,Gym)
Bedtime = (Katarina_Appartment,Akali_Appartment,Ashe_Appartment,Vi_Appartment)
