from random import randint
import Image

# Set the size of the maze.
# These must be odd integers of 7 or above.
xSize = 67
ySize = 35

# Set the maximum wall length.  This avoids overly long
# walls on larger mazes.
# The smaller the value, the greater possible solutions.
maxWall = 13

# Create a list to store the maze data.
# 0 denotes a walkway, 1 is a wall, start with no walls.
maze = (xSize*ySize)*[0]

# Set every other cell to 2, these are the starting points.
for i in range(0,xSize,2):
    for j in range(0,ySize,2):
        maze[(j*xSize)+i]=2

# Create a wall around the maze.
# Top and bottom.
for i in range(0,xSize):
    maze[i]=1
    maze[(xSize*(ySize-1))+i] = 1
# Left and right.
for i in range(1,ySize-1):
    maze[xSize*i]=1
    maze[(xSize*i)+(xSize-1)] = 1

# Create the maze.
while 2 in maze:

    # Pick a random starting point.
    x = randint(1,(xSize-1)/2)*2
    y = randint(1,(ySize-1)/2)*2
    c = maze[(y*xSize)+x]

    # If the point hasn't already been used pick a random direction
    # and move that way until we hit a wall.
    if c == 2:
        mwc = 0
        r = randint(0,3)
        if r == 0:
            while c != 1:
                maze[(y*xSize)+x] = 1
                y -= 1
                c = maze[(y*xSize)+x]
                mwc += 1
                if mwc == maxWall: break
        if r == 1:
            while c != 1:
                maze[(y*xSize)+x] = 1
                x += 1
                c = maze[(y*xSize)+x]
                mwc += 1
                if mwc == maxWall: break
        if r == 2:
            while c != 1:
                maze[(y*xSize)+x] = 1
                y += 1
                c = maze[(y*xSize)+x]
                mwc += 1
                if mwc == maxWall: break
        if r == 3:
            while c!= 1:
                maze[(y*xSize)+x] = 1
                x -= 1
                c = maze[(y*xSize)+x]
                mwc += 1
                if mwc == maxWall: break

# Set this to True to print the maze to screen.
if True:
    for i in range(0,ySize):
        s=""
        for j in range(0,xSize):
            k = maze[(i*xSize)+j]
            if k == 1:s=s+"@"
            else:s=s+" "
        print s

# Set this to True to save the maze as a PNG.
if True:
    mPic = Image.new("RGB",(xSize,ySize),0)
    pix = mPic.load()
    for i in range(0,ySize):
        for j in range(0,xSize):
            col = maze[(i*xSize)+j]*255
            col = 255-col
            pix[j,i] = col,col,col
    mPic.save("maze.png")
