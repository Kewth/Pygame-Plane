'''
飞机大战
'''

import pygame, random, sys
from pygame.locals import *
from modules import *
# from modules.cfg import *
from cfg import *

def draw_status ():
    start = 3
    for i in range(LIFE_MAX):
        heart = IMAGE_DICT['heart'] if i < life else IMAGE_DICT['cross']
        rect = heart.get_rect()
        rect.top = 3
        rect.left = start
        start += rect.width
        screen.blit(heart, rect)

    if super_fire_c > 0:
        offset, limit = 10, 100
        pygame.draw.rect(screen, (0, 255, 0), (start + offset, 3, min(super_fire_c, limit) * 3, 20), 0)
        if super_fire_c > limit:
            pygame.draw.rect(screen, (0, 139, 0), (start + offset, 3, min(super_fire_c - limit, limit) * 3, 20), 0)
        start += 10 + min(super_fire_c, limit) * 3
    # font = pygame.font.Font(None, 25)
    # text = font.render(f'firepower: {fire_freq - c_fire.freq + 1}', True, (0, 0, 0))
    # rect = text.get_rect()
    # rect.top = 3
    # rect.left = start + 10
    # start += rect.width
    # screen.blit(text, rect)

    font = pygame.font.Font(None, 18)
    text = font.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    rect = text.get_rect()
    rect.top = 3
    rect.right = SCREEN_SIZE[0] - 3
    screen.blit(text, rect)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)
    pygame.mouse.set_visible(0)

    myplane = My_plane()
    bullet_group = pygame.sprite.Group()
    anti_plane_group = pygame.sprite.Group()

    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    c_fire = Counter(8)
    c_newplane = Counter(27)
    super_fire_c = 0

    life = LIFE_MAX

    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_q:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_j:
                anti_plane_group.add(Big_plane())

        if c_fire.run():
            if super_fire_c > 0:
                bullet_group.add(Bullet((myplane.rect.left, myplane.rect.top)))
                bullet_group.add(Bullet((myplane.rect.centerx, myplane.rect.top)))
                bullet_group.add(Bullet((myplane.rect.right, myplane.rect.top)))
                super_fire_c -= 1
            else:
                new_bullet = Bullet((myplane.rect.centerx, myplane.rect.top))
                bullet_group.add(new_bullet)
        if c_newplane.run():
            new_plane = Big_plane() if random.randint(1, 100) <= 12 else Small_plane()
            anti_plane_group.add(new_plane)

        myplane.update(pygame.key.get_pressed())
        for anti in anti_plane_group:
            if anti.update():
                life -= 1
        for bullet in bullet_group:
            bullet.update()

        collision_detection = False
        for anti in anti_plane_group:
            if pygame.sprite.collide_mask(myplane, anti):
                collision_detection = True
                anti.kill()
        if collision_detection:
            life -= 1

        # TODO: 优化复杂度
        for bullet in bullet_group:
            for anti in anti_plane_group:
                if pygame.sprite.collide_mask(bullet, anti):
                    bullet.kill()
                    if anti.be_attacked():
                        if anti.__class__ == Big_plane and random.randint(1, 100) <= 60:
                            super_fire_c += 30
                        anti.kill()
                    break

        if life <= 0:
            myplane.kill()
            screen.fill(BACKGROUND_COLOR)
            font = pygame.font.Font(None, 48)
            text = font.render('GAME OVER', True, (0, 0, 0)) # 黑色
            rect = text.get_rect()
            center, top = screen.get_rect().center
            rect.midtop = center, top
            screen.blit(text, rect)
            pygame.display.flip()
            break

        myplane.draw(screen)
        bullet_group.draw(screen)
        anti_plane_group.draw(screen)
        draw_status()
        pygame.display.flip()
        clock.tick(FPS)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_q:
                sys.exit()
        clock.tick(FPS)
