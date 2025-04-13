from pygame import *
from random import randint
from time import time as timer

# фонова музика
mixer.init()
mixer.music.load('doom_02.-Rip-_-Tear.ogg')
mixer.music.play()
fire_sound = mixer.Sound('aktivirovannaya-lazernaya-mina.ogg')
 
goal = 100


# шрифти і написи
font.init()
font1 = font.Font(None, 40)
font2 = font.Font(None, 36)
win = font1.render('ТИ КЛУТОЙ ПЕПСИКОЛЬНИЙ!', True, (255, 180, 51))
lose = font1.render('ТИ ОБОБА БАРАБУЛЬКА', True, (180, 0, 0))
font2 = font.Font(None, 36)


# нам потрібні такі картинки:
img_back = "galaxy.jpg"  # фон гри
img_hero = "pixil-frame-220.png"  # герой
img_bullet = "pixil-frame-890.png" # куля
img_enemy = "pixil-frame-2.png"  # ворог
img_ast = "pixil-frame-50.png" 
img_hero2 = "pixil-frame-20.png"  # герой 
img_enemy1 = "pixil-frame-4.png"  # ворог
img_enemy2 = "pixil-frame-05.png"  # ворог





skin = "pixil-frame-90 (1).png"
skin2 = "pixil-frame-09.png"
skin3 = "pixil3-frame-0.png"
skin4 = "pixil-frame-0 (14).png"
skin5 = "pixil-frame-03.png"
skin6 = "pixil-frame-06.png"
skin7 = "pixil-frame-0 2(1).png"
skin8 = "pixil-fra33me-0.png"
skin9 = "pixi4l-frame-0.png"




score = 0  # збито кораблів
lost = 0  # пропущено кораблів
max_lost = 15 # програли, якщо пропустили стільки
# клас-батько для інших спрайтів





class GameSprite1(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
 
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (100, 100))
        self.speed = player_speed
 
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y








class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
 
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 




    # метод, що малює героя у вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player1(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
 

    def fire (self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -105)
        bullets.add(bullet)  



# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed





    def fire (self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -105)
        bullets.add(bullet)  

























# клас спрайта-ворога
class Enemy(GameSprite1):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


class Enemy1(GameSprite1):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1




class Enemy2(GameSprite1):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()







# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

ship1 = Player1(img_hero2, 5, win_height - 100, 80, 100, 10)








monsters = sprite.Group()
for i in range(1, 2):
    monster = Enemy(img_enemy, randint(
        80, win_width - 80), -40, 80, 100, randint(1, 5))
    monsters.add(monster)



monsters1 = sprite.Group()
for i in range(1, 2):
    monster1 = Enemy1(img_enemy1, randint(
        80, win_width - 80), -40, 80, 100, randint(1, 5))
    monsters1.add(monster1)



monsters2 = sprite.Group()
for i in range(1, 2):
    monster2 = Enemy1(img_enemy2, randint(
        80, win_width - 80), -40, 80, 100, randint(1, 5))
    monsters2.add(monster2)









asteroids = sprite.Group()
for i in range(1, 6):
    asteroid = Enemy(img_ast, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    asteroids.add(asteroid)





bullets = sprite.Group()


# змінна "гра закінчилася": як тільки вона стає True, в основному циклі перестають працювати спрайти
finish = False
# Основний цикл гри:
run = True  # прапорець скидається кнопкою закриття вікна
 
num_fire = 0

rel_time = False

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False


        elif e.type == KEYDOWN:
            if e.key == K_RSHIFT:
                if num_fire < 30 and rel_time == False:
                    num_fire = num_fire + 1
                    fire_sound.play()
                    ship.fire()

                if num_fire >= 30 and rel_time == False:
                    last_time = timer()
                    rel_time = True







            if e.key == K_SPACE:
                if num_fire < 30 and rel_time == False:
                    num_fire = num_fire + 1
                    fire_sound.play()
                    ship1.fire()



                if num_fire >= 30 and rel_time == False:
                    last_time = timer()
                    rel_time = True




                
            if e.key == K_1:
                ship1 = Player1(skin, 5, win_height - 100, 80, 100, 10)

            if e.key == K_2:
                ship1 = Player1(skin2, 5, win_height - 100, 80, 100, 10)

            if e.key == K_3:
                ship1 = Player1(skin3, 5, win_height - 100, 80, 100, 10)

            if e.key == K_4:
                ship1 = Player1(skin4, 5, win_height - 100, 80, 100, 10)

            if e.key == K_5:
                ship1 = Player1(img_hero2, 5, win_height - 100, 80, 100, 10)


















            if e.key == K_6:
                ship = Player(skin5, 5, win_height - 100, 80, 100, 10)




            if e.key == K_7:
                ship = Player(skin6, 5, win_height - 100, 80, 100, 10)


            if e.key == K_8:
                ship = Player(skin7, 5, win_height - 100, 80, 100, 10)

            if e.key == K_9:
                ship = Player(skin8, 5, win_height - 100, 80, 100, 10)


























    if not finish:
        # оновлюємо фон
        window.blit(background, (0, 0))
 
        # пишемо текст на екрані
        text = font2.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
 
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        # рухи спрайтів
        ship.update()
        ship1.update()
        monsters.update()
        monsters1.update()
        bullets.update()
        asteroids.update()
        monsters2.update()


        # оновлюємо їх у новому місці при кожній ітерації циклу
        ship1.reset()
        ship.reset()
        monsters.draw(window)
        monsters1.draw(window)
        bullets.draw(window)
        asteroids.draw(window)
        monsters2.draw(window)


        if rel_time:
            now_time = timer()



            if now_time - last_time < 1:
                reload = font2.render("ПЕРЕЗАРЯДКА ", 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else: 
                num_fire = 0
                rel_time = False




 





        collides = sprite.groupcollide(monsters2, bullets, True, True)
        for c in collides:
            score = score + 1
            monster2 = Enemy(img_enemy2, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters2.add(monster2)


        collides = sprite.groupcollide(monsters1, bullets, True, True)
        for c in collides:
            score = score + 1
            monster1 = Enemy(img_enemy1, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters1.add(monster1)




        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)




        collides = sprite.groupcollide(asteroids, bullets, True, True)
        for c in collides:
            asteroid = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            asteroids.add(asteroid)























        if sprite.spritecollide(ship1, monsters, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))




        if sprite.spritecollide(ship1, monsters1, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))


        if sprite.spritecollide(ship1, monsters2, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))
  


























        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))




        if sprite.spritecollide(ship, monsters1, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))


        if sprite.spritecollide(ship, monsters2, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))



        if score >= goal:
            finish = True
            window.blit(win, (200, 200))


        display.update()
    # цикл спрацьовує кожні 0.05 секунд
    time.delay(65)
