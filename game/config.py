# coding: utf-8

# PYGAME
WIDTH = 800
HEIGHT = 600

FPS = 120

# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# LOGIN
LOGIN_BG_POS = (-200, 0)

USERNAME_RECT = (300, 230, 200, 32)
PASSWORD_RECT = (305, 378, 200, 32)
FIELD_COLOR = (140, 140, 140)

LOGIN_FONT = "Viner Hand ITC"

USERNAME_TITLE = "Username :"
USERNAME_LENGTH = 10
PASSWORD_TITLE = "Password :"
PASSWORD_LENGTH = 20

PASSWORD_FIELD_RECT = (280, 370, 200, 32)

VALIDATE_POS = (305, 425)
VALIDATE_TEXT_POS = (365, 458)
VALIDATE_TEXT = "ENTER"
VALIDATE_FONT = "Felix Titling"

ERROR_TEXT = "Username or Password is invalid."
ERROR_FONT = "Copperplate Gothic"
ERROR_BG_POS = (220, 285)
ERROR_BUTTON_POS = (562, 305)
ERROR_TEXT_POS = (260, 320)

SAVE_USERNAME_POS = (275, 290)
SAVE_USERNAME_TEXT = "Remember me"

# DATABASE ALEX
HOST="alencon-python-2020-p2-db.pythonrover.wilders.dev"
PORT="15003"
DATABASE="SavalFer"
USER="PG2006"
# NEEDS TO BE SECURE
PASSWORD="PG2006p2"
DB_PREFIX = "Game_server"


# DATABASE AURE
# HOST="localhost"
# DATABASE_2="p2test2"
# USER="postgres"
# # NEEDS TO BE SECURE
# PASSWORD_2="Formation2020-at"
# DB_PREFIX = "Projet_2"

# Accounts
# 1
# Username = Beta_Test1
# Password = Test_2020!
# 2
# Username = Beta_Test2
# Password = Test_2022!

# GAME

# Warper
WARPER_FONT = "assets/fonts/CompassPro.ttf"

# Actions
SHOW_ACTIONS_FONT = "assets/fonts/EquipmentPro.ttf"

# DECAY TIMER
HYDRATION_DECAY_TIMER = 180000  # 3 min
SATIETY_DECAY_TIMER = 300000    # 5 min
ENERGY_DECAY_TIMER = 120000     # 2 min
