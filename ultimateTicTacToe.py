import turtle
import math
 
class UltimateTicTacToeGame():
  def __init__(self):
    self.board_drawer = turtle.Turtle()
    self.screen_width = turtle.Screen().window_width()
    self.screen_height = turtle.Screen().window_height()
    self.setScale()
    self.square_size = self.box_size / 3
    self.width = 1
    self.height = 1
    self.board_xcor = turtle.Screen().window_width() / -5.5
    self.board_ycor = turtle.Screen().window_height() / 2.5
    self.drawGrid()
    self.scoreturtle = turtle.Turtle()
    self.scoreturtle.ht()
    
  def setScale(self):
    if self.screen_width < self.screen_height:
      self.box_size = self.screen_width / 1.5
    else:
      self.box_size = self.screen_height / 1.5
      
  def gameover(self, player):
    turtle.Screen().resetscreen()
    self.scoreturtle.speed(0)
    self.scoreturtle.ht()
    self.scoreturtle.penup()
    self.scoreturtle.setposition(0, self.screen_height / 6.5)
    if player == 0:
      self.scoreturtle.write("Tie!", False, align="center", font=("Arial", 32, "normal"))
    elif player == 1:
      self.scoreturtle.write("X Wins!", False, align="center", font=("Arial", 32, "normal"))
    elif player == 2:
      self.scoreturtle.write("O Wins!", False, align="center", font=("Arial", 32, "normal"))
    self.scoreturtle.setposition(0, -self.screen_height / 6.5)
    self.scoreturtle.write("Game Over!", False, align="center", font=("Arial", 32, "normal"))
    self.gameOver = True
    
  def drawGrid(self):
    self.board_drawer.penup()
    self.board_drawer.ht()
    self.board_drawer.speed(0)
    self.board_drawer.setpos(self.board_xcor,
                             self.board_ycor)
    self.board_drawer.pendown()
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.height)
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.height)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.width)
  
  def createMiniGame(self, width, height):  
    game = MiniTicTacToeGame(self.board_xcor + (width - 1) * self.square_size, self.board_ycor - (height - 1) * self.square_size)
    return game
  
  def getBoardX(self):
    return self.board_xcor
  
  def getBoardY(self):
    return self.board_ycor
    
    
class MiniTicTacToeGame():
  def __init__(self, x, y):
    self.board_drawer = turtle.Turtle()
    self.screen_width = turtle.Screen().window_width()
    self.screen_height = turtle.Screen().window_height()
    self.setScale()
    self.square_size = self.box_size / 3
    self.width = 1
    self.height = 1
    self.board_xcor = x
    self.board_ycor = y
    self.boardstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.drawGrid()
    self.turtles = []
    self.initializeTurtles()
    self.registerShapes()
   
  def setScale(self):
    if self.screen_width < self.screen_height:
      self.box_size = self.screen_width / 4.5
    else:
      self.box_size = self.screen_height / 4.5
   
  def initializeTurtles(self):
    for i in range(9):
      x = turtle.Turtle()
      x.hideturtle()
      self.turtles.append(x)
    
  def gameover(self, player):
    if not player == 0:
      for i in range(9):
        currentTurtle = self.turtles[i]
        currentTurtle.hideturtle()  
    r = turtle.Turtle()
    r.speed(0)
    if player == 1:
      r.shape("End X")
    if player == 2:
      r.shape("End O") 
      r.fillcolor("white")
    r.penup()
    self.moveObject(r, 2, 2)
    self.gameOver = True
    return player
   
  def registerShapes(self):
    screen = turtle.Screen()
    q = 5 * self.square_size / 12
    r = 5 * self.box_size / 12
    screen.register_shape("X", (
        (0, 0),
        (-q, -q),
        (q, q),
        (0, 0),
        (-q, q),
        (q, -q)))
    screen.register_shape("End X", (
        (0, 0),
        (-r, -r),
        (r, r),
        (0, 0),
        (-r, r),
        (r, -r)))
    screen.register_shape("O", (
        (q, 0),
        (0.9659 * q, 0.2588 * q),
        (0.8660 * q, 0.5 * q),
        (0.7071 * q, 0.7071 * q),
        (0.5 * q, 0.8660 * q),
        (0.2588 * q, 0.9659 * q),
        (0, q),
        (-0.2588 * q, 0.9659 * q),
        (-0.5 * q, 0.8660 * q),
        (-0.7071 * q, 0.7071 * q),
        (-0.8660 * q, 0.5 * q),
        (-0.9659 * q, 0.2588 * q),
        (-q, 0),
        (-0.9659 * q, -0.2588 * q),
        (-0.8660 * q, -0.5 * q),
        (-0.7071 * q, -0.7071 * q),
        (-0.5 * q, -0.8660 * q),
        (-0.2588 * q, -0.9659 * q),
        (0, -q),
        (0.2588 * q, -0.9659 * q),
        (0.5 * q, -0.8660 * q),
        (0.7071 * q, -0.7071 * q),
        (0.8660 * q, -0.5 * q),
        (0.9659 * q, -0.2588 * q)))
    screen.register_shape("End O", (
        (r, 0),
        (0.9659 * r, 0.2588 * r),
        (0.8660 * r, 0.5 * r),
        (0.7071 * r, 0.7071 * r),
        (0.5 * r, 0.8660 * r),
        (0.2588 * r, 0.9659 * r),
        (0, r),
        (-0.2588 * r, 0.9659 * r),
        (-0.5 * r, 0.8660 * r),
        (-0.7071 * r, 0.7071 * r),
        (-0.8660 * r, 0.5 * r),
        (-0.9659 * r, 0.2588 * r),
        (-r, 0),
        (-0.9659 * r, -0.2588 * r),
        (-0.8660 * r, -0.5 * r),
        (-0.7071 * r, -0.7071 * r),
        (-0.5 * r, -0.8660 * r),
        (-0.2588 * r, -0.9659 * r),
        (0, -r),
        (0.2588 * r, -0.9659 * r),
        (0.5 * r, -0.8660 * r),
        (0.7071 * r, -0.7071 * r),
        (0.8660 * r, -0.5 * r),
        (0.9659 * r, -0.2588 * r)))
  def drawGrid(self):
    self.board_drawer.penup()
    self.board_drawer.ht()
    self.board_drawer.speed(0)
    self.board_drawer.setpos(self.board_xcor,
                             self.board_ycor)
    self.board_drawer.pendown()
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.color("red")
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.height)
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.height)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.width)  
   
  def moveObject(self, obj, width, height):
    obj.setpos((self.board_xcor + self.square_size / 2 + self.square_size * (width - 1)),
               ((self.board_ycor - self.square_size / 2 - self.square_size * (height - 1))))
    return
 
  def createX(self, width, height):  
    x = turtle.Turtle()
    x.speed(0)
    x.shape("X")
    x.penup()
    self.moveObject(x, width, height)
    self.turtles[3 * (height - 1) + (width - 1)] = x
    return
 
  def createO(self, width, height):
    o = turtle.Turtle()
    o.speed(0)
    o.shape("O")
    o.fillcolor("white")
    o.penup()
    self.moveObject(o, width, height)
    self.turtles[3 * (height - 1) + (width - 1)] = o
    return
  
  def checkBoardState(self, width, height):
    return self.boardstate[3 * (height - 1) + (width - 1)]
  
  def changeBoardState(self, width, height, player):
    self.boardstate[3 * (height - 1) + (width - 1)] = player
    return
  
  def returnStatus(self):
    w = 3
  #checks if rows are matching
    for i in range(3):
      if not self.boardstate[3*i] == 0:
        if self.boardstate[3*i] == self.boardstate[3*i+1] and self.boardstate[3*i] == self.boardstate[3*i+2]:
          w = self.gameover(self.boardstate[3*i])
  #checks if columns are matching
    for j in range(3):  
      if not self.boardstate[j] == 0:
        if self.boardstate[j] == self.boardstate[3+j] and self.boardstate[j] == self.boardstate[6+j]:
          w = self.gameover(self.boardstate[j])    
  #checks if diagonals are matching
    if not self.boardstate[0] == 0:
      if self.boardstate[0] == self.boardstate[4] and self.boardstate[0] == self.boardstate[8]:
        w = self.gameover(self.boardstate[0])
    if not self.boardstate[2] == 0:    
      if self.boardstate[2] == self.boardstate[4] and self.boardstate[2] == self.boardstate[6]:
        w = self.gameover(self.boardstate[2])  
  #if entire board is filled, tied
    checker = 0
    for k in range(9):
      if not self.boardstate[k] == 0:
        checker += 1
    if checker == 9:
      w = self.gameover(0)
    
    return w

game = UltimateTicTacToeGame()
screen = turtle.Screen()  
mainTurn = True
xcor = game.getBoardX()
ycor = game.getBoardY()
box_size = game.square_size

boardstate = []
gamestate = [3, 3, 3, 3, 3, 3, 3, 3, 3]

#initializes boardstate 
for i in range(9):
  q = int(math.floor(i % 3)) + 1
  r = int(math.floor(i / 3)) + 1
  boardstate.append(game.createMiniGame(q, r))

currentGame = 4 
sq_size = boardstate[0].square_size

def checkStatus():
  #checks if rows are matching
  for i in range(3):
    if gamestate[3*i] != 0 and gamestate[3*i] != 3:
      if gamestate[3*i] == gamestate[3*i+1] and gamestate[3*i] == gamestate[3*i+2]:
        game.gameover(gamestate[3*i])
  #checks if columns are matching
  for j in range(3):  
    if gamestate[j] != 0 and gamestate[j] != 3:
      if gamestate[j] == gamestate[3+j] and gamestate[j] == gamestate[6+j]:
        game.gameover(gamestate[j])    
  #checks if diagonals are matching
  if gamestate[0] != 0 and gamestate[0] != 3:
    if gamestate[0] == gamestate[4] and gamestate[0] == gamestate[8]:
      game.gameover(gamestate[0])
  if gamestate[2] != 0 and gamestate[0] != 3:    
    if gamestate[2] == gamestate[4] and gamestate[2] == gamestate[6]:
      game.gameover(gamestate[2])  
  #if entire board is filled, tied
  checker = 0
  for k in range(9):
    if gamestate[k] != 0 and gamestate[k] != 3:
      checker += 1
  if checker == 9:
    game.gameover(0)
    
def makeMove(width, height):
  global mainTurn
  global currentGame
  s = int(math.floor(width / 3))
  t = int(math.floor(height / 3))
  g = int(math.floor(width % 3)) + 1
  h = int(math.floor(height % 3)) + 1
  thisGame = 3 * t + s
  if currentGame != thisGame and gamestate[currentGame] == 3:
    print("Wrong Square!")
  elif not gamestate[thisGame] == 3:
    print("Game Decided Already!") 
  elif not boardstate[thisGame].checkBoardState(g, h) == 0:
    print("Already Filled!")
  else:
    #checks if its X's turn
    if mainTurn:
      boardstate[thisGame].createX(g, h)
      mainTurn = False
      boardstate[thisGame].changeBoardState(g, h, 1)
      var = boardstate[thisGame].returnStatus()
      gamestate[3 * t + s] = var
      currentGame = 3 * (h - 1) + (g - 1)
      checkStatus()
    else:
      #else it's O's turn
      boardstate[thisGame].createO(g, h)
      mainTurn = True
      boardstate[thisGame].changeBoardState(g, h, 2)
      var = boardstate[thisGame].returnStatus()
      gamestate[3 * t + s] = var
      currentGame = 3 * (h - 1) + (g - 1)
      checkStatus()
      
def checkMove(x, y):
#makes sure the click is a valid move
  width = (int) (math.floor((x - xcor)/sq_size))
  height = (int) (math.floor((ycor - y)/sq_size))
  if 0 <= width and width <= 8:
    if 0 <= height and height <= 8:
      makeMove(width, height)

screen.onclick(checkMove)
