import pygame
print("Welcome to Sokoban")
pygame.init()
width=400
height=400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Sokoban')
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
    	done=True
  screen.fill((105,105,105))
pygame.quit()