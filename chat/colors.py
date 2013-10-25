import colorsys
import random

def get_random_color():
    return get_web_color(*colorsys.hls_to_rgb(random.random(), .4, .8))

def get_web_color(r, g, b):
    return '%x%x%x' % (r * 255, g * 255, b * 255)
    
