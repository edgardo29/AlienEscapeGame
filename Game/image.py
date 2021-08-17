import pygame
import cv2
import random
import sys

backgroundImg = pygame.image.load('universe.jpg')

screen = pygame.display.set_mode((800,600))


def background():
    screen.blit(backgroundImg,(0,0))

screen.fill(0,0,0)