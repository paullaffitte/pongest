#coding: utf8
import pygame as key

# Name of the theme
THEME           = "dark"

# Size of the screen (px)
WIDTH_SCREEN    = 1280
HEIGHT_SCREEN   = 720

# Speed of the paddles and ball at the begining (px/s)
SPEED           = 800

# Acceleration of the paddles and the ball when the ball hit a paddle (px/s)
ACCELERATION  = 30

# Speed factors coressponding to the special acceleration keys
SPEED_UP        = 1.8
SPEED_DOWN      = 0.5

# Enable or not the speed wall mode, when it's enlabed, the ball and the paddles get acceleration also when the ball hit a wall
SPEED_WALL      = False

# Keymapping player 1
p1_move_up        = key.K_a
p1_move_down      = key.K_q
p1_speed_up       = key.K_z
p1_speed_down     = key.K_s

# Keymapping player 2
p2_move_up        = key.K_UP
p2_move_down      = key.K_DOWN
p2_speed_up       = key.K_p
p2_speed_down     = key.K_m
