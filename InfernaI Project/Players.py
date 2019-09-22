import sys, pygame
import random
class Bottom:
   def __init__(self,name,Morning,Afternoon,Night,Latenight):
      self.name = name
      self.x_pos = 0
      self.y_pos = 0
      self.old_x = 0
      self.old_y = 0
      self.image = pygame.image.load("%s.png"%(name))
      self.rect = self.image.get_rect(center=(0,0))
      self.Morning = Morning
      self.Afternoon = Afternoon
      self.Night = Night
      self.Latenight = Latenight

class Top:
    def __init__(self,name,Morning,Afternoon,Night,Latenight):
      self.name = name
      self.x_pos = 0
      self.y_pos = 0
      self.old_x = 0
      self.old_y = 0
      self.image = pygame.image.load("%s.png"%(name))
      self.rect = self.image.get_rect(center=(0,0))
      self.Morning = Morning
      self.Afternoon = Afternoon
      self.Night = Night
      self.Latenight = Latenight
       
class relationship:
   def Lust_Update(self, value):
      self.lust = abs(self.lust+value)
      self.social = abs(self.social-value/2)
      self.romance = abs(self.romance-value/2)
      self.dist = ((self.social/10),(self.romance/10),(self.lust/10),(self.nothing-(self.social+self.romance+self.lust))/10)
   def Social_Update(self, value):
      self.social += value
      self.lust = abs(self.lust-value/2)
      self.romance = abs(self.romance-value/2)
      self.dist = ((self.social/10),(self.romance/10),(self.lust/10),(self.nothing-(self.social+self.romance+self.lust))/10)
   def Romance_Update(self, value):
      self.romance = abs(self.romance+value)
      self.social = abs(self.social-value/2)
      self.lust = abs(self.lust-value/2)
      self.dist = ((self.social/10),(self.romance/10),(self.lust/10),(self.nothing-(self.social+self.romance+self.lust))/10)
      
   def __init__(self):
      self.social = 2
      self.romance = 2
      self.lust = 2
      self.nothing = 10
      self.dist = ((self.social/10),(self.romance/10),(self.lust/10),(self.nothing-(self.social+self.romance+self.lust))/10)
   def Dist(self):
      print(self.dist)


class Location:
    def __init__(self,name,x,y):
       self.name = name
       self.x = x
       self.y = y 
Cat = "Kitty"
