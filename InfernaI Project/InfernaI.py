import random
import sys, pygame
import math
from Players import *
from Paths import *
from Relationship import *
from Locations import *


Katarina = Bottom('Katarina',Katarina_Morning,Katarina_Afternoon,Katarina_Night,Katarina_Latenight)
Akali = Bottom('Akali',Akali_Morning,Akali_Afternoon,Akali_Night,Akali_Latenight)
Caitlyn = []
Sarah = []


Ashe = Top('Ashe',Ashe_Morning,Ashe_Afternoon,Ashe_Night,Ashe_Latenight)
Vi = Top('Vi',Vi_Morning,Vi_Afternoon,Vi_Night,Vi_Latenight)
Sona = []
Morgana = []


Tops = (Vi,Ashe)
Bottoms = (Katarina,Akali)
     
def Position_Updater(player):
   player.old_x = player.x_pos
   player.old_y = player.y_pos

   if Time.daily_count == 0:
      Choice = random.choices(Locations,(player.Morning))
   if Time.daily_count == 1:
      Choice = random.choices(Locations,(player.Afternoon))
   if Time.daily_count == 2:
      Choice = random.choices(Locations,(player.Night))
   if Time.daily_count == 3:
      Choice = random.choices(Bedtime,(player.Latenight))

   
   print(Choice[0])
   player.x_pos = Choice[0].x
   player.y_pos = Choice[0].y
   

def Speed(A,B,C,D):
   global speedx, speedy
   speedx = (A-C)
   speedy = (B-D)

def Display(a,b,c,d):
   
   Image = pygame.image.load("Art/screen.png")
   Imagerect = Image.get_rect(top=0)
   screen.blit(Image, Imagerect)
   screen.blit(a.image, a.rect)
   screen.blit(b.image, b.rect)
   screen.blit(c.image, c.rect)
   screen.blit(d.image, d.rect)
   
   pygame.display.flip() 

   
def Motion(player):
    Position_Updater(player)
    Speed(player.x_pos,player.y_pos,player.old_x,player.old_y)
    player.rect = player.rect.move(speedx,speedy)
    Display(Ashe,Akali,Vi,Katarina)
    

def Pos_check(player1,player2):
    if player1.x_pos == player2.x_pos and player1.y_pos == player2.y_pos:
        Event_Selector(player1,player2)
def Event_Selector(Bottom,Top):
   global picked,events
   
   events = ['Social', 'Romance', 'Lust','Nothing']
   picked = random.choices(events,dict[Bottom.name,Top.name].Dist())
   print(picked[0])
   Event_Updater(Bottom,Top)
   

def Event_Updater(Bottom,Top):
   
   if picked[0]==events[0]:
      dict[Bottom.name,Top.name].Social_Update(0.5)
      image = pygame.image.load("Art/stud.png")
      imagerect = image.get_rect(right=1050,bottom=750)
      screen.blit(image, imagerect)
      
      image2 = pygame.image.load("Art/%s.png"%(Bottom.name))
      imagerect2 = image2.get_rect(right=1450,bottom=750)
      #image2 = pygame.transform.scale(image2,(190,300))
      screen.blit(image2, imagerect2)
      
      image3 = pygame.image.load("Art/%s.png"%(Top.name))
      imagerect3 = image3.get_rect(right=1250,bottom=750)
      screen.blit(image3, imagerect3)

      image4 = pygame.image.load("Art/Backstage.png")
      imagerect4 = image4.get_rect(right=850,bottom=750)
      screen.blit(image4, imagerect4)
      
      pygame.display.flip()      
   if picked[0]==events[1]:
      dict[Bottom.name,Top.name].Social_Update(0.5)
      image = pygame.image.load("Art/stud.png")
      imagerect = image.get_rect(right=1050,bottom=750)
      screen.blit(image, imagerect)
      
      image2 = pygame.image.load("Art/%s.png"%(Bottom.name))
      imagerect2 = image2.get_rect(right=1450,bottom=750)
      screen.blit(image2, imagerect2)
      
      image3 = pygame.image.load("Art/%s.png"%(Top.name))
      imagerect3 = image3.get_rect(right=1250,bottom=750)
      screen.blit(image3, imagerect3)

      image4 = pygame.image.load("Art/Backstage.png")
      imagerect4 = image4.get_rect(right=850,bottom=750)
      screen.blit(image4, imagerect4)
      
      pygame.display.flip()  
   if picked[0]==events[2]:
      dict[Bottom.name,Top.name].Social_Update(0.5)
      image = pygame.image.load("Art/stud.png")
      imagerect = image.get_rect(right=1050,bottom=750)
      screen.blit(image, imagerect)
      
      image2 = pygame.image.load("Art/%s.png"%(Bottom.name))
      imagerect2 = image2.get_rect(right=1450,bottom=750)
      screen.blit(image2, imagerect2)
      
      image3 = pygame.image.load("Art/%s.png"%(Top.name))
      imagerect3 = image3.get_rect(right=1250,bottom=750)
      screen.blit(image3, imagerect3)

      image4 = pygame.image.load("Art/Backstage.png")
      imagerect4 = image4.get_rect(right=850,bottom=750)
      screen.blit(image4, imagerect4)
      
      pygame.display.flip() 


dict = {(Katarina.name,Vi.name):KatarinaVi,(Katarina.name,Ashe.name):KatarinaAshe,(Akali.name,Vi.name):AkaliVi,(Akali.name,Ashe.name):AkaliAshe}

size = width, height = 1500, 800
black = 0, 0, 0
screen = pygame.display.set_mode(size)
Image = pygame.image.load("Art/screen.png")
Imagerect = Image.get_rect(top=0)
screen.blit(Image, Imagerect)
pygame.display.flip() 


class Time:
   def __init__(self):
      self.daily_count = -1
      self.weekly_count = 0

Time = Time()
Daily_Time = ['Morning','Afternoon', 'Night','Latenight']
Days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def Time_updater(self):

   self.daily_count = self.daily_count +1
   
  
   if self.daily_count == 4:
      self.daily_count = self.daily_count -4
      self.weekly_count = self.weekly_count +1
   if self.weekly_count == 7:
      self.weekly_count = self.weekly_count -7
   print(Daily_Time[self.daily_count])
   print(Days[self.weekly_count])
while True:
    for event in pygame.event.get():

       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_w:
               Time_updater(Time)
               Motion(Katarina)
               Motion(Vi)
               Motion(Ashe)
               Motion(Akali)
               for i in range(len(Tops)):
                  
                  Pos_check(Katarina,Tops[i])
                  Pos_check(Akali,Tops[i])
               

               
               




















