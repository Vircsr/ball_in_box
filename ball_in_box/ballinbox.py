import math
import random
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(m, blockers):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r oif the circle.
    """

    # The following is an example implementation.
    circles = []

    for circle_index in range(m):
        r = 0.0
        x = 0
        y = 0
        i = 0
        while i < 10000:
            rf = 2.0
            xf = random.random() * 2 - 1
            yf = random.random() * 2 - 1
            if circles is not None and len(circles) > 0:
                while not validate(circles, blockers):
                    xf = random.random() * 2 - 1
                    yf = random.random() * 2 - 1
                for circle in circles:
                    x1 = circle[0]
                    y1 = circle[1]
                    r1 = circle[2]
                    rc = math.sqrt((xf - x1)**2 + (yf - y1)**2)
                    if rf > (rc - r1):
                        rf = rc - r1
            for blocker in blockers:
                bx = blocker[0]
                by = blocker[1]
                rb = math.sqrt((xf - bx)**2 + (yf - by)**2)
                if rf > rb:
                    rf = rb
            dd = min([(xf + 1), (1 - xf), (yf + 1), (1 - yf)])
            if rf > dd:
                rf = dd
            if r < rf:
                r = rf
                x = xf
                y = yf
            else:
                i = i + 1
        circles.append((x, y, r))
        print(r)
        if not validate(circles, blockers):
            print('There are some thing wrong')
        circle_index += 1
    
    return circles

