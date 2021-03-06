from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)

x = 1
y = 1


maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,g,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

sense.set_pixels(sum(maze,[]))

maze[y][x] = w

game_over = False

def check_wall(x,y,new_x,new_y):
   if maze[new_y][new_x] != r:
        return new_x, new_y
   elif maze [new_y][x] != r:
        return x, new_y
   elif maze[y][new_x] != r:
        return new_x, y
   else:
        return x,y

def move_marble(pitch, roll, x, y):
   new_x = x
   new_y = y
   check_wall(x,y,new_x,new_y)
   new_x, new_y = check_wall(x,y, new_x, new_y)
   if 1 < pitch < 179:
        new_x -= 1
   elif 359 > pitch > 181 and x != 7:
        new_x +=1
   elif 359 > roll > 179 and y != 0:
        new_y -= 1
   if 359 < pitch < 181:
       new_x +=1
   return new_x, new_y

while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    x,y = move_marble(pitch,roll,x,y)     
    if maze[y][x] == g: 
        sense.show_message("Win!")
        game_over = True
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
while not game_over:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    yaw = sense.get_orientation()['yaw']
    x,y = move_marble(pitch,roll,x,y)
    maze[y][x] = w
    sense.get_pixels(sum(maze,[]))
    sleep(0.05) 
    maze[y][x] = b
sense.set_pixels(sum(maze,[]))
r = 255
g = 255
b = 255
sense.clear((r, g, b))