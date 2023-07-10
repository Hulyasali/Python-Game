import turtle
import math
import random



#Arka planı düzelt
wn = turtle.Screen()
wn.bgcolor("white")
wn.bgpic("resim3.gif")
wn.tracer(4)
wn.title("Collision of Balls")

#Oyun alanını oluştur 
mypen = turtle.Turtle()
mypen.color("black")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.hideturtle()
for side in range(4):
        mypen.forward(600)
        mypen.left(90)
mypen.hideturtle()

#Kalemler
myscore = turtle.Turtle()
myscore.color("black")
myscore.penup()
myscore.hideturtle()
myscore.setposition(-290, 310)

myh = turtle.Turtle()
myh.color("black")
myh.penup()
myh.hideturtle()
myh.setposition(290, 310)


#Oyuncuyu oluştur
player = turtle.Turtle()
player.color("purple")
player.shape("triangle")
player.penup()
player.speed(0)

wn.addshape("resim2.gif")
#Topları oluştur
maxGoals = 10
goals = []
for count in range(maxGoals):
        goals.append(turtle.Turtle())
        goals[count].shape("resim2.gif")
        goals[count].penup()
        goals[count].speed(0)
        goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

wn.addshape("fire3.gif")

#Alevi oluştur
maxGoals2 = 10
goals2 = []

for count in range(maxGoals2):
        goals2.append(turtle.Turtle())
        goals2[count].shape("fire3.gif")
        goals2[count].penup()
        goals2[count].speed(0)
        goals2[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
 
#Hız ayarı
speed = 1

#Fonksiyonlar
def turnleft():
        player.left(30)
        
def turnright():
        player.right(30)
        
def increasespeed():
        global speed
        speed += 1

def decreasespeed():
        global speed
        speed -= 1

def isCollision(t1, t2):
        d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
        if d < 20:
                return True
        else:
                return False
                
#Klavye ayarları
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

#Skor oluştur
score = 0

#Can oluştur
health = 3

#Canı ekranda yaz
myh.undo()
myh.penup()
myh.hideturtle()
myh.setposition(290, 310)
healthstring = "Health: %s" %health
myh.write(healthstring, False, align="right", font=("Arial",14, "normal"))

#Skoru ekranda yaz
myscore.undo()
myscore.penup()
myscore.hideturtle()
myscore.setposition(-290, 310)
scorestring = "Score: %s" %score
myscore.write(scorestring, False, align="left", font=("Arial",14, "normal"))



while health>0:
        player.forward(speed)
        
        #Oyuncu için sınır
        if player.xcor() > 300 or player.xcor() < -300:
                player.right(180)
                
                
                
        #Oyuncu için sınır
        if player.ycor() > 300 or player.ycor() < -300:
                player.right(180)
    
                
                
        #Toplar için hareket
        for count in range(maxGoals):
                goals[count].forward(3)

                #Toplar için sınır
                if goals[count].xcor() > 290 or goals[count].xcor() < -290:
                        goals[count].right(180)
                       
                        
                                
                #Toplar için sınır
                if goals[count].ycor() > 290 or goals[count].ycor() < -290:
                        goals[count].right(180)
                        
                 #Oyuncu ve topların çarpışması
                if isCollision(player, goals[count]):
                        goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
                        goals[count].right(random.randint(0,360))
                        import winsound
                        winsound.PlaySound("button-11.wav",winsound.SND_ASYNC)
                        score += 10
                        #Skoru ekranda yaz
                        myscore.undo()
                        myscore.penup()
                        myscore.hideturtle()
                        myscore.setposition(-290, 310)
                        scorestring = "Score: %s" %score
                        myscore.write(scorestring, False, align="left", font=("Arial",14, "normal"))
                        

        #Alevler için hareket
        for count in range(maxGoals2):
                goals2[count].forward(3)

                #Alevler için sınır
                if goals2[count].xcor() > 290 or goals2[count].xcor() < -290:
                        goals2[count].right(180)
    
                        
                                
                #Toplar için sınır
                if goals2[count].ycor() > 290 or goals2[count].ycor() < -290:
                        goals2[count].right(180)


                #Oyuncu ve alevlerin çarpışması
                if isCollision(player, goals2[count]):
                        goals2[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
                        goals2[count].right(random.randint(0,360))
                        import winsound
                        winsound.PlaySound("button-10.wav",winsound.SND_ASYNC)
                        score -= 20
                        health -= 1
                        #Skoru ekranda yaz
                        myscore.undo()
                        myscore.penup()
                        myscore.hideturtle()
                        myscore.setposition(-290, 310)
                        scorestring = "Score: %s" %score
                        myscore.write(scorestring, False, align="left", font=("Arial",14, "normal"))
                        #Canı ekranda yaz
                        myh.undo()
                        myh.penup()
                        myh.hideturtle()
                        myh.setposition(290, 310)
                        healthstring = "Health: %s" %health
                        myh.write(healthstring, False, align="right", font=("Arial",14, "normal"))
                        #Game over'ı ekranda yaz
                        if health==0:
                                mypen.undo()
                                mypen.penup()
                                mypen.hideturtle()
                                mypen.setposition(0, 0)
                                gameoverstring="GAME OVER"
                                mypen.write(gameoverstring,False, align="center", font=("Arial",26, "normal"))                



