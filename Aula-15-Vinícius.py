# Instalar a biblioteca 

# Importar a biblioteca
import pygame


pygame.init() # Inicieo funcionamento do módulo.
tela = pygame.display.set_mode((1900,1000)) # Criei a tela.
tela.fill((255,0,0)) # pintei a tela. 
pygame.display.flip() # sequencia de quadros.

pygame.init()
tela = pygame.display.set_mode((500,500))
quadrado = pygame.Rect(250,250,50,50)
clock = pygame.time.Clock()

run = False 

while True :
    for event in pygame.event.get():
      if event.type  == pygame.QUIT:
         run = False
         pygame.quit()
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_RIGHT:
         quadrado.move_ip([2,0])
      if event.key == pygame.K_LEFT:
       quadrado.move_ip([-2,0])
      if event.key == pygame.K_DOWN:
         quadrado.move_ip([0,2])
      if event.key == pygame.K_UP:
         quadrado.move_ip([0,-2])



    tela.fill("white")
    pygame.draw.rect (tela, ('red'), quadrado)
    pygame.display.update()