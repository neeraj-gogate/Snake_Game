from os import SCHED_RESET_ON_FORK
import random, sys, pygame

pygame.init()

#Sets score to zero
score = 0

#RGB colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_YELLOW = (255, 215, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)

#screen set up
WIDTH = pygame.display.Info().current_w // 10 * 10
HEIGHT = pygame.display.Info().current_h // 10 * 10
SIZE = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SIZE)
SCOREX = 10
SCOREY = 10
FONT = pygame.font.SysFont('arial', 32)
CLOCK = pygame.time.Clock()

direction = 'right'
new_direction = direction


#Class for Snake Object
class Snake(object):
  #gives snake properties
  def __init__(self):
    self.speed = 10
    self.overall_position = [60, 50]
    self.positions = [[50, 50], [40, 50], [30, 50], [20, 50]]
    self.direction = 'right'
    self.new_direction = self.direction

  #This function binds movements to certain keys
  def handle_keys(self):
    key = pygame.key.get_pressed()
    if key is None:
      return
    if key[pygame.K_LEFT] or key[pygame.K_a]:
      self.new_direction = 'left'
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        return
        #Add your code here! REMOVE THE RETURN
    if key[pygame.K_UP] or key[pygame.K_w]:
        return
      #Add your code here! REMOVE THE RETURN
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        return
      #Add your code here! REMOVE THE RETURN
    self.check_direction()

  #sees if the  
  def check_direction(self):
    if self.new_direction == 'left' and self.direction != 'right':
      self.direction = self.new_direction
    #Add your code here!

    #This function controls the speed at which the snakes move at
  def move(self):
    if self.direction == 'left':
      self.overall_position[0] -= 10
    if self.direction == 'right':
      self.overall_position[0] += 10
    #Now do up and down yourself!

  #put the snake on the screen
  def draw(self, surface):
    for pos in self.positions:
      pygame.draw.rect(SCREEN, PURPLE, pygame.Rect(pos[0], pos[1], 10, 10))

  #good practice for getting speed. Don't worry about it that much....
  def get_speed(self):
    return self.speed

  #when you eat an apple, 
  def growth(self, apple):
    global score
    self.positions.insert(0, list(self.overall_position))
    apple_position = apple.get_position()
    if self.overall_position[0] == apple_position[0] and self.overall_position[1] == apple_position[1]:
      score += 1
      apple.spawn()
    else:
      self.positions.pop()

  def death_check(self):
    if self.overall_position[0] < 0 or self.overall_position[0] > width - 10:
        game_over()

    #Now do the height yourself!
    for pos in self.positions:
      if self.overall_position[0] == pos[0] and self.overall_position[1] == pos[1]:
        game_over()


#This function controls the properties of the apple
class Apple(object):
  def __init__(self):
    self.position = [random.randrange(1, ((WIDTH-10)//10)) * 10,random.randrange(1, ((HEIGHT-30)//10)) * 10]
  def draw(self, surface):
    pygame.draw.rect(SCREEN, RED, pygame.Rect(self.position[0], self.position[1], 10,10))

  def get_position(self):
    return self.position

  def spawn(self):
      return
      #write this yourself! Hint: it's somewhere above...... REMOVE THE RETURN

#Game over...
def game_over():
  global running
  running = False

#Making objects
snake = Snake()
apple = Apple()

running = True

#This function allows us to display the score
def display_score(x, y):
    scon = FONT.render(f"Score : {score}", True, (255, 255, 255))
    SCREEN.blit(scon, (x, y))


def main():
  global running
  while running:
    for event in pygame.event.get():
      if pygame.event == pygame.QUIT:
          pygame.quit()
          sys.exit()
          running = False
        #populate the screen
    SCREEN.fill(DARK_YELLOW)
    snake.handle_keys()
    snake.move()
    snake.growth(apple)
    snake.death_check()
    snake.draw(SCREEN)
    apple.draw(SCREEN)
    display_score(SCOREX, SCOREY)
    pygame.display.update()
    CLOCK.tick(snake.get_speed())
if __name__ == '__main__':
    main()