import turtle as t
from random import randrange
from time import sleep

# Simulate an ant walking.
t.hideturtle()
while True:
    n = randrange(-3, +4)
    t.fd(10)
    t.left(30 * n)
    sleep(0.1)
