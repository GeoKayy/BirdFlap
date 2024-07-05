import pygame
import random

pygame.init()
birdy = 0
gap = 100
gapy = random.randint(100, 1720)
screen = pygame.display.set_mode((900, 900))
screen.fill((0, 200, 255))
mdown = False
clock = pygame.time.Clock()
boxy = 450
boxvely = 0
obX = 1600
obY = random.randint(1, 900)
boxx = 0
boxxx = 10
respawnr = False
respawnl = False
p1r = 0
p2r = 0
p3r = 0
spikesr = []
spikesl = []
dead = False
score = 0
bird = pygame.image.load("actualbird.png")
birdflip = pygame.image.load("birdflip.png")
logo = pygame.image.load("wing.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Bird Flap")
numFont = pygame.font.SysFont("twcen", 200)
pointsdisplay = numFont.render(str(score), 1, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False

    if not mdown:
        boxvely -= 0.8
    elif mdown:
        boxvely = 15
        mdown = False

    if boxvely >= 20:
        boxvely = 20
    elif boxvely <= -20:
        boxvely = -20

    screen.fill((0, 200, 255))
    boxy -= boxvely
    boxx += boxxx

    if boxy <= 19:
        dead = True
        
    if boxy >= 820:
        dead = True
        
    if boxx >= 836:
        boxxx = -10
        respawnr = True
        score += 1
        
    elif boxx <= 0:
        boxxx = 10
        respawnl = True
        score += 1
        
    if respawnr:
        spikesr = []
        for i in range(9):
            rannum = random.randint(0,19)
            p1r = (0, rannum*45)
            p2r = (0, rannum*45+45)
            p3r = (20, rannum*45+22.5)
            spikesr.append((p1r, p2r, p3r))
        respawnr = False

    if respawnl:
        spikesl = []
        for i in range(9):
            rannum = random.randint(0,19)
            p1l = (900, rannum*45)
            p2l = (900, rannum*45+45)
            p3l = (880, rannum*45+22.5)
            spikesl.append((p1l, p2l, p3l))
        respawnl = False

    for spike in spikesr:
        pygame.draw.polygon(screen, (255, 0, 0), spike)

    for spike in spikesl:
        pygame.draw.polygon(screen, (255, 0, 0), spike)

    for i in range(len(spikesr)):
        if spikesr[i][2][1] >= boxy and spikesr[i][2][1] <= boxy+64 and boxx <= 30:
            dead = True
    for i in range(len(spikesl)):
        if spikesl[i][2][1] >= boxy and spikesl[i][2][1] <= boxy+64 and boxx >= 806:
            dead = True
            
    pointsdisplay = numFont.render(str(score), 1, (255, 255, 255))

    if dead:
        respawnr = False
        respawnl = False
        boxx = 450
        boxy = 450
        boxvely = 0
        dead = False
        spikesr = []
        spikesl = []
        score = 0

    if score < 10:
        screen.blit(pointsdisplay, (390, 350))
    else:
        screen.blit(pointsdisplay, (360, 350))

    if boxxx == 10:
        screen.blit(bird, (boxx, boxy))
    else:
        screen.blit(birdflip, (boxx, boxy))
    pygame.draw.rect(screen, (255, 0, 0), (0, 877.5, 900, 23))
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 900, 23))
    pygame.display.flip()
    clock.tick(60)
