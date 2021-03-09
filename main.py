import pygame
from pygame import gfxdraw
import time

WIDTH = 1920
HEIGHT = 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
xaxis = WIDTH/1.80 + 150
yaxis = HEIGHT/2
scale = 500

def draw_set(iterations):
    win.fill((0, 0, 0))
    '''
    fc(z) = z^2 +c
    which it does not diverge when iterated from z = 0

    c^2 =
    (a+bi) * (a+bi)
    = a^2 + 2abi - b^2
    = a^2 - b^2 + 2abi
    where a^2 - b^2 is real
    and 2abi is imaginary
    '''
    start = time.time()
    # iy indicates the imaginary number y
    # ix indicates the imaginary number x
    for iy in range(int(HEIGHT / 2 + 1)):   
        for ix in range(WIDTH):
            # 0j tells python it will be imaginary
            # z is a complex number
            # with 0 being real
            # and 0j being imaginary 
            # both start at 0 for first iteration
            z = complex(0 + 0j)
            # both real and complex components
            c = complex(float(ix-xaxis)/scale, float(iy-yaxis)/scale)
            # gets real and imaginary components
            x = c.real
            y = c.imag
            y2 = y * y
            q = ( x - 0.25)**2 + y2
            if (q * (q + (x - 0.25)) >= y2 / 4.0 or (x + 1.0)**2 + y2 < 0.0625):
                for i in range(iterations):

                    z = z**2 + c
                    # abs() value of a complex number is defined as
                    # the distance between the origin and the point a,b
                    # in the complex plane
                    # so (a^2 + b^2) ^ 1/2
                    # or sqrt(a^2 + b^2)
                    if abs(z) > 2:
                        # getting the colour of the pixel
                        v = 765 * i / iterations
                        if v > 510:
                            colour = (255, 255, v % 255)
                        elif v > 255:
                            colour = (100, v % 255 , 255)
                        else:
                            colour = (0 , 0, v % 255)
                        break
                    else:
                        # setting colour to black if the point tends towards infinity
                        colour = (0, 0, 0)


                # draws one half above x axis
                gfxdraw.pixel(win, ix, iy, colour)
                # draws second half below x axis
                gfxdraw.pixel(win, ix, HEIGHT-iy, colour)
                
        # progress
        print(f"{iy / (HEIGHT / 2 + 1) * 100}% - DONE")
    # prints time taken
    end = time.time()
    print(f"Finished in {end - start}s")

    pygame.display.update()

draw_set(100)
