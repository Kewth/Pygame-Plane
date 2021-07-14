'''
敌人的飞机
'''
import pygame, random
import cfg

class Small_plane (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.life = 3
        self.image = cfg.IMAGE_DICT['small_plane'][self.life - 1]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = - self.rect.height
        self.rect.centerx = + self.rect.width / 2 + \
                random.randrange(cfg.SCREEN_SIZE[0] - self.rect.width)
    '''被攻击'''
    def be_attacked (self):
        self.life -= 1
        if self.life <= 0:
            return True
        self.image = cfg.IMAGE_DICT['small_plane'][self.life - 1]
        return False
    '''更新位置并检查是否入侵'''
    def update (self):
        self.rect.move_ip(0, 2)
        if self.rect.top > cfg.SCREEN_SIZE[1]:
            self.kill()
            return True
        return False

class Big_plane (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.life = 10
        self.image = cfg.IMAGE_DICT['big_plane'][self.life - 1]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = - self.rect.height
        self.rect.centerx = + self.rect.width / 2 + \
                random.randrange(cfg.SCREEN_SIZE[0] - self.rect.width)
    '''被攻击'''
    def be_attacked (self):
        self.life -= 1
        if self.life <= 0:
            return True
        self.image = cfg.IMAGE_DICT['big_plane'][self.life - 1]
        return False
    '''更新位置并检查是否入侵'''
    def update (self):
        self.rect.move_ip(0, 1)
        if self.rect.top > cfg.SCREEN_SIZE[1]:
            self.kill()
            return True
        return False
