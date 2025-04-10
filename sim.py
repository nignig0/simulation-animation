import pygame
from pygame.locals import QUIT
import random

from model import sim_model
from predator import Predator
from prey import Prey
import time

pygame.init()
HEIGHT = 500
WIDTH = 1000
RECT_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
NUM_PREY = 100
NUM_PREDATOR = 2

prey_list = []
predator_list = []

X, Y = sim_model(NUM_PREY, NUM_PREDATOR)
X = [int(x) for x in X]
Y = [int(y) for y in Y]

def spawn_prey(number):
    for _ in range(number):
        collides = True
        x, y = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)
        temp = Prey(x, y, RECT_SIZE)
        while collides:
            x, y = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)
            temp = Prey(x, y, RECT_SIZE)
            collides = any([temp.rect.colliderect(prey.rect) for prey in prey_list])
            collides = any([temp.rect.colliderect(predator.rect) for predator in predator_list])

        prey_list.append(temp)

def kill_prey(number):

    for _ in range(number):
        prey_list.pop()

def spawn_predator(number):
    for _ in range(number):
        collides = True
        x, y = random.randrange(0, WIDTH-RECT_SIZE), random.randrange(0, HEIGHT-RECT_SIZE)
        temp = Predator(x, y, RECT_SIZE)
        while collides:
            x, y = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)
            temp = Predator(x, y, RECT_SIZE)
            collides = any([temp.rect.colliderect(predator.rect) for predator in predator_list])
            collides = any([temp.rect.colliderect(prey.rect) for prey in prey_list])
        
        predator_list.append(temp)

def kill_predator(number):
    for _ in range(number):
        predator_list.pop()


frame_counter = 0         

while frame_counter < len(X):

    for event in pygame.event.get(): #get events
        if event.type == QUIT:
            running = False
    if X[frame_counter]  > len(prey_list):
        spawn_prey(X[frame_counter] - len(prey_list))
    else:
        kill_prey(len(prey_list) - X[frame_counter])

    if Y[frame_counter]  > len(predator_list):
        spawn_predator(Y[frame_counter] - len(predator_list))
    else:
        kill_predator(len(predator_list) - Y[frame_counter])
    
    screen.fill((0, 0, 0))
    for prey in prey_list:
        prey.draw(screen)
    
    for predator in predator_list:
        predator.draw(screen)
    
    pygame.display.flip()


    frame_counter+=1   
    time.sleep(1)

pygame.quit() 