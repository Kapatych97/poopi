x = 0
y = 0
u = 0
o = 0
p = 0
li = 0
k = 0
d = 0
url = 'https://i.gifer.com/embedded/download/2diX.gif'
def setup():
    global sun
    size(800,800)
    sun = loadImage(url, 'gif')
def draw():
    global x,y,o,u,p,li,k,d,sun
    background(0)
    for e in range(50):
        k = random(800)
        d = random (800)
        fill(255)
        ellipse(k,d,5,5)

    fill( 179, 0, 0)
    strokeWeight(0)
    
    # солнце
    image(sun, 235,280, 330,210)
    #ellipse(400,400,100,100)
    translate(400,400)
    strokeWeight(1)
   
    push()
    #
    for l in range(360):
        rotate(radians(1))
        stroke(255)
        point(150,150)
        
    rotate(radians(y))
    fill(255, 136, 0)
    ellipse(150,150,60,60)
     
    translate(150,150)
    rotate(radians(li))
    fill(250)
    ellipse(30,30,10,10)    
    pop()
    
    push()
    for d in range(180):
        rotate(radians(3))
        stroke(255)
        point(200,200)
        
    rotate(radians(u))
    fill(255, 209, 117)
    ellipse(200,200,70,70)
    fill(0,0,0,0)
    strokeWeight(5)
    ellipse(200,200,100,100)

    translate(200,200)
    rotate(radians(p))
    fill(250)
    ellipse(40,40,10,10)    
    pop()
    
     # земля
    push()
    for l in range(360):
        rotate(radians(1))
        stroke(255)
        point(90,90)
        fill(179,0,0)
     
    rotate(radians(x))
    fill(0, 132, 255)
    ellipse(90,90,50,50)
    strokeWeight(0)
    fill(0, 255, 9)
    ellipse(90,98,20,20)
    fill(0, 255, 9)
    ellipse(97,98,20,20)
    fill(0, 255, 9)
    ellipse(85,104,20,20)
    ellipse(85,78,20,20)
    strokeWeight(1)
    
    translate(90,90)
    rotate(radians(o))
    fill(250)
    ellipse(30,30,10,10)   
    pop()
    
    x = x + 1
    y = y + 2
    u = u + 1
    o = o + 2
    p = p + 10
    li += 13
    k = k + 1
    d = d + 1
