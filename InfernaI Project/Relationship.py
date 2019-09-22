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

KatarinaVi = relationship()
KatarinaAshe = relationship()
AkaliAshe = relationship()
AkaliVi = relationship()
