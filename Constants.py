import arcade
import os

PLAY_BUTTON = "src" + os.sep + "sprites" + os.sep + "playbutton.png"

GET_READY_MESSAGE = "src" + os.sep + "sprites" + os.sep + "message.png"

GAME_OVER = "src" + os.sep + "sprites" + os.sep + "gameover.png"

BASE = "src" + os.sep + "sprites" + os.sep + "base.png"

BACKGROUNDS = ["src" + os.sep + "sprites" + os.sep + "day_time.png","src" + os.sep + "sprites" + os.sep + "sunset.png"] 

PIPES = ["src" + os.sep + "sprites" + os.sep + "pipe-green.png", "src" + os.sep + "sprites" + os.sep + "pipe-red.png"]

BIRDS = {'yellow': ["src" + os.sep + "sprites" + os.sep + "yellowbird-downflap.png", "src" + os.sep + "sprites" + os.sep + "yellowbird-midflap.png",
                    "src" + os.sep + "sprites" + os.sep + "yellowbird-upflap.png"],
         'red': ["src" + os.sep + "sprites" + os.sep + "redbird-downflap.png", "src" + os.sep + "sprites" + os.sep + "redbird-midflap.png",
                    "src" + os.sep + "sprites" + os.sep + "redbird-upflap.png"],
         'blue': ["src" + os.sep + "sprites" + os.sep + "bluebird-downflap.png", "src" + os.sep + "sprites" + os.sep + "bluebird-midflap.png",
                    "src" + os.sep + "sprites" + os.sep + "bluebird-upflap.png"]}

SOUNDS = {'wing': arcade.load_sound("src" + os.sep + "audio" + os.sep + "wing.wav"),
          'die': arcade.load_sound("src" + os.sep + "audio" + os.sep + "die.wav"),
          'hit': arcade.load_sound("src" + os.sep + "audio" + os.sep + "hit.wav"),
          'point': arcade.load_sound("src" + os.sep + "audio" + os.sep + "point.wav"),
          'swoosh': arcade.load_sound("src" + os.sep + "audio" + os.sep + "swoosh.wav")}



MIN_HEIGHT = 50


GAP_SIZE = 120

JUMP_DY = 60
# Speed of x pixels
JUMP_STEP = 4
DY = 2
# Gravity
GRAVITY = 2

ANGUP = 15
ANGDOWN = -1.5

SCORE = {
    '0': 'src' + os.sep + 'sprites' + os.sep + '0.png',
    '1': 'src' + os.sep + 'sprites' + os.sep + '1.png',
    '2': 'src' + os.sep + 'sprites' + os.sep + '2.png',
    '3': 'src' + os.sep + 'sprites' + os.sep + '3.png',
    '4': 'src' + os.sep + 'sprites' + os.sep + '4.png',
    '5': 'src' + os.sep + 'sprites' + os.sep + '5.png',
    '6': 'src' + os.sep + 'sprites' + os.sep + '6.png',
    '7': 'src' + os.sep + 'sprites' + os.sep + '7.png',
    '8': 'src' + os.sep + 'sprites' + os.sep + '8.png',
    '9': 'src' + os.sep + 'sprites' + os.sep + '9.png',
}