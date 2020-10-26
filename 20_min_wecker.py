import time
import pygame

pygame.mixer.init() 
sound1 = pygame.mixer.Sound('song.ogg')  # In dem Ordner muss dann noch eine ogg datei liegen, die dann abgespielt wird

zeit = 0
while True:
    time.sleep(1)
    zeit = zeit + 1
    print(zeit)

    if zeit == 1200:
        zeit = 0
        print("Bro musst Lüften jetzt, in der Zwischenzeit spiele ich für dich einen 187 Song ab")
        sound1.play()
        time.sleep(300)
