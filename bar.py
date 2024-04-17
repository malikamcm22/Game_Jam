import pygame
pygame.init()

class Bar():
    def __init__(self,x,y,width,height,max_unit,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.unit = max_unit
        self.max_unit = max_unit
        self.color = color
    def draw(self,surface):
        ratio = self.unit/self.max_unit
        pygame.draw.rect(surface,"grey",(self.x,self.y,self.width,self.height))    
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width * ratio,self.height))    