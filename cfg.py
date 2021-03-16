'''
配置文件
'''
import os
import pygame

'''图片路径'''
IMAGE_PATHS = {
        'my_plane': os.path.join(os.getcwd(), 'resources/images/my_plane.png'),
        'small_plane': [os.path.join(os.getcwd(), f'resources/images/small_plane_{i+1}.png') for i in range(3)],
        'big_plane': [os.path.join(os.getcwd(), f'resources/images/big_plane_{i+1}.png') for i in range(10)],
        'bullet': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
        'heart': os.path.join(os.getcwd(), 'resources/images/heart.png'),
        'cross': os.path.join(os.getcwd(), 'resources/images/cross.png'),
        }
'''字体路径'''
FONT_PATH = os.path.join(os.getcwd(), 'resources/fonts/Ubuntu Mono derivative Powerline.ttf')
'''屏幕大小'''
SCREEN_SIZE = (600, 900)
'''生命值'''
LIFE_MAX = 8
'''背景颜色'''
BACKGROUND_COLOR = (255, 255, 255)
'''帧数'''
FPS = 50

'''读取图片资源'''
IMAGE_DICT = {}
for key, value in IMAGE_PATHS.items():
    # print(key, value)
    if value.__class__ == list:
        IMAGE_DICT[key] = [pygame.image.load(item) for item in value]
    else:
        IMAGE_DICT[key] = pygame.image.load(value)
