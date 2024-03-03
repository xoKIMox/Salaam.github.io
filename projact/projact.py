import pygame
import random
from pygame import mixer
pygame.init()

#ชื่อเกม
pygame.display.set_caption("Salaam")

#ความเร็วเคลื่อนที่/FPS/score/time
SPEED = 10
ball_speed = 10
FPS = 60
score = 0
timeTRUE = 30
time = timeTRUE
frame_rate = 10
current_frame = 0
animation_speed = 0.1
Hit = 0



#เวลา
clock = pygame.time.Clock()

#ขนาดจอ
SCREEN_W = 1600
SCREEN_H = 880
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

#สี(RGB)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

#นำรูปเข้า
bg = pygame.image.load("bg.png")
#enemy = pygame.image.load("D:\projact\Fire_Spirit\Idle.png")
button_image = pygame.image.load("button.png")
ball = pygame.image.load("D:\\projact\\ball\\03.png")

#นำเสียงเข้า
windowmusic = mixer.music.load('D:\projact\MA_DaniilDavydov_NeonAeon_Main.wav')
windowmusic = mixer.music.play(0)

#Salaamcharacter
Salaamcharacter_Idle = [pygame.image.load("D:\\projact\\Green_Slime\\Idle (1).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (2).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (3).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (4).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (5).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (6).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (7).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (8).png")]

Salaamcharacter_Run = [pygame.image.load("D:\\projact\\Green_Slime\\Run (1).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (2).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (3).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (4).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (5).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (6).png"),
                       pygame.image.load("D:\\projact\\Green_Slime\\Run (7).png")]


Salaamcharacter_Attack = [pygame.image.load("D:\\projact\\Green_Slime\\Idle (1).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (2).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (3).png"),
                        pygame.image.load("D:\\projact\\Green_Slime\\Idle (4).png")]

character_direction = "Idle"
character_Salaam = Salaamcharacter_Idle


enemy = [pygame.image.load("D:\projact\Fire_Spirit\IdleFire .png"),
            pygame.image.load("D:\\projact\\Fire_Spirit\\IdleFire (1).png"),
            pygame.image.load("D:\\projact\\Fire_Spirit\\IdleFire (2).png"),
            pygame.image.load("D:\\projact\\Fire_Spirit\\IdleFire (3).png"),
            pygame.image.load("D:\\projact\\Fire_Spirit\\IdleFire (4).png"),
            pygame.image.load("D:\\projact\\Fire_Spirit\\IdleFire (5).png")]

#ตัวละครเดินในbg
bg_rect = bg.get_rect(center = [SCREEN_W//2,SCREEN_H//2])
Salaamcharacter_rect = Salaamcharacter_Run[0].get_rect()
enemy_rect = enemy[0].get_rect()
bg_y = 0
bg_x = 0

#ขนาดรูป
#bg_rect = bg.get_rect()
#character_Salaam = pygame.transform.scale(character_Salaam,(75,60))
#enemy = pygame.transform.scale(enemy,(50,50))
bg = pygame.transform.scale(bg,(SCREEN_W,SCREEN_H))
button_image = pygame.transform.scale(button_image, (300, 200))
ball = pygame.transform.scale(ball ,(50,50))

# ตำแหน่งปุ่ม/ปุ่มเริ่ม
buttonstart_rect = button_image.get_rect()
buttonstart_rect.center = (SCREEN_W // 2, SCREEN_H // 2)
buttonexit_rect = button_image.get_rect()
buttonexit_rect.center = (SCREEN_W // 2, SCREEN_H - 200)

# โหลดฟอนต์/ปรับขนาด
font_start = pygame.font.Font("Micro5-Regular.ttf", 60)
font_Salaam = pygame.font.Font("Micro5-Regular.ttf", 300)
font_time = pygame.font.Font("Micro5-Regular.ttf",100)
font_score = pygame.font.Font("Micro5-Regular.ttf",100)
font_endgame = pygame.font.Font("Micro5-Regular.ttf",200)
font_exit = pygame.font.Font("Micro5-Regular.ttf",60)
font_scoreend = pygame.font.Font("Micro5-Regular.ttf",60)
font_timescore = pygame.font.Font("Micro5-Regular.ttf",60)
font_Hp = pygame.font.Font("Micro5-Regular.ttf",100)


# สร้างตัวหนังสือ "เริ่ม"
start_text = font_start.render("start", True, (WHITE))
start_rect = start_text.get_rect()
start_rect.center = (buttonstart_rect.centerx, buttonstart_rect.centery - 10)

# สร้างตัวหนังสือ "Salaam"
Salaam_text = font_Salaam.render("Salaam", True, (WHITE))
Salaam_rect = Salaam_text.get_rect()
Salaam_rect.center = (SCREEN_W // 2, 200)

# สร้างตัวหนังสือ "time"
time_passed = clock.tick(1000)
time_text = font_time.render("Time : "+str(time),True,WHITE)
time_rect = time_text.get_rect()
time_rect.center = (SCREEN_W // 2, SCREEN_H - 800)

# สร้างตัวหนังสือ "end game"
endgame_text = font_endgame.render("End Game" , True,(RED))
endgame_rect = endgame_text.get_rect()
endgame_rect.center = (SCREEN_W // 2, 200)

# สร้างตัวหนังสือ "Exit"
exit_text = font_exit.render("Exit", True, (WHITE))
exit_rect = exit_text.get_rect()
exit_rect.center = (buttonexit_rect.centerx , buttonexit_rect.centery - 10)

#ตัวหนังสือ "score"
score_text = font_score.render("Score :  "+str(score),True,WHITE)
score_rect = score_text.get_rect()
score_rect.center = (SCREEN_W -1400, SCREEN_H - 800)

#ตัวหนังสือ "Hp"
HP = 3
HP_text = font_Hp.render("HP : " +str(HP),True,WHITE)
HP_rect = HP_text.get_rect()
HP_rect.topleft = (SCREEN_W -300, SCREEN_H - 850)

#ตำแหน่งcharacter
Salaamcharacter_rect.x = 299
Salaamcharacter_rect.y = 299

#ตำแหน่ง "Ball"
ball_rect = ball.get_rect()
ball_rect1 = ball.get_rect()
ball_rect2 = ball.get_rect()
ball_rect3 = ball.get_rect()
ball_rect4 = ball.get_rect()
ball_rect5 = ball.get_rect()
#ตำแหน่งenemy
enemy_rect.x = 100
enemy_rect.y = 100
#enemy_rect = enemy.get_rect()
#enemy_rect.center = (SCREEN_W // 2 ,SCREEN_H // 2-300 )

working = False
while True:

   # แสดงหน้าต่างเริ่มเกม
   start_window = True
   while start_window:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               game_over = True
               
           elif event.type == pygame.MOUSEBUTTONDOWN:
               # ตรวจสอบว่าคลิกอยู่ภายในปุ่มหรือไม่
               if buttonstart_rect.collidepoint(event.pos):
                   start_window = False

           if start_window == False:
               windowmusic = mixer.music.pause()

                   
   
       screen.blit(bg, (0, 0))
       screen.blit(button_image, buttonstart_rect)
       screen.blit(start_text, start_rect)
       screen.blit(Salaam_text, Salaam_rect)
       pygame.display.flip()
       clock.tick(FPS)
   
   
   #การรัน
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running=False

       timescore = time 

   # รับคำสั่งจากเมา/คีล์
       if event.type == pygame.MOUSEBUTTONDOWN:
           #ปุ้มเริ่ม
           mouse_x = event.pos[0]
           mouse_y = event.pos[1]
           Salaamcharacter_rect.centerx = mouse_x
           Salaamcharacter_rect.centery = mouse_y
   
       #การชน/สุ่ม/
       if Salaamcharacter_rect.colliderect(enemy_rect):
           enemy_rect.x=random.randint(0,SCREEN_W-100)
           enemy_rect.y=random.randint(0,SCREEN_H-100)
           #นับคะแนนเมื่อชน
           score+=1
           score_text = font_score.render("Score :  "+str(score),True,WHITE)
           Hit += 1
           time+=1
           scoretime = time
           
        #การชนบอล/สุ่ม/y   
       if Salaamcharacter_rect.colliderect(ball_rect):
           ball_rect.x = random.randint(0,SCREEN_W-100)
           ball_rect.y = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)


       if Salaamcharacter_rect.colliderect(ball_rect1): 
           ball_rect1.x = random.randint(0,SCREEN_W-100)
           ball_rect1.y = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)

       if Salaamcharacter_rect.colliderect(ball_rect2): 
           ball_rect2.x = random.randint(0,SCREEN_W-100)
           ball_rect2.y = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)

        #การชนบอล/สุ่ม/x       
       if Salaamcharacter_rect.colliderect(ball_rect3): 
           ball_rect3.y = random.randint(0,SCREEN_H-100)
           ball_rect3.x = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)


       if Salaamcharacter_rect.colliderect(ball_rect4): 
           ball_rect4.y = random.randint(0,SCREEN_H-100)
           ball_rect4.x = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)

       if Salaamcharacter_rect.colliderect(ball_rect5): 
           ball_rect5.y = random.randint(0,SCREEN_H-100)
           ball_rect5.x = -150
           HP -= 1
           HP_text = font_Hp.render("HP :  "+str(HP),True,WHITE)

        #การเคลื่อนที่ลูกบอล y
       if ball_rect.y < SCREEN_H:
           ball_rect.y+=ball_speed
           ball_speed += 0.002
       else:
            ball_rect.x = random.randint(0,SCREEN_W-100)
            ball_rect.y = -150  

       if score >=10  and ball_rect1.y < SCREEN_H:
           ball_rect1.y+=ball_speed + 2.5
           ball_speed += 0.002
       else:
            ball_rect1.x = random.randint(0,SCREEN_W-100)
            ball_rect1.y = -150  

       if score >=20  and ball_rect2.y < SCREEN_H:
           ball_rect2.y+=ball_speed + 5
           ball_speed += 0.002
       else:
            ball_rect2.x = random.randint(0,SCREEN_W-100)
            ball_rect2.y = -150  

        #การเคลื่อนที่ลูกบอล x

       if ball_rect3.x < SCREEN_W:
           ball_rect3.x+=ball_speed
           ball_speed += 0.002
       else:
            ball_rect3.y = random.randint(0,SCREEN_W-60)
            ball_rect3.x = -150
  

       if score >=10  and ball_rect4.x < SCREEN_W:
           ball_rect4.x+=ball_speed + 2.5
           ball_speed += 0.002
       else:
            ball_rect4.y = random.randint(0,SCREEN_H-60)
            ball_rect4.x = -150  

       if score >=20  and ball_rect5.x < SCREEN_W:
           ball_rect5.x+=ball_speed + 5
           ball_speed += 0.002
       else:
            ball_rect5.y = random.randint(0,SCREEN_H-60)
            ball_rect5.x = -150  

       #การเคลื่อนที่และขอบเขต 
       keys  = pygame.key.get_pressed()
       if keys[pygame.K_w] and Salaamcharacter_rect.top>0:
           character_direction = "Idle"
           character_Salaam = Salaamcharacter_Idle
           current_frame += animation_speed
           #bg_y += SPEED
           Salaamcharacter_rect.y-=SPEED
           if keys[pygame.K_LSHIFT] and Salaamcharacter_rect.left > 0:
                Salaamcharacter_rect.y -= SPEED /2

       if keys[pygame.K_s] and Salaamcharacter_rect.bottom<SCREEN_H -34:
           character_direction = "Idle"
           character_Salaam = Salaamcharacter_Idle
           current_frame += animation_speed
           #bg_y -= SPEED
           Salaamcharacter_rect.y+=SPEED
           if keys[pygame.K_LSHIFT] and Salaamcharacter_rect.left > 0:
                Salaamcharacter_rect.y += SPEED /2

       if keys[pygame.K_a] and Salaamcharacter_rect.left>0:
           character_direction = "RunA"
           character_Salaam = Salaamcharacter_Idle
           current_frame += animation_speed
           #bg_x -= SPEED
           Salaamcharacter_rect.x-=SPEED
           if keys[pygame.K_LSHIFT] and Salaamcharacter_rect.left > 0:
                Salaamcharacter_rect.x -= SPEED / 2
                character_Salaam = Salaamcharacter_Run

       if keys[pygame.K_d] and Salaamcharacter_rect.right<SCREEN_W:
           character_direction = "Run"
           character_Salaam = Salaamcharacter_Idle
           current_frame += animation_speed
           #bg_x -= SPEED
           Salaamcharacter_rect.x+=SPEED
           if keys[pygame.K_LSHIFT] and Salaamcharacter_rect.left > 0:
                Salaamcharacter_rect.x += SPEED /2
                character_Salaam = Salaamcharacter_Run

        # หากไม่มีการกระทำใด ๆ ให้ทำอนิเมชัน Run ต่อเนื่อง
       else:
            character_direction = "ldle"
            character_Salaam = Salaamcharacter_Idle
            current_frame += animation_speed

            enemy = enemy
            current_frame += animation_speed

       screen.fill((0,0,0))

       if current_frame >= len(character_Salaam): 
        current_frame = 0

       if current_frame >= len(enemy):  
        current_frame = 0

   
       #นัดเวลา
       time_passed = clock.tick(FPS)
       time -= time_passed / 1000
       if time < 0:
           time = 0
       time_text = font_time.render("Time : " + "{:.1f}".format(time), True, WHITE)
   
       if time==0:
           running = False

       if HP==0:
           running = False
   
   
       #ตำแหน่งในหน้าจอ/การแสดงภาพ
       #screen.blit(bg, bg_rect)
       screen.blit(bg, (bg_x,bg_y))
       screen.blit(character_Salaam[int(current_frame)], Salaamcharacter_rect )
       screen.blit(enemy[int(current_frame)],enemy_rect)
       screen.blit(ball,ball_rect)
       screen.blit(ball,ball_rect1)
       screen.blit(ball,ball_rect2)
       screen.blit(ball,ball_rect3)
       screen.blit(ball,ball_rect4)
       screen.blit(ball,ball_rect5)
       screen.blit(HP_text,HP_rect)
       screen.blit(score_text,score_rect)
       screen.blit(time_text,time_rect)
   
       #screen.blit(character,(500,500))
       #ขอบเขตการชน
       #pygame.draw.rect(screen,RED,character_rect,2)
       #pygame.draw.rect(screen,RED,enemy_rect,2)
       #pygame.draw.rect(screen,RED,ball_rect,2)
       pygame.display.flip()
       clock.tick(FPS)
   
   # แสดงหน้าต่างจบเริ่มเกม
   End_game = True
   while End_game:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               End_game = False

           elif event.type == pygame.MOUSEBUTTONDOWN:
               # ตรวจสอบว่าคลิกอยู่ภายในปุ่มหรือไม่
               if buttonexit_rect.collidepoint(event.pos):
                   End_game = False
                   game_over = False

   
   
       screen.blit(bg, (0, 0))
       screen.blit(button_image,buttonexit_rect)
       screen.blit(exit_text,exit_rect)
       screen.blit(endgame_text,endgame_rect)


       #ตัวหนังสือ "scoreend"
       scoreend_text = font_scoreend.render("Score        :    "+str(score),True,WHITE)
       scoreend_rect = scoreend_text.get_rect()
       scoreend_rect.topleft = (SCREEN_W - 1000 , SCREEN_H - 600)
       screen.blit(scoreend_text,scoreend_rect)

       # สร้างตัวหนังสือ "timescore"
       time_passed = clock.tick(1000)
       timescore_text = font_timescore.render("Timescore   :   " + "{:.1f}".format(timeTRUE+Hit), True, WHITE)
       timescore_rect = timescore_text.get_rect()
       timescore_rect.topleft = (SCREEN_W - 1000 , SCREEN_H - 500)
       screen.blit(timescore_text,timescore_rect)
   
       pygame.display.flip()
       clock.tick(FPS)
   
   
   pygame.display.update()
   clock.tick(60)
   pygame.quit()

