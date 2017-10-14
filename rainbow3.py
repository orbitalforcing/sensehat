from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

image1 = [
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v
]

image2 = [
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i
]

image3 = [
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b
]

image4 = [
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g
]

image5 = [
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y
]

image6 = [
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o
]

image7 = [
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e,
r,r,r,r,r,r,r,r
]

image8 = [
r,r,r,r,r,r,r,r,
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
i,i,i,i,i,i,i,i,
v,v,v,v,v,v,v,v,
e,e,e,e,e,e,e,e
]

while True:
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)
    sense.set_pixels(image3)
    sleep(1)
    sense.set_pixels(image4)
    sleep(1)
    sense.set_pixels(image5)
    sleep(1)
    sense.set_pixels(image6)
    sleep(1)
    sense.set_pixels(image7)
    sleep(1)
    sense.set_pixels(image8)
    sleep(1)
    