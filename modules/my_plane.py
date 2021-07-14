'''
玩家的飞机
'''
import pygame
from pygame.locals import *
import cfg

class My_plane (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cfg.IMAGE_DICT['my_plane']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = cfg.SCREEN_SIZE[1]
        self.rect.centerx = cfg.SCREEN_SIZE[0] / 2
    '''更新位置'''
    def update (self, pressed_keys):
        step = 6
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -step)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, +step)
        if pressed_keys[K_a]:
            self.rect.move_ip(-step, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(+step, 0)
        self.rect.bottom = min(cfg.SCREEN_SIZE[1], self.rect.bottom)
        self.rect.top = max(0, self.rect.top)
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(cfg.SCREEN_SIZE[0], self.rect.right)
    # '''自动开火'''
    # def fire (self):
    #     axis = (self.rect.centerx, self.rect.top)
    #     new_bullet = Bullet(axis)
    #     return new_bullet
    '''绘制'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Bullet (pygame.sprite.Sprite):
    def __init__ (self, axis):
        pygame.sprite.Sprite.__init__(self)
        self.image = cfg.IMAGE_DICT['bullet']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = axis
    '''更新位置'''
    def update (self):
        self.rect.move_ip(0, -9)
        if self.rect.bottom <= 0:
            self.kill()
            return True
        return False
