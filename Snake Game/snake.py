import pygame, sys, random

from pygame.locals import *
#the color of the eggs
redColor = pygame.Color(255, 0, 0)
#the color of the background
blackColor = pygame.Color(0, 0, 0)
#the color of the snake
whiteColor = pygame.Color(255, 255, 255)

#quits the game, used when the snake hits the side of the window
def gameover():
     pygame.quit()
     sys.exit()

# randomly respawns the eggs on a random spot on the window
def respawn (l):
     x = random.randrange(1, 32)
     y = random.randrange(1, 24)
     fp = [int(x*20), int(y*20)]
     if not fp in(l):
          return fp
     else:
          respawn(l)

# if the first element appears in the rest of the list, pop all elemments after the second appearance
# used to cut the snake if it hits its own tail
def cut(lst):
     for i in range(len(lst) - 1, 0, -1):
          if lst[i] == lst[0]:
               del lst[i:len(lst)]
                    

     


def main():
    #initialize
     pygame.init()
    #delares a variable to control the speed of the game
     fpsClock = pygame.time.Clock()
     level = 5
    #creates the window
     window = pygame.display.set_mode((640, 480))
     pygame.display.set_caption('snake')
    #the startinf point for the snake (x,y)
     snakePosition = [100, 100]
    #the list represents the snake, each element is one part of the body
     snakeBody = [[100, 100], [80, 100], [60, 100]]
    #starting position for the egg
     foodPosition = [300, 300]
    # a flag that shows if the egg is eaten or not, 1 means its not
     foodflag = 1
     direction = 'right'
    
     while True:
          for event in pygame.event.get():
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
                   # changes the direction string in to the direction according to the key pressed
                   # cannot change the direction into the opposite direction as the current one
                   # for example, if the current direction string is left, pressing d won't change the direction
               elif event.type == KEYDOWN:
                    if event.key == K_d and direction != 'left':
                         direction = 'right'
                    if event.key == K_w and direction != 'down':
                         direction = 'up'
                    if event.key == K_a and direction != 'right':
                         direction = 'left'
                    if event.key == K_s and direction != 'up':
                         direction = 'down'

          # moves the position of the snake according to the direction string
          if direction == 'right':
               snakePosition[0] += 20
          if direction == 'left':
               snakePosition[0] -= 20    
          if direction == 'up':
               snakePosition[1] -= 20
          if direction == 'down':
               snakePosition[1] += 20
          # every time the snake moves, it detects if the snake hit its own tail or not,
          # if so, it cuts its own tail and perform the cut method that was defined above
          cut(snakeBody)
          

#adds a new piece of the snakes body to the beginning of snakebody, to represent the snake moving forwards
# will pop the last piece of snake body so the length won't change, if on this move, the snake eats the egg,
# the snake will not pop for this turn so the length of the snake will be longer
          snakeBody.insert(0, list(snakePosition))
          # checks if the head of the snake overlaps with the food after every move the snake takes
          if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
               foodflag = 0
          else:
               snakeBody.pop()
          if foodflag == 0:
               level +=3
               foodPosition = respawn(snakeBody)
               foodflag = 1
          window.fill(blackColor)
          # draws the snake and the egg
          for position in snakeBody:
               pygame.draw.rect(window, whiteColor, Rect(position[0], position[1], 20, 20))
          pygame.draw.rect(window, redColor, Rect(foodPosition[0], foodPosition[1], 20, 20))
          pygame.display.flip()
          # quits if the snake hits the side of the window
          if snakePosition[0] > 620 or snakePosition[0] < 0:
               gameover()
          elif snakePosition[1] > 460 or snakePosition[1] < 0:
               gameover()
          # pace of the game
          fpsClock.tick(level)

if __name__ == '__main__':
     main()

               




               
               
