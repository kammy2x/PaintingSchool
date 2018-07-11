
def setup():
    size(600, 400)
    global xCoordinate, yCoordinate
    
    rect(0, 350, 400, 400)
    fill(0, 0, 255)      #Blue color
    rect(0, 350, 25, 25)   #blue square
    fill(0,255,0)        #green. color
    rect(0, 375, 25, 25)   #green. square
    fill(255, 0, 0)        #red color
    rect(25, 350, 25, 25)   #red square
    fill(255, 255 ,0)       #yellow color
    rect(25, 375, 25, 25)  #yellow square
    fill(0)                #black color
    rect(50, 375, 25, 25)  #black square
    fill(255, 150, 51)     #orange color
    rect(50, 350, 25, 25)  #orange square
    fill(random(255), random(255), random(255)) #randomizer
    rect(75, 350, 50, 50)
    
def draw():
    if mousePressed:
        line(pmouseX, pmouseY, mouseX, mouseY)
    elif line(mouseX < 100, mouseY >= 200, pmouseX <100, pmouseY >= 200):
        noStroke
        
def mouseClicked():
    if mouseX < 25 and mouseY > 350: #blue
        stroke(0, 0, 255)
    if mouseX < 25 and mouseY > 375: #green.
        stroke(0, 255, 0)
    if mouseX > 25 and mouseY > 350: #red
        stroke(255, 0, 0)
    if mouseX > 25 and mouseY > 375: #yellow
        stroke(255, 255, 0)
    if mouseX > 50 and mouseY > 375: #black
        stroke(0)
    if mouseX > 50 and mouseY < 375: #orange
        stroke(255, 150, 51)
    if mouseX > 75 and mouseY > 350:
        stroke(random(255), random(255), random(255))
