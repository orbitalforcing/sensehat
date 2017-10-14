from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)
message = "Steve is cool!!!"
speed = 0.1

while True:
    sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
