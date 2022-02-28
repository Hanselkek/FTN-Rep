# Imports
import pygame
import math

from pygame import mixer
# Scripts
import data
##
from data import NoobsFramework
# Code
pygame.init()
# Window Configures
screen = pygame.display.set_mode((800, 600))
icon_of_game = pygame.image.load('data\IconNoob.png')

bg_info = 'data\main_data\World_1_BG.png'

Background_1 = pygame.image.load(bg_info)
Background_1 = pygame.transform.scale(Background_1, (800, 600))

pygame.display.set_icon(icon_of_game)
pygame.display.set_caption('Find the Noobs')
# Player
default_PosX = 370
default_PosY = 395
playerY_change = 0
playerX_change = 0

playerImage = pygame.image.load('data\main_data\character\player.png')
playerImage = pygame.transform.scale(playerImage, (80, 80))

def isCollided(x, y, tX, tY):
    distance = math.sqrt((math.pow(tX-x, 2)) + (math.pow(tY-y, 2)))
    return distance

def addPlayer(x, y):
   screen.blit(playerImage, (x, y))
# Music
mixer.music.load('data\Sounds\BackgroundMusic.ogg')
mixer.music.set_volume(0.083)
mixer.music.play(-1)
# Noobs Variables
noobIcon_bsNoob = pygame.image.load('data\_Noobs_\_basicnoob_.png')
noobIcon_bsNoob = pygame.transform.scale(noobIcon_bsNoob, (70, 70))

noobIcon_scardyNoob = pygame.image.load('data\_Noobs_\ScardyNoob.png')
noobIcon_scardyNoob = pygame.transform.scale(noobIcon_scardyNoob, (70, 70))

noobIcon_Kaboom = pygame.image.load('data\_Noobs_\KaboomNoob.png')
noobIcon_Kaboom = pygame.transform.scale(noobIcon_Kaboom, (70, 70))

noobIcon_Sleepy = pygame.image.load('data\_Noobs_\SleepyNoob.png')
noobIcon_Sleepy = pygame.transform.scale(noobIcon_Sleepy, (70, 70))

bsn_HAS_BEEN_TAKEN = False
scardy_HAS_BEEN_TAKEN = False
kaboom_HAS_BEEN_TAKEN = False
sleepy_HAS_BEEN_TAKEN = False
# Noobs Adder
def addNoob_Basic(x, y):
    screen.blit(noobIcon_bsNoob, (x, y))

    global bsn_HAS_BEEN_TAKEN

    if bsn_HAS_BEEN_TAKEN == False:
        if isCollided(default_PosX, default_PosY, x, y) < 27:
            bsn_HAS_BEEN_TAKEN = True
            NoobsFramework.update().update_ui(1, "Basic Noob")
def addNoob_Scardy(x, y):
    screen.blit(noobIcon_scardyNoob, (x, y))

    global scardy_HAS_BEEN_TAKEN

    if scardy_HAS_BEEN_TAKEN == False:
        if isCollided(default_PosX, default_PosY, x, y) < 27:
            scardy_HAS_BEEN_TAKEN = True
            NoobsFramework.update().update_ui(1, "Scardy Noob")
def addNoob_Kaboom(x, y):
    screen.blit(noobIcon_Kaboom, (x, y))

    global kaboom_HAS_BEEN_TAKEN

    if kaboom_HAS_BEEN_TAKEN == False:
        if isCollided(default_PosX, default_PosY, x, y) < 27:
            kaboom_HAS_BEEN_TAKEN = True
            NoobsFramework.update().update_ui(1, "Kaboom Noob")
def addNoob_Sleepy(x, y):
    screen.blit(noobIcon_Sleepy, (x, y))

    global sleepy_HAS_BEEN_TAKEN

    if sleepy_HAS_BEEN_TAKEN == False:
        if isCollided(default_PosX, default_PosY, x, y) < 27:
            sleepy_HAS_BEEN_TAKEN = True
            NoobsFramework.update().update_ui(1, "Sleep Noob")

# Game
Game_Is_Open = True

# Game Loop
while Game_Is_Open:
    screen.blit(Background_1, (0, 0))
    screen.blit(NoobsFramework.show().show_ui(), (35, 55))
    screen.blit(NoobsFramework.showRec().showRecent(), (35, 94))

    addNoob_Basic(110, 355)
    addNoob_Scardy(495, 500)
    addNoob_Kaboom(575, 500)
    addNoob_Sleepy(125, 525)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            Game_Is_Open = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                playerY_change = -0.2
            if events.key == pygame.K_DOWN:
                playerY_change = 0.2
            if events.key == pygame.K_ESCAPE:
                quit()
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                playerY_change = 0

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                playerX_change = -0.2
            if events.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                playerX_change = 0
    # Y Barrier
    if default_PosY <= 0:
        default_PosY = 0
    elif default_PosY >= 550:
        default_PosY = 550
    # Other Functions
    default_PosY += playerY_change
    default_PosX += playerX_change

    addPlayer(default_PosX, default_PosY)
    pygame.display.update()
pygame.quit()