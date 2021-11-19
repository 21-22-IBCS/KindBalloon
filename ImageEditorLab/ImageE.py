from graphics import*
from Button import*
 
def brighten(cats): #add all colors by 50
 
    for i in range(500):
        for j in range(451):
           
            l = cats.getPixel(i,j)
           
            r = l[0] + 50
            if (r > 255):# if color exceeds the min/max set to min/max
                r = 255
            g = l[1] + 50
            if (g > 255):
                g = 255
            b = l[2] + 50
            if (b > 255):
                b = 255
           
            cats.setPixel(i,j, color_rgb(r,g,b))
   
    
def darken(cats): # subtract all colors by 50
 
    for i in range(500):
        for j in range(451):
           
            l = cats.getPixel(i,j)
           
            r = l[0] - 50
            if (r < 0):# if color exceeds the min/max set to min/max
                r = 0
 
            g = l[1] - 50
            if (g < 0):
                g = 0
 
            b = l[2] - 50
            if (b < 0):
                b = 0
           
            cats.setPixel(i,j, color_rgb(r,g,b))
           
def blurr(cats):#finding average of adjacent pixels and averaging them and setting the main pixel to the average
 
    for i in range(1,498): #run though entire picture multiple times
        for j in range(1,449):
 
            l1 = cats.getPixel(i,j)#adjacent pixels
            l2 = cats.getPixel(i,j-1)
            l3 = cats.getPixel(i+1,j)
            l4 = cats.getPixel(i,j+1)
            l5 = cats.getPixel(i-1,j)
 
            r = int((l1[0]+l2[0]+l3[0]+l4[0]+l5[0])/5)#average
            g = int((l1[1]+l2[1]+l3[1]+l4[1]+l5[1])/5)
            b = int((l1[2]+l2[2]+l3[2]+l4[2]+l5[2])/5)
 
            cats.setPixel(i,j, color_rgb(r,g,b))
   
    
def contrast(cats):#contrast by seeing if color is bigger or less by 128 then adding or subtracting by 20
 
    for i in range(500):
        for j in range(451):
           
            l = cats.getPixel(i,j)
            if l[0] > 128:#if picture color is bigger than middle value of color, make it brighter
           
                r = l[0] + 20
                if (r > 255):
                    r = 255
                g = l[1] + 20
                if (g > 255):
                    g = 255
                b = l[2] + 20
                if (b > 255):
                    b = 255
           
                cats.setPixel(i,j, color_rgb(r,g,b))
           
            else: #if picture color is less than middle value of color, make it darker
           
                r = l[0] - 20
                if (r < 0):# if color exceeds the min/max set to min/max
                    r = 0
 
                g = l[1] - 20
                if (g < 0):
                    g = 0
 
                b = l[2] - 20
                if (b < 0):
                    b = 0
           
                cats.setPixel(i,j, color_rgb(r,g,b))
   
def specialFilter(cats):#turns the picture to black and white by setting all colors to red + 20
    for i in range(500):
        for j in range(451):
 
            l = cats.getPixel(i,j)
 
            r = l[0] + 20
            if(r > 255): # if color exceeds the min/max set to min/max
                 r = 255
            g = l[0] + 20
            if(g > 255): 
                 g = 255
            b = l[0] + 20
            if(b > 255):
                 b = 255
            cats.setPixel(i,j, color_rgb(r,g,b))
 
def sett(cats, Scats): #changes current pictures to copy of the invisible original picture
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i,j)
            Spix = Scats.getPixel(i,j)
            cats.setPixel(i,j, color_rgb(Spix[0],Spix[1],Spix[2]))
   
def main():
 
    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Filter", Point(720, 450), 45)
    redo = Button(win, "white", "Redo", Point(500, 40), 45)
 
    cats = Image(Point(400,300), "Cats.png")
    Scats = Image(Point(400,300), "Catscopy.png")#invisible never changing picture which is copy of picture
   
    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        if redo.isClicked(m):# if clicked reset pitcure 
            sett(cats, Scats)#takes cats and Scats from main method to sett
        m = win.getMouse()
 
    win.close()
   
if __name__ == "__main__":
    main()
