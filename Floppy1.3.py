import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)
import pygame
import pgzrun
import random

TITLE = 'Flappy Bird'
WIDTH = 500
HEIGHT = 800

PipeTopSprite = Actor('pipetop')
PipeTopSprite.pos = (250,75)
PipeBottomSprite = Actor('pipebottom')
PipeBottomSprite.pos = (250,725)
birdSprite = Actor('bird1')
birdSprite.pos = (50,400)

pipe_speed = 3
gravity = 0.5
birdSprite.vy = 0
game_state = ''
score = 0

def on_key_down():
    if keyboard.space == True :
        birdSprite.vy = -5
        if birdSprite.y <= 0 :
            birdSprite.y = 0 

def birdMove():
    global game_state
    birdSprite.vy = birdSprite.vy + gravity
    birdSprite.y = birdSprite.y + birdSprite.vy
    if birdSprite.vy < 0 :
       birdSprite.image = 'bird2'
    else :
        birdSprite.image = 'bird1'
    if (birdSprite.colliderect(PipeTopSprite) or birdSprite.colliderect(PipeBottomSprite)) or birdSprite.y >= 800:
        birdSprite.y = 800
        game_state = 'gameover'

def pipeMove():
    global score
    global game_state
    pipe_randommove = random.randint(-100,250)
    PipeTopSprite.x = PipeTopSprite.x - pipe_speed
    PipeBottomSprite.x = PipeBottomSprite.x - pipe_speed
    if PipeBottomSprite.x <= 0 or PipeTopSprite.x <=0 :
        PipeTopSprite.x = 500
        PipeBottomSprite.x = 500
        PipeTopSprite.pos = (PipeTopSprite.x, 0 + pipe_randommove)
        PipeBottomSprite.pos = (PipeBottomSprite.x, 650 + pipe_randommove)
        score = score + 1
        print('score is ', score)
    if score >= 5:
        game_state = 'win'

def update():
    global game_state
    if game_state == 'play' :
        pipeMove()
        birdMove()

def draw():
    #global game_state
    screen.blit('background',(0,0))
    def restart():
        global game_state
        global score
        screen.draw.text('Press s to start', center = (250,350), color = 'lightgoldenrod1', fontsize =35)
        if keyboard.s == True :
            game_state = 'play'
            birdSprite.pos = (40,400)
            score = 0
            PipeTopSprite.x = 500
            PipeBottomSprite.x = 500
            
    if game_state == '' :
        screen.draw.text('Flappy Bird', center = (250,300), color = 'cornsilk1', fontsize = 50)
        restart()
        
    elif game_state == 'gameover':
        screen.draw.text('Game Over!', center = (250,300), color = 'slateblue4', fontsize = 50)
        restart()

    elif game_state == 'win' :
        screen.draw.text('You are the winner', center = (250,300), color = 'slategray1', fontsize = 50)
        restart()
        
    elif game_state == 'play':
        PipeTopSprite.draw()
        PipeBottomSprite.draw()
        birdSprite.draw()
        screen.draw.text('score : ' + str(score), (15,10), color = 'seashell1', fontsize = 25)

            
pgzrun.go()
