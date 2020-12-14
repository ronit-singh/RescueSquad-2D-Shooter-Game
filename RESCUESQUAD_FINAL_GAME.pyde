#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                       RESCUESQUAD - FINAL GAME PROJECT (Giorgi and Ronit)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# importing modules
import os
add_library('minim')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

path = os.getcwd()                 # stores the current working directory
 
# VARIABLES
state = 'start'                    # checks whether player is on start screen or not
select = 0                         # keeps track of the menus on start screen
gun_select = 0                     # keeps track of the type of gun selected by the player
ammo_count = 10                    # keeps the count of the bullets left
ammo_count_initial = ammo_count    # keeps the total count of the bullets
num_reload = 0
reload = False                     # to check if the player has reloaded or not
level = 1                          # stores the current level (1, 2, or 3)
level_initial = 3                  # total number of levels
total_score = 0                    # to store total score
enemy_count = 0                    # counts the number of enemies in the level
host_count = 0                     # counts the number of hostages in the level
total_enemies_level = 5            # counts the number of enemies in the level
total_enemy_killed = 0             # counts the number of enemies killed in the level
total_host_killed = 0              # counts the number of hostages killed in the level


# variables for clock/timer    
col = color(255)                   # stores the color of the clock/timer
sec = 0                            # stores 'seconds' in timer
minutes = 0                        # stores 'minutes' in timer
hours = 0                          # stores 'hours' in timer
fin_sec = 0                        # stores 'seconds' for end screen
fin_min = 0                        # stores 'minutes' for end screen
fin_hour = 0                       # stores 'hours' for end screen

# boolean variables for controlling main functionalities
up_pressed = False                 # stores true or false when 'W' key is pressed or not
left_pressed = False               # stores true or false when 'A' key is pressed or not
right_pressed = False              # stores true or false when 'D' key is pressed or not
down_pressed = False               # stores true or false when 'S' key is pressed or not
game_started = False               # stores true or false when game started or not
endgame = False                    # to check if player voluntarily ended the game
endscreen = False                  # to check if endscreen should appear or not
clock = True                       # to ensure clock doesn't run on endscreen

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# loading all the images used in the game
img = loadImage(path + "/images/" + "RESCUESQUAD.png")
img2 = loadImage(path + "/images/" + "keys.jpg")
img3 = loadImage(path + "/images/" +"spacebar.png")
img4 = loadImage(path + "/images/" + "mouse.PNG")
img5 = loadImage(path + "/images/" + "selectlocation.png")
img6 = loadImage(path + "/images/" + "arrow.png")
img_fire = loadImage(path + "/images/fire2.png")
img_guns = loadImage(path + "/images/" + "gun_select.png")
img_killed = loadImage(path + "/images/" + "killedt.png")
img_killedh = loadImage(path + "/images/" + "killed.png")
img_shooter = loadImage(path + "/images/" + "shootermain.png")
img_aim = loadImage(path + "/images/" + "aim2.png")
img_bg = loadImage(path + "/images/" + "level1.png")
img_alive = loadImage(path + "/images/enemy_alive.png")
img_dead = loadImage(path + "/images/dead.jpg")
img_stats_board = loadImage(path + "/images/stats_board.PNG")
img_exit = loadImage(path + "/images/exit.png")
img_heading = loadImage(path + "/images/heading.PNG")
img_next1 = loadImage(path + "/images/next1.png")
img_next2 = loadImage(path + "/images/next2.png")
img_next3 = loadImage(path + "/images/next3.png")
img_end = loadImage(path + "/images/endscreentest.jpg")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# loading all the sounds used in the game
minim=Minim(this)
intro=minim.loadFile(path + "/sounds/mainintrosong.mp3")
click=minim.loadFile(path + "/sounds/clicksound.mp3")
player = Minim(this)
shot_sound = player.loadFile(path + "/sounds/Gunshot.mp3")
bg_sound = player.loadFile(path + "/sounds/maingamesound.mp3")
gun_screen_sound = minim.loadFile(path + "/sounds/gunscreen.mp3")

# variables for ENEMIES and HOSTAGES
enemy_1 = 0
enemy_2 = 0
enemy_3 = 0
enemy_4 = 0
enemy_5 = 0
enemy_6 = 0
enemy_7 = 0
enemy_8 = 0
enemy_9 = 0
enemy_10 = 0
enemy_11 = 0
enemy_12 = 0
enemy_13 = 0 
enemy_14 = 0
enemy_15 = 0

host_1 = 0
host_2 = 0
host_3 = 0
host_4 = 0
host_5 = 0
score_enemy1 = 0
score_enemy2 = 0
score_enemy3 = 0
score_enemy4 = 0
score_enemy5 = 0
score_enemy6 = 0
score_enemy7 = 0
score_enemy8 = 0
score_enemy9 = 0
score_enemy10 = 0
score_enemy11 = 0
score_enemy12 = 0
score_enemy13 = 0
score_enemy14 = 0
score_enemy15 = 0

score_host1 = 0
score_host2 = 0
score_host3 = 0
score_host4 = 0
score_host5 = 0


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# shooter or player's starting co-ordinates and walking speed
x = 500
y = -150
speed = 12

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Shooter:
    
    def __init__(self, x, y, speed, ammo_count, num_reload):
        
        self.enemypositions1 = [[2052, 1367],[1158,485], [1398, 437], [1878, 1085], [2226, 1529]]   # Enemy Position Coordinates for level1 map
        self.hostpositions1 = [[1194,581], [1206,799], [1926,1193]]                                 # Hostage Position Coordinates for level1 map
        self.enemypositions2 = [[1338, 173],[1974,245], [1434, 965], [1518, 1481], [2100, 1490]]    # Enemy Position Coordinates for level2 map
        self.hostpositions2 = [[1374, 1241], [1890, 1540]]                                          # Hostage Position Coordinates for level2 map
        self.enemypositions3 = [[930, 641],[1782, 533], [690,1455], [1062,1565], [1440, 1420]]      # Enemy Position Coordinates for level3 map
        self.startingposition = [750, 425]                                                          # Our shooter's starting Position Coordinates
        self.x = x
        self.y = y
        self.speed = speed
        self.ammo_count = ammo_count
        self.num_reload = num_reload
        self.killed_first1 = False                                                                 # Boolean Variables for enemies killed on level1 map
        self.killed_second1 = False
        self.killed_third1 = False
        self.killed_fourth1 = False
        self.killed_fifth1 = False
        self.killed_host11 = False                                                                 # Boolean Variables for hostages killed on level1 map
        self.killed_host12 = False
        self.killed_host13 = False
        self.killed_first2 = False                                                                 # Boolean Variables for enemies killed on level2 map
        self.killed_second2 = False
        self.killed_third2 = False
        self.killed_fourth2 = False
        self.killed_fifth2 = False    
        self.killed_host21 = False                                                                 # Boolean Variables for hostages killed on level2 map
        self.killed_host22 = False
        self.killed_first3 = False                                                                 # Boolean Variables for hostages killed on level3 map
        self.killed_second3 = False
        self.killed_third3 = False
        self.killed_fourth3 = False
        self.killed_fifth3 = False
        
    # function for overall gameplay
    # def updateEnemyPositions(self, ):
        
    
    def playGame(self):
        global up_pressed, right_pressed, left_pressed, down_pressed, level, score, enemy_count, total_enemies_level1, host_count, gun_select
        global enemy_1, enemy_2, enemy_3, enemy_4, enemy_5,enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, host_1, host_2, host_3, total_enemy_killed, total_host_killed, reload, ammo_count_initial
        global enemy_11, enemy_12, enemy_13, enemy_14, enemy_15, score_enemy11, score_enemy12, score_enemy13, score_enemy14, score_enemy15
        global score_enemy1, score_enemy2, score_enemy3, score_enemy4, score_enemy5,score_enemy6, score_enemy7, score_enemy8, score_enemy9, score_enemy10
        global score_host1, score_host2, score_host3, score_host4, score_host5, total_score, img_bg, img_next1, img_next2, img_next3, endscreen
        
        if level == 1:
            img_bg = loadImage(path + "/images/" + "level1.png")
        elif level == 2:
            img_bg = loadImage(path + "/images/" + "level2.jpg")
        elif level == 3:
            img_bg = loadImage(path + "/images/" + "level3.jpg")
        
        bg_sound.play()
        background(0)
        image(img_bg, self.x, self.y, 2000, 2000)      # background (according to level)
        
        # checking if player has pressed W, A, S, or D key and moving it accordingly
        # and updating enemies and hostages Coordinates as player is moving.
        if up_pressed:
            self.y += self.speed
            self.enemypositions1[0][1] += self.speed 
            self.enemypositions1[1][1] += self.speed
            self.enemypositions1[2][1] += self.speed
            self.enemypositions1[3][1] += self.speed
            self.enemypositions1[4][1] += self.speed
            self.hostpositions1[0][1] += self.speed
            self.hostpositions1[1][1] += self.speed
            self.hostpositions1[2][1] += self.speed
            self.enemypositions2[0][1] += self.speed
            self.enemypositions2[1][1] += self.speed
            self.enemypositions2[2][1] += self.speed
            self.enemypositions2[3][1] += self.speed
            self.enemypositions2[4][1] += self.speed
            self.hostpositions2[0][1] += self.speed
            self.hostpositions2[1][1] += self.speed
            self.enemypositions3[0][1] += self.speed
            self.enemypositions3[1][1] += self.speed
            self.enemypositions3[2][1] += self.speed
            self.enemypositions3[3][1] += self.speed
            self.enemypositions3[4][1] += self.speed
            
            self.startingposition[1] += self.speed
            
        elif left_pressed:
            self.x += self.speed
            self.enemypositions1[0][0] += self.speed
            self.enemypositions1[1][0] += self.speed
            self.enemypositions1[2][0] += self.speed
            self.enemypositions1[3][0] += self.speed
            self.enemypositions1[4][0] += self.speed
            self.hostpositions1[0][0] += self.speed
            self.hostpositions1[1][0] += self.speed
            self.hostpositions1[2][0] += self.speed
            self.enemypositions2[0][0] += self.speed
            self.enemypositions2[1][0] += self.speed
            self.enemypositions2[2][0] += self.speed
            self.enemypositions2[3][0] += self.speed
            self.enemypositions2[4][0] += self.speed
            self.hostpositions2[0][0] += self.speed
            self.hostpositions2[1][0] += self.speed
            self.enemypositions3[0][0] += self.speed
            self.enemypositions3[1][0] += self.speed
            self.enemypositions3[2][0] += self.speed
            self.enemypositions3[3][0] += self.speed
            self.enemypositions3[4][0] += self.speed
            
            
            self.startingposition[0] += self.speed
        elif right_pressed:
            self.x -= self.speed
            self.enemypositions1[0][0] -= self.speed
            self.enemypositions1[1][0] -= self.speed
            self.enemypositions1[2][0] -= self.speed
            self.enemypositions1[3][0] -= self.speed
            self.enemypositions1[4][0] -= self.speed
            self.hostpositions1[0][0] -= self.speed
            self.hostpositions1[1][0] -= self.speed
            self.hostpositions1[2][0] -= self.speed
            self.enemypositions2[0][0] -= self.speed
            self.enemypositions2[1][0] -= self.speed
            self.enemypositions2[2][0] -= self.speed
            self.enemypositions2[3][0] -= self.speed
            self.enemypositions2[4][0] -= self.speed
            self.hostpositions2[0][0] -= self.speed
            self.hostpositions2[1][0] -= self.speed
            self.enemypositions3[0][0] -= self.speed
            self.enemypositions3[1][0] -= self.speed
            self.enemypositions3[2][0] -= self.speed
            self.enemypositions3[3][0] -= self.speed
            self.enemypositions3[4][0] -= self.speed
           
            
            
            self.startingposition[0] -= self.speed
            
        elif down_pressed:
            self.y -= self.speed
            self.enemypositions1[0][1] -= self.speed
            self.enemypositions1[1][1] -= self.speed
            self.enemypositions1[2][1] -= self.speed
            self.enemypositions1[3][1] -= self.speed
            self.enemypositions1[4][1] -= self.speed
            self.hostpositions1[0][1] -= self.speed
            self.hostpositions1[1][1] -= self.speed
            self.hostpositions1[2][1] -= self.speed
            self.enemypositions2[0][1] -= self.speed
            self.enemypositions2[1][1] -= self.speed
            self.enemypositions2[2][1] -= self.speed
            self.enemypositions2[3][1] -= self.speed
            self.enemypositions2[4][1] -= self.speed
            self.hostpositions2[0][1] -= self.speed
            self.hostpositions2[1][1] -= self.speed
            self.enemypositions3[0][1] -= self.speed
            self.enemypositions3[1][1] -= self.speed
            self.enemypositions3[2][1] -= self.speed
            self.enemypositions3[3][1] -= self.speed
            self.enemypositions3[4][1] -= self.speed
            
            
            self.startingposition[1] -= self.speed
        elif reload:
            self.ammo_count = ammo_count_initial # Reloading the gun
        
        # adding functionality to rotate player/shooter using mouse
        pushMatrix()
        translate(width/2, height/2)
        angle = atan2(mouseX-width/2, mouseY-height/2)
        rotate(angle*-1)
        fill(255)
        image(img_shooter, -50, -50, 100, 100, 300, 300, 0, 0)
        
        # to check ammo count/bullets
        if reload and self.num_reload > 0:
                self.ammo_count += 10
                self.num_reload -= 1
                
        # shooting bullets on mouse click
        if(mousePressed and game_started and self.ammo_count > 0 and frameCount % 2 == 0):
            shot_sound.rewind()
            shot_sound.play()
            image(img_fire, -10, 35, 20, 20)
            self.ammo_count -= 1
        popMatrix()
        
        pushMatrix()
        translate(self.x, self.y)
        fill(255, 0, 0)
        # Detecting when mouse click matches enemies or hostages coordinates in order to detect the kill condition.
        
        #This is for level 1
        if level == 1:
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions1[0][0] - 50 and mouseX <= self.enemypositions1[0][0] + 30 and mouseY >= self.enemypositions1[0][1] and mouseY <= self.enemypositions1[0][1] + 80):
                self.killed_first1 = True
                enemy_1 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if self.killed_first1:
                image(img_killed,1480 ,1515, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions1[1][0] - 20 and mouseX <= self.enemypositions1[1][0] + 30 and mouseY >= self.enemypositions1[1][1]-55 and mouseY <= self.enemypositions1[1][1] + 15):
                self.killed_second1 = True
                enemy_2 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)

            if self.killed_second1:
                image(img_killed,615 ,560, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions1[2][0] - 32 and mouseX <= self.enemypositions1[2][0] + 30 and mouseY >= self.enemypositions1[2][1]-35 and mouseY <= self.enemypositions1[2][1] + 36):
                self.killed_third1 = True
                enemy_3 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_third1:
                image(img_killed,844, 542, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions1[3][0] - 28 and mouseX <= self.enemypositions1[3][0] + 25 and mouseY >= self.enemypositions1[3][1]-41 and mouseY <= self.enemypositions1[3][1] + 30):
                self.killed_fourth1 = True
                enemy_4 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_fourth1:
                image(img_killed,1333, 1176, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions1[4][0] - 22 and mouseX <= self.enemypositions1[4][0] + 32 and mouseY >= self.enemypositions1[4][1]-45 and mouseY <= self.enemypositions1[4][1] + 30):
                self.killed_fifth1 = True
                enemy_5 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_fifth1:
                image(img_killed,1687, 1624, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.hostpositions1[0][0] - 22 and mouseX <= self.hostpositions1[0][0] + 32 and mouseY >= self.hostpositions1[0][1]-45 and mouseY <= self.hostpositions1[0][1] + 30):
                self.killed_host11 = True
                host_1 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_host11:
                image(img_killedh,633,671, 120, 120)
            
            if (mousePressed and mouseClicked and mouseX >= self.hostpositions1[1][0] - 18 and mouseX <= self.hostpositions1[1][0] + 30 and mouseY >= self.hostpositions1[1][1]-83 and mouseY <= self.hostpositions1[1][1] + 17):
                self.killed_host12 = True
                host_2 = 1 
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_host12:
                image(img_killedh,665,850, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.hostpositions1[2][0] - 22 and mouseX <= self.hostpositions1[2][0] + 32 and mouseY >= self.hostpositions1[2][1]-45 and mouseY <= self.hostpositions1[2][1] + 30):
                self.killed_host13 = True
                host_3 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_host13:
                image(img_killedh,1386,1278, 120, 120)
                
            if total_enemy_killed == 5: # If 5 enemies are killed, the game is over.
                endscreen = True
                
        # This is for level 2        
        if level == 2:    
            if ( mousePressed and mouseClicked and mouseX >= self.enemypositions2[0][0] - 22 and mouseX <= self.enemypositions2[0][0] + 22 and mouseY >= self.enemypositions2[0][1] - 44 and mouseY <= self.enemypositions2[0][1] + 16):
                self.killed_first2 = True
                enemy_6 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
            
            if self.killed_first2:
                image(img_killed,798, 273, 120, 120)
                
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions2[1][0] - 22 and mouseX <= self.enemypositions2[1][0] + 22 and mouseY >= self.enemypositions2[1][1] - 44 and mouseY <= self.enemypositions2[1][1] + 16):
                self.killed_second2 = True
                enemy_7 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if self.killed_second2:
                image(img_killed,1424,335, 120, 120) 
                                                            
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions2[2][0] - 32 and mouseX <= self.enemypositions2[2][0] + 22 and mouseY >= self.enemypositions2[2][1] - 44 and mouseY <= self.enemypositions2[2][1] + 36):
                self.killed_third2 = True
                enemy_8 = 1 
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if self.killed_third2:
                image(img_killed,882, 1062, 120, 120)
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions2[3][0] - 22 and mouseX <= self.enemypositions2[3][0] + 22 and mouseY >= self.enemypositions2[3][1] - 44 and mouseY <= self.enemypositions2[3][1] + 16):
                self.killed_fourth2 = True
                enemy_9 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
           
                
            if self.killed_fourth2:
                image(img_killed,985,1596, 120, 120)
                
                
            if (mousePressed and mouseClicked and mouseX >= self.enemypositions2[4][0] - 22 and mouseX <= self.enemypositions2[4][0] + 22 and mouseY >= self.enemypositions2[4][1] - 44 and mouseY <= self.enemypositions2[4][1] + 16):
                self.killed_fifth2 = True
                enemy_10 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
                    
            if self.killed_fifth2:
                image(img_killed,1540,1580, 120, 120)
                
            if (  mouseClicked and mousePressed and mouseX >= self.hostpositions2[0][0] - 22 and mouseX <= self.hostpositions2[0][0] + 32 and mouseY >= self.hostpositions2[0][1]-45 and mouseY <= self.hostpositions2[0][1] + 30):
                self.killed_host21 = True
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_host21:
                image(img_killedh,834,1320, 120, 120)
                
            if (  mouseClicked and mousePressed and mouseX >= self.hostpositions2[1][0] - 22 and mouseX <= self.hostpositions2[1][0] + 32 and mouseY >= self.hostpositions2[1][1]-45 and mouseY <= self.hostpositions2[1][1] + 30):
                self.killed_host22 = True
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if  self.killed_host22:
                image(img_killedh,1350,1600, 120, 120)
                
            if total_enemy_killed == 5: # If 5 enemies are killed, the game is over.
                endscreen = True
        #This is for level3
        if level == 3:
            if (mouseClicked and mousePressed and mouseX >= self.enemypositions3[0][0] - 50 and mouseX <= self.enemypositions3[0][0] + 50 and mouseY >= self.enemypositions3[0][1] -40 and mouseY <= self.enemypositions3[0][1] + 30):
                self.killed_first3 = True
                enemy_11 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20) 
                
                
            if self.killed_first3:
                image(img_killed,370, 721, 120, 120)
            
            if (mouseClicked and mousePressed and mouseX >= self.enemypositions3[1][0] - 50 and mouseX <= self.enemypositions3[1][0] + 50 and mouseY >= self.enemypositions3[1][1]-35 and mouseY <= self.enemypositions3[1][1] + 35):
                self.killed_second3 = True
                enemy_12 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)

                
            if self.killed_second3:
                image(img_killed,1222, 623, 120, 120)
            
            if (mouseClicked and mousePressed and mouseX >= self.enemypositions3[2][0] - 50 and mouseX <= self.enemypositions3[2][0] + 50 and mouseY >= self.enemypositions3[2][1]-35 and mouseY <= self.enemypositions3[2][1] + 35):
                self.killed_third3 = True
                enemy_12 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20) 
                
            if self.killed_third3:
                image(img_killed,110,1530, 120, 120)
            
            if (mouseClicked and mousePressed and mouseX >= self.enemypositions3[3][0] - 50 and mouseX <= self.enemypositions3[3][0] + 50 and mouseY >= self.enemypositions3[3][1]-35 and mouseY <= self.enemypositions3[3][1] + 35):
                self.killed_fourth3 = True
                enemy_14 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if self.killed_fourth3:
                image(img_killed,500, 1645, 120, 120)
            
            if (mouseClicked and mousePressed and mouseX >= self.enemypositions3[4][0] - 50 and mouseX <= self.enemypositions3[4][0] + 50 and mouseY >= self.enemypositions3[4][1]-35 and mouseY <= self.enemypositions3[4][1] + 35):
                self.killed_fifth3 = True
                enemy_15 = 1
                shot_sound.rewind()
                shot_sound.play()
                image(img_fire, -10, 35, 20, 20)
                
            if self.killed_fifth3:
                image(img_killed,885, 1510, 120, 120)
                
            if total_enemy_killed == 5: # If 5 enemies are killed, the game is over.
                endscreen = True
        # Getting the total number of killed hostages and enemies    
        total_enemy_killed = enemy_1 + enemy_2 + enemy_3 + enemy_4 + enemy_5 + enemy_6 + enemy_7 + enemy_8 + enemy_9 + enemy_10 + enemy_11 + enemy_12 + enemy_13 + enemy_14 + enemy_15
        total_host_killed = host_1 + host_2 + host_3 + host_4 + host_5

        popMatrix()        
        
        image(img_heading, 0, 0, 1500, 90)
        image(img_stats_board, 1120, 0, 380, 230)
        
        features.clock()     # displays the timer/clock on screen while playing
        
        # displaying game statistics
        fill(255)
        textSize(30)
        text("AMMO LEFT: " + str(self.ammo_count) + " / " + str(ammo_count_initial), 1160, 40)
        textSize(25)
        text("LEVEL: " + str(level) + " / " + str(level_initial), 1160, 75)
        text("TIME: ", 1160, 110)
        text("ENEMIES KILLED: " + str(total_enemy_killed) + " / " + str(total_enemies_level), 1160, 145)
        text("SCORE: " + str(total_enemy_killed * 500 - total_host_killed * 500), 1160, 182)
        
        if (mouseClicked and mouseX > 10 and mouseX < 70 and mouseY > 10 and mouseY < 70):
        
            state = 'start'
        
        # aiming icon (uses mouse's position on screen)
        strokeWeight(0)
        fill(255, 0, 0)
        image(img_aim, mouseX- 43//2, mouseY- 45//2,43,45)
        image(img_exit, 8, 10, 65, 65)
        image(img_next1, 990, 730, 160, 160)
        image(img_next2, 1160, 730, 160, 160)
        image(img_next3, 1330, 730, 160, 160)
        
        # resetting position and variables when clicked on next level
        if (mousePressed and mouseClicked and mouseX > 990 and mouseX < 1150 and mouseY > 730 and mouseY < 890):
            level = 1
            self.x = 500
            self.y = -150
            self.ammo_count = 10
            total_score = 0
            total_enemy_killed = 0
            total_host_killed = 0
            
        elif (mousePressed and mouseClicked and mouseX > 1180 and mouseX < 1320 and mouseY > 730 and mouseY < 890):
            level = 2
            self.x = 500
            self.y = -150
            self.ammo_count = 10
            total_score = 0
            total_enemy_killed = 0
            total_host_killed = 0
            
        elif (mousePressed and mouseClicked and mouseX > 1330 and mouseX < 1490 and mouseY > 730 and mouseY < 890):
            level = 3
            self.x = 500
            self.y = -150
            self.ammo_count = 10
            total_score = 0
            total_enemy_killed = 0
            total_host_killed = 0
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Features:
    
    def __init__(self, sec, minutes, hours, col):
        
        self.sec = sec
        self.minutes = minutes
        self.hours = hours
        self.col = col
         
    # function for clock/timer
    def clock(self):
        global fin_min, fin_hour, fin_sec, clock
        
        if clock:
            if frameCount % 30 == 0:
                self.sec+=1
                fin_sec += 1
            if(self.sec == 60):
                self.sec = 0
                self.minutes+=1
                fin_min += 1
            if(self.minutes == 60):
                self.minutes = 0
                self.hours+=1
                fin_hour += 1
            if(self.hours == 24):
                self.hours = 0
                self.minutes = 0
                self.sec = 0
            
            # displaying the clock/timer     
            textSize(25)
            fill(255)
            text(floor(self.sec), 1335, 110)
            text(floor(self.minutes), 1285, 110)
            text(floor(self.hours), 1235, 110)
            
            # for blinking colons
            if(self.sec % 2 == 0):
                self.col = color(0)
            else:
                self.col = color(255)
            
            fill(self.col)
            textSize(30)
            text(":", 1270, 110)
            text(":", 1320, 110)
                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Submenus:
    
    def __init__(self, num_reload):
        
        self.num_reload = num_reload

    # HOW TO PLAY screen
    def howToPlay(self):
        
        background(255)
        fill(0)
        textSize(30)
        text("GAME INSTRUCTIONS",600,40)
        text("____________________________________________________________________________________________________",0,60)
        textSize(20)
        text("OBJECTIVE: Complete the missions without penalties - and do it fast for a higher score.",8,110)
        text("You have 3 missions or levels in the game: LVL 1 - MANSION (Easy)",122,140) 
        text("LVL 2 - HOTEL (Medium)",542,170)
        text("LVL 3 - BANK (Difficult)",542,200)
        text("KEYS TO USE:",8,300)
        image(img2,8,300,200,200)
        text("W - Move Up",220,350)
        text("S - Move Down",222,380)
        text("A - Move Left",220,410)
        text("D - Move Right",220,440)
        image(img3,8,500,190,80)
        text("SPACEBAR - Reload the Gun when Bullets Finish",220,540)
        image(img4,8,610,170,180)
        text("Move MOUSE to Aim",220,680)
        text("When the Aim is above the Enemy, Left MOUSE Click to Shoot",220,710)
        image(img6, 8, 8, 65, 65)
        text("SCORING SYSTEM:", 900, 350)
        text("1 Enemy Kill = +500 Points", 920, 390)
        text("1 Hostage Kill = -500 Points", 920, 430)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def gun_select_func(self):
        
        global gun_select, select
        image(img_guns, 0, 0, 1500, 900)
        image(img6, 8, 8, 65, 65)
        
        gun_screen_sound.play()
        if (mousePressed and mouseClicked and mouseX > 65 and mouseX < 335 and mouseY > 680 and mouseY < 770 and select == 1):

            gun_screen_sound.close()
            gun_select = 1

        elif (mousePressed and mouseClicked and mouseX > 640 and mouseX < 910 and mouseY > 675 and mouseY < 765 and select == 1):
            #print("game started2")
            gun_screen_sound.close()
            gun_select = 2

        elif (mousePressed and mouseClicked and mouseX > 1170 and mouseX < 1440 and mouseY > 680 and mouseY < 770 and select == 1):
            #print("game started3")
            gun_screen_sound.close()
            gun_select = 3

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # LEVEL/LOCATION SELECTION screen 
    def level_select(self):
        
        global select, level, img_bg
        
        if (mousePressed and mouseClicked and mouseX > 65 and mouseX < 335 and mouseY > 680 and mouseY < 770 and select == 2):
                img_bg = loadImage(path + "/images/" + "level1.png")
                level = 1
                select = 1
                self.num_reload = 0
        elif (mousePressed and mouseX > 640 and mouseX < 910 and mouseY > 675 and mouseY < 765 and select == 2):
                img_bg = loadImage(path + "/images/" + "level2.jpg")  
                level = 2  
                select = 1
                self.num_reload = 1
        elif (mousePressed and mouseX > 1170 and mouseX < 1440 and mouseY > 680 and mouseY < 770 and select == 2):
                img_bg = loadImage(path + "/images/" + "level3.jpg") 
                level = 3   
                select = 1
                self.num_reload = 4
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
def mouseClicked():
    
    global state, select, level_select, img_bg
    if state == 'start':
        # mouse events for the START screen
        if (mouseClicked and mouseX > 920 and mouseX < 1360 and mouseY > 285 and mouseY < 425):
            
            click.play()
            click.rewind()
            state = 'back'
            select = 1
            
        elif (mouseClicked and mouseX > 920 and mouseX < 1360 and mouseY > 468 and mouseY < 610):
            click.play()
            click.rewind()
            state = 'back'
            select = 2
            
        elif (mouseClicked and mouseX > 920 and mouseX < 1360 and mouseY > 659 and mouseY < 801):
            click.play()
            click.rewind()
            state = 'back'
            select = 3

    elif state == 'back':
        # mouse events for the BACK screen
        if (mouseClicked and mouseX > 10 and mouseX < 70 and mouseY > 10 and mouseY < 70):
        
            state = 'start'

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyPressed():
    
    global up_pressed, left_pressed, right_pressed, down_pressed, reload, endgame

    if key == 'w':
        up_pressed = True
    elif key == 'a':
        left_pressed = True
    elif key == 'd':
        right_pressed = True
    elif key == 's':
        down_pressed = True
    elif keyCode == 32:
        reload = True
    elif key == ESC:
        endgame = True
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyReleased():
    
    global up_pressed, left_pressed, right_pressed, down_pressed, reload, endgame

    if key == 'w':
        up_pressed = False
    elif key == 'a':
        left_pressed = False
    elif key == 'd':
        right_pressed = False
    elif key == 's':
        down_pressed = False
    elif keyCode == 32:
        reload = False
    elif keyCode == 'r':
        endgame = False
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

shooter = Shooter(x, y, speed, ammo_count, num_reload)
features = Features(sec, minutes, hours, col)
submenus = Submenus(num_reload)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setup():
    
    global intro, click
    
    size(1500,850)

def draw():
    
    global img_bg, game_started, clock, state, endscreen, total_enemy_killed

    submenus.level_select()    # displays the level selection screen
    
    intro.play()
    
    # displaying the starting main screen
    if state == 'start':
        image(img, 0, 0, 1500, 900)
        noFill()
        
    elif state == 'back':
        if select == 1:                  # if player clicks 'START' on the main screen
            intro.close()
            
            # for displaying the gun type selection screen
            if gun_select == 0:
                submenus.gun_select_func()
            
            if gun_select != 0:
                shooter.playGame()
                game_started = True
                

        elif select == 2:                # if player clicks 'CHOOSE LOCATION' on the main screen
            image(img5, 0, 0, 1500, 900)
            image(img6, 8, 8, 65, 65)
            
        elif select == 3:                # if player clicks 'HOW TO PLAY' on the main screen
            submenus.howToPlay()
        #End screen depiction.
        if endscreen:
            clock = False     # to ensure clock/timer does't run on endscreen
            image(img_end, 0, 0, 1500, 850)
            textSize(50)
            fill(57,255,20)
            text("Final Score: " + str(total_enemy_killed * 500 - total_host_killed * 500), 10, 50)
            text("Kills: "+ str(total_enemy_killed), 10, 150)
            text("Penalties: " + str(total_host_killed), 10, 250)
            text("Runtime: "+ str(fin_hour)+ ":" + str(fin_min) + ":" + str(fin_sec) , 10, 350)
            text("Thank you for playing!", 10, 650)
            text("Click anywhere to RESTART!", 10, 720)
            text("or press ESC to close!", 10, 790)
            
            # To restart on click after game over
            if (mouseClicked and mousePressed):
                state = 'start'

#---------------------------------------------------------------------- END OF THE PROGRAM -------------------------------------------------------------------------
