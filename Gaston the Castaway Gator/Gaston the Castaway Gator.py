from pygame import mixer
mixer.init()
main = mixer.Sound("main.wav")
intro = mixer.Sound("intro.wav")
punch = mixer.Sound("punch.wav")
chomp = mixer.Sound("chomp.wav")
collision = mixer.Sound("collision.wav")
boss = mixer.Sound("boss.wav")
squirt = mixer.Sound("squirt.wav")
finale = mixer.Sound("end.wav")
finish = mixer.Sound("finish.wav")
foxw = mixer.Sound("foxw.wav")
import pgzrun
import random
from random import randint
WIDTH = 1400
HEIGHT = 903
b = Actor("title")
b.pos = 700, 450
gaston = Actor("0")
gaston.pos = 700, 400
entry = Actor("0")
entry.pos = 700, 600
shark = Actor("0")
shark.pos = 700, 100
shark2 = Actor("0")
shark2.pos = 700, 803
coconut = Actor("0")
coconut.pos = 300, 300
kingshark = Actor("shark king")
kingshark.pos = -1000, -1000
fireball = Actor("0")
fireball.pos = -1000, -1000
fireball2 = Actor("0")
fireball2.pos = -1000, -1000
fuel = Actor("0")
fuel.pos = 700, 100
end = Actor("0")
end.pos = 700, 450
endi = Actor("0")
endi.pos = 700, 450
intro.play()
switch = 0
score = 0
hp = 3
di = ""
di2 = ""
di3 = ""
di4 = ""
di5 = 0
di6 = 0
fly = 0.001
fly2 = 0.001
hp2 = 0
x = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
distance = [20, 40, 60, 80, 100]
direction = ["up", "down", "left", "right"]
face = ""
def up():
    gaston.image = "gaston up punch"
    clock.schedule(up2, 0.2)
def up2():
    gaston.image = "gaston"
def down():
    gaston.image = "gaston down punch"
    clock.schedule(down2, 0.2)
def down2():
    gaston.image = "gaston down"
def left():
    gaston.image = "gaston left punch"
    clock.schedule(left2, 0.2)
def left2():
    gaston.image = "gaston left"
def right():
    gaston.image = "gaston right punch"
    clock.schedule(right2, 0.2)
def right2():
    gaston.image = "gaston right"
def rotate():
    global direction, di
    di = random.choice(direction)
def rotate2():
    global direction, di2
    di2 = random.choice(direction)
def right3():
    shark.image = "shark right"
    gaston.image = "gaston right"
def left3():
    shark.image = "shark left"
    gaston.image = "gaston left"
def down3():
    shark.image = "shark"
    gaston.image = "gaston down"
def up3():
    shark2.image = "shark up"
    gaston.image = "gaston"
def right4():
    shark2.image = "shark right"
    gaston.image = "gaston right"
def left4():
    shark2.image = "shark left"
    gaston.image = "gaston left"
def down4():
    shark2.image = "shark"
    gaston.image = "gaston down"
def up4():
    shark2.image = "shark up"
    gaston.image = "gaston"
def nextt():
    global score
    score = 1510
def nexttt():
    global score
    score = 1720
def spoil():
    global score, hp
    if score < 1710:
        coconut.image = "coconut spoil"
        hp -= 1
        score = 1510
def reset():
    coconut.image = "coconut"
def ender():
    global hp
    hp = 1
    end.image = "end"
    endi.image = "end2"
    finale.play(-1)
def fire():
    global x, di3, di4, fly
    fireball.x += di3
    fireball.y += di4
    fly += 0.001
    if fireball.x < 1400:
        if fireball.y < 903:
            clock.schedule(fire, fly)
        else:
            fireball.pos = 700, 200
            di3 = random.choice(x)
            di4 = random.choice(x)
            clock.schedule(fire, fly)
    else:
        fireball.pos = 700, 200
        di3 = random.choice(x)
        di4 = random.choice(x)
        clock.schedule(fire, fly)
def fire2():
    global x, di5, di6, fly2
    fireball2.x -= di6
    fireball2.y += di5
    fly2 += 0.001
    if fireball2.x > 0:
        if fireball2.y < 903:
            clock.schedule(fire2, fly2)
        else:
            fireball2.pos = 700, 200
            di5 = random.choice(x)
            di6 = random.choice(x)
            clock.schedule(fire2, fly2)
    else:
        fireball2.pos = 700, 200
        di5 = random.choice(x)
        di6 = random.choice(x)
        clock.schedule(fire2, fly2)
def fall():
    gaston.pos = 700, 800
def flee():
    kingshark.y -= 10
def update():
    global hp2, switch, di5, di6, face, direction, distance, di, di2, hp, score, x, di3, di4
    b.draw()
    gaston.draw()
    entry.draw()
    shark.draw()
    shark2.draw()
    coconut.draw()
    fireball.draw()
    fireball2.draw()
    kingshark.draw()
    fuel.draw()
    endi.draw()
    end.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    screen.draw.text("HP: " + str(hp), color="black", topleft=(10, 40))
    if keyboard.space:
        b.image = "background"
        gaston.image = "gaston"
        entry.image = "entry"
        intro.stop()
        switch += 1
    if switch == 1:
        if keyboard.a:
            entry.image = "0"
            switch += 1
            main.play(-1)
            shark.image = "shark"
            shark2.image = "shark up"
    if switch == 2:
        if hp == 0:
            endi.image = "end2"
            end.image = "end3"
            foxw.play()
            switch = 0
            main.stop()
        entry.image = "0"
        clock.schedule(rotate, 0.1)
        clock.schedule(rotate2, 0.1)
        if keyboard.up:
            gaston.y -= 20
            gaston.image = "gaston"
            face = "up"
        if keyboard.down:
            gaston.y += 20
            gaston.image = "gaston down"
            face = "down"
        if keyboard.left:
            gaston.x -= 20
            gaston.image = "gaston left"
            face = "left"
        if keyboard.right:
            if gaston.x <= 1400:
                gaston.x += 20
                gaston.image = "gaston right"
                face = "right"
        if keyboard.a:
            punch.play()
            if face == "up":
                clock.schedule(up, 0.1)
            if face == "down":
                clock.schedule(down, 0.1)
            if face == "left":
                clock.schedule(left, 0.1)
            if face == "right":
                clock.schedule(right, 0.1)
        if di == "up":
            shark.image = "shark up"
            if shark.y >= 100:
                shark.y -= random.choice(distance)
            else:
                shark.y += random.choice(distance)
            clock.schedule(rotate, 0.1)
        if di == "down":
            shark.image = "shark"
            if shark.y <= 903:
                shark.y += random.choice(distance)
            else:
                shark.y -= random.choice(distance)
            clock.schedule(rotate, 0.1)
        if di == "left":
            shark.image = "shark left"
            if shark.x >= 100:
                shark.x -= random.choice(distance)
            else:
                shark.x += random.choice(distance)
            clock.schedule(rotate, 0.1)
        if di == "right":
            shark.image = "shark right"
            if shark.x <= 1400:
                shark.x += random.choice(distance)
            else:
                shark.x -= random.choice(distance)
            clock.schedule(rotate, 0.1)
        if gaston.x == shark.x - 20:
            if gaston.image == "gaston left":
                if shark.colliderect(gaston):
                    di = ""
                    shark.image = "shark left bite"
                    gaston.image = "gaston left hurt"
                    hp -= 1
                    chomp.play()
                    shark.x -= 20
                    clock.schedule(left3, 1)
                    clock.schedule(rotate, 2)
        if gaston.x == shark.x + 20:
            if gaston.image == "gaston right":
                if shark.colliderect(gaston):
                    di = ""
                    shark.image = "shark right bite"
                    gaston.image = "gaston right hurt"
                    hp -= 1
                    chomp.play()
                    shark.x += 20
                    clock.schedule(right3, 1)
                    clock.schedule(rotate, 2)
        if gaston.y == shark.y - 20:
            if gaston.image == "gaston up":
                if shark.colliderect(gaston):
                    di = ""
                    shark.image = "shark up bite"
                    gaston.image = "gaston up hurt"
                    hp -= 1
                    chomp.play()
                    shark.y -= 20
                    clock.schedule(up3, 1)
                    clock.schedule(rotate, 2)
        if gaston.y == shark.y + 20:
            if gaston.image == "gaston down":
                if shark.colliderect(gaston):
                    di = ""
                    shark.image = "shark down bite"
                    gaston.image = "gaston down hurt"
                    hp -= 1
                    chomp.play()
                    shark.y += 20
                    clock.schedule(down3, 1)
                    clock.schedule(rotate, 2)
        if di2 == "up":
            shark2.image = "shark up"
            if shark2.y >= 100:
                shark2.y -= random.choice(distance)
            else:
                shark2.y += random.choice(distance)
            clock.schedule(rotate2, 0.1)
        if di2 == "down":
            shark2.image = "shark"
            if shark2.y <= 903:
                shark2.y += random.choice(distance)
            else:
                shark2.y -= random.choice(distance)
            clock.schedule(rotate2, 0.1)
        if di2 == "left":
            shark2.image = "shark left"
            if shark2.x >= 100:
                shark2.x -= random.choice(distance)
            else:
                shark2.x += random.choice(distance)
            clock.schedule(rotate2, 0.1)
        if di2 == "right":
            shark2.image = "shark right"
            if shark2.x <= 1400:
                shark2.x += random.choice(distance)
            else:
                shark2.x -= random.choice(distance)
            clock.schedule(rotate2, 0.1)
        if gaston.x == shark2.x - 20:
            if gaston.image == "gaston left":
                if shark.colliderect(gaston):
                    di2 = ""
                    shark2.image = "shark left bite"
                    gaston.image = "gaston left hurt"
                    hp -= 1
                    chomp.play()
                    shark2.x -= 20
                    clock.schedule(left4, 1)
                    clock.schedule(rotate2, 2)
        if gaston.x == shark2.x + 20:
            if gaston.image == "gaston right":
                if shark.colliderect(gaston):
                    di = ""
                    shark2.image = "shark right bite"
                    gaston.image = "gaston right hurt"
                    hp -= 1
                    chomp.play()
                    shark2.x += 20
                    clock.schedule(right4, 1)
                    clock.schedule(rotate2, 2)
        if gaston.y == shark2.y - 20:
            if gaston.image == "gaston up":
                if shark.colliderect(gaston):
                    di = ""
                    shark2.image = "shark up bite"
                    gaston.image = "gaston up hurt"
                    hp -= 1
                    chomp.play()
                    shark2.y -= 20
                    clock.schedule(up4, 1)
                    clock.schedule(rotate2, 2)
        if gaston.y == shark2.y + 20:
            if gaston.image == "gaston down":
                if shark.colliderect(gaston):
                    di = ""
                    shark2.image = "shark down bite"
                    gaston.image = "gaston down hurt"
                    hp -= 1
                    chomp.play()
                    shark2.y += 20
                    clock.schedule(down4, 1)
                    clock.schedule(rotate2, 2)
        if gaston.colliderect(shark):
            if keyboard.a:
                shark.pos = 700, 0
                collision.play()
                score += 100
        if gaston.colliderect(shark2):
            if keyboard.a:
                shark2.pos = 700, 1400
                collision.play()
                score += 100
        if score == 1500:
            switch = 1
            if switch == 1:
                entry.image = "entry2"
                main.stop()
                shark.pos = 90000, 90000
                shark2.pos = 90000, 90000
                clock.schedule(nextt, 3)
                if keyboard.a:
                    switch = 2
                    entry.image = "0"
                    main.play(-1)
                    coconut.image = "coconut"
        if score > 1500 and score < 1710:
            if switch == 2:
                clock.schedule(spoil, 60)
                clock.schedule(reset, 0.1)
                if gaston.colliderect(coconut):
                    score += 20
                    coconut.x = randint(100, 1300)
                    coconut.y = randint(100, 800)
        if score == 1710:
            switch = 1
            if switch == 1:
                entry.image = "entry3"
                main.stop()
                coconut.x = 100000
                clock.schedule(nexttt, 3)
                if keyboard.a:
                    switch = 2
                    entry.image = "0"
                    boss.stop()
                    boss.play(-1)
                    kingshark.pos = 700, 100
                    fireball.pos = 700, 200
                    gaston.pos = 700, 800
                    fireball.image = "fireball"
                    fireball2.image = "fireball"
                    di3 = random.choice(x)
                    di4 = random.choice(x)
                    di5 = random.choice(x)
                    di6 = random.choice(x)
                    clock.schedule(fire, fly)
                    clock.schedule(fire2, fly2)
                    hp = 5
        if kingshark.x == 700:
            main.stop()
            if di3 and di4 == 0:
                    di3 = random.choice(x)
                    di4 = random.choice(x)
            if di5 and di6 == 0:
                    di5 = random.choice(x)
                    di6 = random.choice(x)
            if gaston.colliderect(fireball):
                squirt.play()
                if gaston.image == "gaston":
                    gaston.image = "gaston up hurt"
                    hp -= 1
                    clock.schedule(up3, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston down":
                    gaston.image = "gaston down hurt"
                    hp -= 1
                    clock.schedule(down3, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston left":
                    gaston.image = "gaston left hurt"
                    hp -= 1
                    clock.schedule(left, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston right":
                    gaston.image = "gaston right hurt"
                    hp -= 1
                    clock.schedule(right3, 1)
                    clock.schedule(fall, 0.1)
            if gaston.colliderect(fireball2):
                squirt.play()
                if gaston.image == "gaston":
                    gaston.image = "gaston up hurt"
                    hp -= 1
                    clock.schedule(up3, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston down":
                    gaston.image = "gaston down hurt"
                    hp -= 1
                    clock.schedule(down3, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston left":
                    gaston.image = "gaston left hurt"
                    hp -= 1
                    clock.schedule(left, 1)
                    clock.schedule(fall, 0.1)
                if gaston.image == "gaston right":
                    gaston.image = "gaston right hurt"
                    hp -= 1
                    clock.schedule(right3, 1)
                    clock.schedule(fall, 0.1)
            if gaston.colliderect(kingshark):
                if keyboard.a:
                    clock.schedule(fall, 0.1)
                    collision.play()
                    hp2 -= 1
            if hp2 == 0:
                switch = 1
                boss.stop()
                fireball.pos = -1000000, -1000000
                fireball2.pos = -1000000, -1000000
                gaston.pos = -10000, -100000
                fuel.image = "fuel"
                clock.schedule(flee, 0.1)
                finish.play()
                clock.schedule(ender, 64)
pgzrun.go()
