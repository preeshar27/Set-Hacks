#imports and initializations

import pygame
import random
import time

pygame.init()

def showmenu(showend):
    if showend:
        while True:
            screen.blit(end, (0, 0))
            pygame.display.update()

            clickx, clicky = getmouseclicks()

            if clickx >= 831 and clickx <= 940:
                if clicky >= 388 and clicky <= 462:
                    showmenu(False)
    
    while True:
        
        screen.blit(menu, (0, 0))
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if (clickx >= 40 and clickx <= 149) and (clicky >= 330 and clicky <= 404):
                showlevelinfo(0)

        if (clickx >= 40 and clickx <= 171) and (clicky >= 427 and clicky <= 501):
                showrules()

def showrules():
    while True:
        screen.blit(rules, (0,0))
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if clickx >= 30 and clickx <= 139:
            if clicky >= 388 and clicky <= 462:
                showmenu(False)

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                showlevelinfo(0)

def showlevelinfo(level):
    while True:
        screen.blit(levelinstr[level], (0, 0))
        pygame.display.update()
        
        clickx, clicky = getmouseclicks()

        if clickx >= 365 and clickx <= 621:
            if clicky >= 408 and clicky <= 458:
                showlevel(level)

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                showmenu(False)

def showlevel(level):
    while True:
        screen.blit(levels[level], (0, 0))

        if level == 0 or level == 3:
            choices[level] = [False, False, False, False]
        
        elif level == 1:
            choices[level] = [[False, False], [False, False], [False, False], [False, False]]

        elif level == 2:
            choices[level] = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
            pygame.display.update()
            getinput(level)

        elif level == 4:
            choices[level] = [False, False, False]
            
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                showmenu(False)

        if clickx >= 395 and clickx <= 568:
            if clicky >= 408 and clicky <= 458:
                print("not ticked enough")

        if level == 0 or level == 3:
            if clickx >= 253 and clickx <= 278:
                if clicky >= 225 and clicky <= 250:
                    choices[level][0] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 273 and clicky <= 298:
                    choices[level][1] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 318 and clicky <= 343:
                    choices[level][2] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 358 and clicky <= 383:
                    choices[level][3] = True
                    showtick(clickx, clicky, level)
                
                else:
                    continue

        elif level == 4:
            if clickx >= 253 and clickx <= 278:
                if clicky >= 225 and clicky <= 250:
                    choices[level][0] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 273 and clicky <= 298:
                    choices[level][1] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 318 and clicky <= 343:
                    choices[level][2] = True
                    showtick(clickx, clicky, level)
        
        elif level == 1:
            if clickx >= 330 and clickx <= 351:
                if clicky >= 237 and clicky <= 258:
                    choices[level][0][0] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 283 and clicky <= 304:
                    choices[level][1][0] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 323 and clicky <= 344:
                    choices[level][2][0] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 363 and clicky <= 384:
                    choices[level][3][0] = True
                    showtick(clickx, clicky, level)
                
                else:
                    continue

            if clickx >= 602 and clickx <= 623:
                if clicky >= 237 and clicky <= 258:
                    choices[level][0][1] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 283 and clicky <= 304:
                    choices[level][1][1] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 323 and clicky <= 344:
                    choices[level][2][1] = True
                    showtick(clickx, clicky, level)

                elif clicky >= 363 and clicky <= 384:
                    choices[level][3][1] = True
                    showtick(clickx, clicky, level)
                
                else:
                    continue

def getinput(level):
    font = pygame.font.Font(pygame.font.get_default_font(), 14)
    actives = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    inputboxes = [pygame.Rect(410, 215, 142, 23), pygame.Rect(410, 245, 142, 21), pygame.Rect(410, 270, 142, 21), pygame.Rect(410, 298, 142, 21), pygame.Rect(410, 327, 142, 21), pygame.Rect(410, 354, 142, 21), pygame.Rect(410, 382, 142, 21), pygame.Rect(593, 215, 142, 23), pygame.Rect(593, 245, 142, 21), pygame.Rect(593, 270, 142, 21), pygame.Rect(593, 298, 142, 21), pygame.Rect(593, 327, 142, 21), pygame.Rect(593, 354, 142, 21), pygame.Rect(593, 382, 142, 21)]

    while True:
        chosen = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

                
            for x in range(len(inputboxes)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if inputboxes[x].collidepoint(event.pos):
                        chosen
                        # Toggle the active variable.
                        actives[x] = not actives[x]
                    else:
                        actives[x] = False
                        clickx, clicky = pygame.mouse.get_pos()

                        if clickx >= 831 and clickx <= 940:
                            if clicky >= 388 and clicky <= 462:
                                showmenu(False)

                        if clickx >= 395 and clickx <= 568:
                            if clicky >= 408 and clicky <= 458:
                                showresults(level)
                        
                if event.type == pygame.KEYDOWN:
                    if actives[x] == True:
                        if event.key == pygame.K_RETURN:
                            level3ticks[x] = ''
                        elif event.key == pygame.K_BACKSPACE:
                            level3ticks[x] = level3ticks[x][:-1]
                        else:
                            level3ticks[x] += event.unicode
                
                txt_surface = font.render(level3ticks[x], True, (0,0,0))
                screen.blit(txt_surface, (inputboxes[x].x+5, inputboxes[x].y+5))
                pygame.display.update()

def showtick(x, y, level):
    while True:
        if level == 0 or level == 3 or level == 4:
            screen.blit(tick, (x - 23, y - 23))

        elif level == 1:
            screen.blit(tick, (x-15, y-20))
            
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                showmenu(False)

 
        if clickx >= 395 and clickx <= 568:
            if clicky >= 408 and clicky <= 458:
                if level == 0:
                    print("ticked enough")
                    
                elif level == 1 or level == 3 or level == 4:
                    showresults(level)

            

        if level == 0:
            if clickx >= 253 and clickx <= 278:
                if clicky >= 225 and clicky <= 250:
                    if choices[level][0] != True:
                        choices[level][0] = True
                        showtick2(clickx, clicky, level)

                elif clicky >= 273 and clicky <= 298:
                    if choices[level][1] != True:
                        choices[level][1] = True
                        showtick2(clickx, clicky, level)

                elif clicky >= 318 and clicky <= 343:
                    if choices[level][2] != True:
                        choices[level][2] = True
                        showtick2(clickx, clicky, level)

                elif clicky >= 358 and clicky <= 383:
                    if choices[level][3] != True:
                        choices[level][3] = True
                        showtick2(clickx, clicky, level)
                
                else:
                    continue

        elif level == 3:
            if clickx >= 253 and clickx <= 278:
                if clicky >= 225 and clicky <= 250:
                    if choices[level][0] != True:
                        choices[level][0] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 273 and clicky <= 298:
                    if choices[level][1] != True:
                        choices[level][1] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 318 and clicky <= 343:
                    if choices[level][2] != True:
                        choices[level][2] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 358 and clicky <= 383:
                    if choices[level][3] != True:
                        choices[level][3] = True
                        showtick(clickx, clicky, level)

        elif level == 4:
            if clickx >= 253 and clickx <= 278:
                if clicky >= 225 and clicky <= 250:
                    if choices[level][0] != True:
                        choices[level][0] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 273 and clicky <= 298:
                    if choices[level][1] != True:
                        choices[level][1] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 318 and clicky <= 343:
                    if choices[level][2] != True:
                        choices[level][2] = True
                        showtick(clickx, clicky, level)
        

        elif level == 1:
            if clickx >= 330 and clickx <= 351:
                if clicky >= 237 and clicky <= 258:
                    if choices[level][0][0] != True:
                        choices[level][0][0] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 283 and clicky <= 304:
                    if choices[level][1][0] != True:
                        choices[level][1][0] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 323 and clicky <= 344:
                    if choices[level][2][0] != True:
                        choices[level][2][0] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 363 and clicky <= 384:
                    if choices[level][3][0] != True:
                        choices[level][3][0] = True
                        showtick(clickx, clicky, level)
                
                else:
                    continue

            if clickx >= 602 and clickx <= 623:
                if clicky >= 237 and clicky <= 258:
                    if choices[level][0][1] != True:
                        choices[level][0][1] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 283 and clicky <= 304:
                    if choices[level][1][1] != True:
                        choices[level][1][1] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 323 and clicky <= 344:
                    if choices[level][2][1] != True:
                        choices[level][2][1] = True
                        showtick(clickx, clicky, level)

                elif clicky >= 363 and clicky <= 384:
                    if choices[level][3][1] != True:
                        choices[level][3][1] = True
                        showtick(clickx, clicky, level)
                
                else:
                    continue

def showtick2(x, y, level):
    while True:
        screen.blit(tick, (x - 23, y - 23))
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if clickx >= 253 and clickx <= 278:
            if clicky >= 225 and clicky <= 250:
                print("checked max error")

            elif clicky >= 273 and clicky <= 298:
                print("checked max error")

            elif clicky >= 318 and clicky <= 343:
                print("checked max error")

            elif clicky >= 358 and clicky <= 383:
                print("checked max error")
            
            else:
                continue

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                showmenu(False)

        if clickx >= 395 and clickx <= 568:
            if clicky >= 408 and clicky <= 458:
                showresults(level)

def showresults(level):
    result = determineresults(level)

    if result == True:
        showwin(level)

    else:
        showlose(level)

def determineresults(level):
    if level == 2 or level == 4:
       return True

    elif level == 3:
        trues = 0
        print(choices[level])
        for x in range(4):
            if choices[level][x] == True:
                trues += 1

        if trues >= 2:
            return True

        else:
            return False
    
    for x in range(4):
        if choices[level][x] != answers[level][x]:
            return False

    return True

def showwin(level):
    while True:
        if level == 2:
            imports = 0
            exports = 0
            for x in range(7):
                if x < 7:
                    imports += int(level3ticks[x])
                else:
                    exports += int(level3ticks[x])

            result = exports / imports
            print(result)

            if result < 0:
                screen.blit(extrawin, (0, 0))

            else:
                screen.blit(wins[level], (0, 0))

        else:
            screen.blit(wins[level], (0, 0))

        pygame.display.update()
        clickx, clicky = getmouseclicks()

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                if level == 4:
                    showmenu(True)

                else:
                    showlevelinfo(level + 1)

def showlose(level):
    while True:
        screen.blit(loses[level], (0, 0))
        pygame.display.update()

        clickx, clicky = getmouseclicks()

        if clickx >= 831 and clickx <= 940:
            if clicky >= 388 and clicky <= 462:
                print("lost game at", level)
                showmenu(True)
    

# Gets the x and y co-ordinates of the pointer every time the mouse is clicked.
def getmouseclicks():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #pygame.mixer.Sound.play(mouseclicksound)
                clickx, clicky = pygame.mouse.get_pos()
                return clickx, clicky

            # If the event was the user clicking top left
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()


#loading stuff
menu = pygame.image.load(r'menu.png')
rules = pygame.image.load(r'rules.png')
clock = pygame.time.Clock()

level1i = pygame.image.load(r'level1 intro.png')
level2i = pygame.image.load(r'level2 intro.png')
level3i = pygame.image.load(r'level3 intro.png')
level4i = pygame.image.load(r'level4 intro.png')
level5i = pygame.image.load(r'level5 intro.png')

level1 = pygame.image.load(r'level1.png')
level2 = pygame.image.load(r'level2.png')
level3 = pygame.image.load(r'level3.png')
level4 = pygame.image.load(r'level4.png')
level5 = pygame.image.load(r'level5.png')

win1 = pygame.image.load(r'win1.png')
win2 = pygame.image.load(r'win2.png')
win3 = pygame.image.load(r'win3.png') # this is for when you have trade >= 0
win4 = pygame.image.load(r'win4.png')
win5 = pygame.image.load(r'win5.png')

extrawin = pygame.image.load(r'extrawin.png') # level 3 when trade <= 0

lose1 = pygame.image.load(r'lose1.png')
lose2 = pygame.image.load(r'lose2.png')
lose3 = pygame.image.load(r'lose2.png')
lose4 = pygame.image.load(r'lose4.png')

tick = pygame.image.load(r'tick1.png')
tick = pygame.transform.scale(tick, (45, 45))

levelinstr = [level1i, level2i, level3i, level4i, level5i]
levels = [level1, level2, level3, level4, level5]

end = pygame.image.load(r'end.png')

level1ticks = [False, False, False, False]
level2ticks = [[False, False], [False, False], [False, False], [False, False]]
level3ticks = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
level4ticks = [False, False, False, False]
level5ticks = [False, False, False]

level1ans = [False, True, False, True]
level2ans = [[True, True], [False, False], [True, False], [True,True]]
level3ans = ["depends on the division"]
level4ans = ["again depends"]
level5ans = ["win regardless"]

choices = [level1ticks, level2ticks, level3ticks, level4ticks, level5ticks]
answers = [level1ans, level2ans, level3ans, level4ans, level5ans]

wins = [win1, win2, win3, win4, win5]
loses = [lose1, lose2, lose3, lose4]

inputbox1 = pygame.Rect(100, 100, 140, 32)

run = True
while run:
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Orths Economic Game...?")

    showmenu(False)
    
pygame.quit()
exit()

  
