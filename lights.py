# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from datetime import datetime

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 300
# num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB


# Function to get the current time as a datetime object
def get_current_time():
    now = datetime.now()
    return now.time()


# Function to check if the current time is within the specified time range
def is_time_between(start_time, end_time, current_time):
    if start_time <= end_time:
        return start_time <= current_time <= end_time
    else:
        # Handles time ranges that cross midnight
        return start_time <= current_time or current_time <= end_time


# Define the start and end times for turning on the lights
start_time = datetime.strptime("18:15:00", "%H:%M:%S").time()
end_time = datetime.strptime("01:00:00", "%H:%M:%S").time()

# Create a NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def snake_color(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        b = int(255 - pos * 3)
        g = int(255 - pos * 3)
    else:
        pos -= 170
        r = 0
        b = 0
        g = 0
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.RGB) else (r, g, b, 0)


def snake_flow():
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            # pixels[i] = snake_random(pixel_index & 255)
            pixels[i] = snake_red_and_green(pixel_index & 255)
        pixels.show()
    return


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
    #  time.sleep(wait)
    return

def snake_red_and_green(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:  # Half of the range (0-127) will be red
        r = 255
        g = 0
        b = 0
    else:  # The other half (128-255) will be green
        r = 0
        g = 255
        b = 0

    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)



def snake_random(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0

    elif pos < 85:
        r = int(pos * 3)
        b = int(170 - pos * 1)
        g = int(255 - pos * 3)

    elif pos > 85 and pos < 170:
        r = 0
        g = 0
        b = 0
    elif pos > 171 and pos < 220:
        r = 255
        g = 255
        b = 255
    else:
        r = 0
        g = 0
        b = 0
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.RGB) else (r, g, b, 0)


def string(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 254:
        r = 0
        g = 0
        b = 0
    elif pos == 255:
        r = 255
        g = 0
        b = 0
    else:
        r = 0
        g = 0
        b = 0

    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def blink_white():
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.15)
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(1)
    return

def turn_off_lights():
    pixels.fill((0, 0, 0))
    pixels.show()

def blue(wait):
    ##### color code is GRB #####
    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(wait)


def red(wait):
    ##### color code is GRB #####
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(wait)


def green(wait):
    ##### color code is GRB #####
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(wait)


def purple(wait):
    ##### color code is GRB #####
    pixels.fill((128, 0, 128))
    pixels.show()
    time.sleep(wait)


def pink(wait):
    ##### color code is GRB #####
    pixels.fill((255, 192, 203))
    pixels.show()
    time.sleep(wait)


def turnOff():
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.15)

def red_and_green():
    for pixel in range(num_pixels):  # Make sure to use `range(num_pixels)`
        if pixel % 2 == 0:
            # Even pixel, set to green
            pixels[pixel] = (0, 255, 0)
        else:
            # Odd pixel, set to red
            pixels[pixel] = (255, 0, 0)
    pixels.show()


def blink_colors(wait):
   #  turnOff()
   #  blue(wait)
   #  turnOff()
    red(wait)
    turnOff()
    green(wait)
    turnOff()
   #  purple(wait)
   #  turnOff()
   #  pink(wait)
   #  turnOff()
    return


def run_light_sequence():
    while True:
        current_time = get_current_time()
        if is_time_between(start_time, end_time, current_time):
               # blink_white()
               # for x in range(10):
                  #  rainbow_cycle(0.00001)
               # for x in range(10):
               #     snake_flow(0.00001)
               for x in range(10):
                   blink_colors(1)
               for x in range(10):
                   red_and_green()
                   time.sleep(2)
               for x in range(10):
                   snake_flow()


try:
    run_light_sequence()
except KeyboardInterrupt:
    turn_off_lights()
    print("\nLEDS OFF")

